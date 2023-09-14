from datetime import datetime, timedelta
from pathlib import Path
from typing import cast, Final
import contextlib

from contrail.security.onlineca.client import OnlineCaClient
from cryptography import x509
from cryptography.hazmat.backends import default_backend

DEFAULT_CERTS_DIR: Final = Path.home() / ".certs"
DEFAULT_COOKIEJAR: Final = Path.home() / "dods_cookies"
DEFAULT_DODSRC_FILE: Final = Path.home() / ".dodsrc"
DEFAULT_PEM_FILE: Final = DEFAULT_CERTS_DIR / "ceda-dods.pem"


# Based upon code at https://github.com/cedadev/opendap-python-example
def auth(
    *,
    username: str,
    password: str,
    min_ttl=timedelta(minutes=30),
    force=False,
    dodsrc_file=DEFAULT_DODSRC_FILE,
    certs_dir=DEFAULT_CERTS_DIR,
    pem_file=DEFAULT_PEM_FILE,
    cookie_jar=DEFAULT_COOKIEJAR,
) -> datetime:
    with contextlib.suppress(Exception):
        pem_bytes = pem_file.read_bytes()
        cert = x509.load_pem_x509_certificate(pem_bytes, default_backend())
        # sourcery skip: aware-datetime-for-utc
        now = datetime.utcnow()
        cert_valid = cert.not_valid_before <= now < cert.not_valid_after - min_ttl

        if dodsrc_file.exists() and not force and cert_valid:
            return cert.not_valid_after

    trustroots_dir = certs_dir / "ca-trustroots"
    trustroots_dir.mkdir(parents=True, exist_ok=True)
    client = OnlineCaClient()
    client.ca_cert_dir = str(trustroots_dir)
    client.get_trustroots(
        "https://slcs.ceda.ac.uk/onlineca/trustroots/",
        write_to_ca_cert_dir=True,
        bootstrap=True,
    )

    # Write certificate credentials file
    _, (cert, *_) = client.get_certificate(
        username,
        password,
        "https://slcs.ceda.ac.uk/onlineca/certificate/",
        pem_out_filepath=pem_file,
    )

    _write_dodsrc_file(
        dodsrc_file,
        pem_file=pem_file,
        trustroots_dir=trustroots_dir,
        cookie_jar=cookie_jar,
    )

    return datetime.strptime(cast(bytes, cert.get_notAfter()).decode(), "%Y%m%d%H%M%SZ")


def _write_dodsrc_file(
    dodsrc_file: Path,
    *,
    pem_file: Path,
    trustroots_dir: Path,
    cookie_jar: Path,
) -> None:
    dodsrc_file.write_text(
        "\n".join(
            [
                f"HTTP.COOKIEJAR={cookie_jar}",
                f"HTTP.SSL.CERTIFICATE={pem_file}",
                f"HTTP.SSL.KEY={pem_file}",
                f"HTTP.SSL.CAPATH={trustroots_dir}",
            ]
        )
    )
