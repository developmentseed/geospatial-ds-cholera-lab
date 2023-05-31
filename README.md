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

Focus on an area where cholera has been identified as a major issue, and where
subnational and sub annual surveillance data is available: _Sub-Saharan Africa_.
Data availability during this time frame will also allow us to take advantage of
a number of remotely sensed variables captured over the same time-frame.

### _Cholera outbreak data_
* Cholera surveillance (published cholera outbreak data for research purposes (see linked repo and associated manuscript, only outbreak data will be extracted and used for demonstration purposes in this PoC:
  [Cholera outbreaks in sub-Saharan Africa 2010-2019](https://github.com/HopkinsIDD/cholera_outbreaks_ssa),
  see `data/outbreak_data.csv`)

### _Environmental drivers_

Below are a list of potential indicator datasets for inclusion into the Cholera Lab study based on literature support ([Gwenzi & Sanganyado 2019](https://www.mdpi.com/2078-1547/10/1/1); [Lessler et al. 2018](https://www.sciencedirect.com/science/article/pii/S0140673617330507#sec1); [Perez-Saez et al. 2022](https://www.thelancet.com/journals/langlo/article/PIIS2214-109X(22)00007-9/fulltext); [Moore et al. 2017](https://www.pnas.org/doi/10.1073/pnas.1617218114), and others outlined below more specifically below)

- [x] [A review of the risk of cholera outbreaks and urbanization in sub-Saharan Africa](https://www.sciencedirect.com/science/article/pii/S2588933820300261)
* Hydroclimatology 👈 we’ll focus predominantly on these
* Geographic location of urban areas
* Urban environment - sanitation
* Urban behavior
- [x] [The Impact of Climate Change on Cholera: A Review on the Global Status and Future Challenges](https://www.mdpi.com/2073-4433/11/5/449)
* Precipitation/flood = increase in disease potential due to disruption of water systems/Increased spread
* Drought = increased spread
- [x] [The seasonality of cholera in sub-Saharan Africa: a statistical modelling study](https://www.thelancet.com/journals/langlo/article/PIIS2214-109X(22)00007-9/fulltext)
* mean monthly fraction of area flooded
* mean monthly air temperature
* cumulative monthly precipitation
- [x] [Estimating cholera risk from an exploratory analysis of its association with satellite-derived land surface temperatures](https://www.researchgate.net/publication/331555046_Estimating_cholera_risk_from_an_exploratory_analysis_of_its_association_with_satellite-derived_land_surface_temperatures) dataset from which outbreak data was extracted
* Precipitation (anomalies)
* Air temperature (anomalies)
* Land surface temperature
* Findings: shows LST anomalies estimated 2 months in advance of cholera incidence for each pixel in the ﬁve locations, with all regions revealing varying degrees of warm and cold temperature pixels in the analyses

Based on available Indicators for both spatial and temporal extent of our AOI (Sub-Saharan Africa from 2010-2019) we will extract the following environmental parameters for our investigation.

| Variable | Temporal Resolution | Spatial Resolution | Data Availability | Data Source |
|---------- | ------------------- | ------------------ | ------------------| ------------ |
| Land Surface Temperature | monthly | 1.11 km | 1995-2020 | [CEDA](https://catalogue.ceda.ac.uk/uuid/785ef9d3965442669bff899540747e28) |
| Precipitation | monthly | 5 km | 1981- near present | [CHIRPS](https://catalogue.ceda.ac.uk/uuid/785ef9d3965442669bff899540747e28), with multiple access points, including [USCB Storage](https://data.chc.ucsb.edu/products/CHIRPS-2.0/) and [SERVIR GLOBAL](https://climateserv.servirglobal.net/map?data=ucsbchirps) |
| Soil Moisture | daily | 0.25 degrees; approx 27-28 km | 1991-2021 | [ESA Climate Data Dashboard](https://climate.esa.int/en/odp/#/project/soil-moisture)|

To explore the use of machine learning techniques on publicly available,
open-sourced datasets to demonstrate the potential to predict cholera in endemic
regions of the world, which could be developed further as part of a public
health planning and decision making tool for humanitarian organizations.
Develop a PoC based only on open-source data to showcase ML capabilities in this
space which could be developed further to support decision tool development in
this space, and provide more context to cholera patterns than is provided by
cases alone.

## Proposed Methodology

1. _Data collection and spatial exploratory data analysis._ We’ll explore what patterns, over both space and time, can be observed from the cholera outbreaks themselves. We’ll also explore the literature to understand what remotely sensed environmental factors  (e.g., precipitation, temperature) that have been suggested as drivers for disease spread.
1. _Development of pre-processing pipeline for remotely sensed EO data._ We’ll develop a pre-processing pipe-line to ensure our satellite data is assembled and aggregated at the same level (i.e., monthly values for each district) as our outbreak data and ready to be ingested into a ML model.
1. _ML model exploration._  We’ll explore a number of ML approaches (e.g., Random Forest, SVMs,
   etc.) to understand the patterns between cholera outbreaks and the environmental drivers we have identified.
1. _Visualize model results and share findings._ We’ll provide visuals of our model results and share our findings in a collection of Jupyter notebooks.

## Hypothesis

Environmental factors alone won’t unravel this very complex
relationship, but they can help identify spatio-temporal patterns that could
help assist in allocating resources and support.

## Setting up your local environment

### Install Git Large File Storage

This repository contains files larger than 50 MB, and thus requires the use of
Git Large File Storage (LFS) for managing them.  In order to obtain these large
files during repository cloning, you must [install Git Large File Storage].

On macOS, the easiest way to install Git LFS is via Homebrew:

```plain
brew install git-lfs
```

Once installed, initialize it:

```plain
git lfs install
```

To track new types of large files (larger than 50 MB), you must tell Git LFS to
track them, typically by extension.  For example, to track all Shapefiles:

```plain
git lfs track "*.shp"
```

You can then add and commit such files like any other file in the repository.

Note that the `git lfs track` command will modify the `.gitattributes` file when
given a new pattern to track.  When this occurs, be sure to add `.gitattributes`
to your commit, along with the newly tracked large files.

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

[Install Git Large File Storage]:
  https://docs.github.com/en/repositories/working-with-files/managing-large-files/installing-git-large-file-storage
