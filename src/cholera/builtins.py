from collections.abc import Mapping
from typing import Any


def compress_kwargs(**kwargs: Any) -> Mapping[str, Any]:
    return {k: v for k, v in kwargs.items() if v is not None}
