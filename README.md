# Geospatial Cholera Lab

A repository dedicated to developing a geospatial data science prototype (see
issue: <https://github.com/developmentseed/labs/issues/292>).

## The Objective

To explore the use of machine learning techniques on publicly available,
open-sourced datasets to demonstrate the potential to predict cholera in endemic
regions of the world, which could be developed further as part of a public
health planning and decision making tool for humanitarian organizations.
Develop a PoC based only on open-source data to showcase ML capabilities in this
space which could be developed further to support decision tool development in
this space, and provide more context to cholera patterns than is provided by
cases alone.

## Literature Support

In cholera-endemic countries, there is
[support of environmental signatures between seasonal outbreaks](https://www.pnas.org/doi/10.1073/pnas.0809654105)
which could be explored and used to develop a framework for an early warning
system.  See also
[The seasonality of cholera in sub-Saharan Africa: a statistical modelling study](https://www.thelancet.com/journals/langlo/article/PIIS2214-109X(22)00007-9/fulltext),
for supporting work in this area.

## The Challenge

* [Cholera](https://www.who.int/news-room/fact-sheets/detail/cholera) can be
  both endemic (where seasonal patterns are more likely) and epidemic (based on
  a perfect storm of conditions).  Environmental factors are just one component,
  there are a number of complex factors at play (e.g., human development
  indices, access to basic hand-washing, natural disasters, etc.)
* Surveillance isn’t perfect, many areas across the globe have varying
  levels/resources allocated to disease surveillance (as we’ve seen with Covid)
  so reported cases aren’t always representative of the true picture.

## Proposed open-source, available datasets

(_WIP_) Focus on an area where endemic cholera is a major issue, and where
subnational and sub annual surveillance data is available: _Sub-Saharan Africa_.
Data availability during this time frame will also allow us to take advantage of
a number of remotely sensed variables captured over the same time-frame.

* cholera surveillance (initial dataset proposed for PoC:
  [Cholera outbreaks in sub-Saharan Africa 2010-2019](https://github.com/HopkinsIDD/cholera_outbreaks_ssa),
  see `data/outbreak_data.csv`)
* sea level (source:
  [ESA Climate Data Dashboard](https://climate.esa.int/en/odp/#/dashboard))
* sea surface temperate (source:
  [ESA Climate Data Dashboard](https://climate.esa.int/en/odp/#/dashboard))
* gridded rainfall data (source:
  [global summary of monthly meteorological data from NOAA](https://www.ncdc.noaa.gov/cdo-web/datasets))
* gridded air temperature data (source:
  [global summary of monthly meteorological data from NOAA](https://www.ncdc.noaa.gov/cdo-web/datasets))
* world population data (source: [WorldPop](https://www.worldpop.org/))
* human development indices (source:
  [INFORM indices](https://drmkc.jrc.ec.europa.eu/inform-index),
  [Human Development Reports/data](https://hdr.undp.org/data-center/human-development-index#/indicies/HDI))

## Proposed Methodology

1. Exploratory spatial data analysis (what patterns can be observed from the
   cholera cases themselves?)
1. Principal component analysis (or similar) to explore correlative indices and
   narrow down list of covariate factors entered into the model
1. Exploration of machine learning model approaches (e.g., Random Forest, SVMs,
   etc.) to develop a model between cholera cases, environmental and
   socio-economic factors
1. Provide visuals of model results

_All to be shared, initially, in a series of Jupyter notebooks_.

## Hypothesis

Environmental and socio-economic factors alone won’t unravel this very complex
relationship, but they can help identify spatio-temporal patterns that could
help assist in allocating resources and support.

## Setting up your local environment

### Install conda and create conda environment

Install `conda`.  The recommended way to do this is by installing
[miniforge](https://github.com/conda-forge/miniforge).

If you are running macOS, the easiest way to do this is to install
[Homebrew](https://brew.sh/), if not already installed, and run the following:

```plain
brew install miniforge
conda init
```

Then, close your terminal and open a new terminal session.

Once, `conda` is installed, run the following commands in your terminal to
create your the environment used for this repository:

```plain
conda env create
conda activate geo-ds-cholera
```

Whenever you modify the `environment.yml` file, run the following command to
update your conda environment:

```plain
conda env update
```

### Install pre-commit and pre-commit hooks

To aid development, this repository uses the `pre-commit` tool, which is
installed into the conda environment created above.  To install the pre-commit
hooks defined in `.pre-commit-config.yaml`, you must run the following command
from the root of your cloned repository working directory:

```plain
pre-commit install --install-hooks
```

If you wish to run the pre-commit hooks in order to check your changes prior to
committing your changes to git, you can run the following command, but note that
files that are untracked by git will be ignored by the pre-commit hooks.
Therefore, if there are untracked files that you wish to check, you must at
least use `git add` to stage them in order for the pre-commit hooks to check
them:

```plain
pre-commit run -a
```
