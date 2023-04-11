# geospatial-ds-cholera-lab
A repo dedicated to developing a geospatial data science prototype (see issue: https://github.com/developmentseed/labs/issues/292) 


**The objective**:
To explore the use of machine learning techniques on publicly available, open-sourced datasets to demonstrate the potential to predict cholera in endemic regions of the world, which could be developed further as part of a public health planning and decision making tool for humanitarian organizations. Develop a PoC based only on open-source data to showcase ML capabilities in this space which could be developed further to support decision tool development in this space, and provide more context to cholera patterns than is provided by cases alone.


**Literature support**:
In cholera endemic countries, there is [support of environmental signatures between seasonal outbreaks](https://www.pnas.org/doi/10.1073/pnas.0809654105) which could be explored and used to develop a framework for an early warning system. See also [this paper](https://www.thelancet.com/journals/langlo/article/PIIS2214-109X(22)00007-9/fulltext), for supporting work in this area.


**The challenge**:
* [Cholera](https://www.who.int/news-room/fact-sheets/detail/cholera?gclid=Cj0KCQjw8e-gBhD0ARIsAJiDsaWCrF6A6O7Idtd3X_gOJe1UIYHA-V8Gp2SAtbYTKy6Jwe_UJ9CYUM0aAmToEALw_wcB) can be both endemic (where seasonal patterns are more likely) and epidemic (based on a perfect storm of conditions). Environmental factors are just one component, there are a number of complex factors at play (e.g., human development indices, access to basic hand-washing, natural disasters, etc.)
* Surveillance isn’t perfect, many areas across the globe have varying levels/resources allocated to disease surveillance (as we’ve seen with Covid) so reported cases aren’t always representative of the true picture.

**Proposed open-source, available datasets**: (_WiP_) Focus on an area where endemic cholera is a major issue, and where subnational and sub annual surveillance data is available: _Sub-Saharan Africa_. Data availability during this time frame will also allow us to take advantage of a number of remotely sensed variables captured over the same time-frame.

* cholera surveillance ([initial dataset proposed for PoC: Cholera outbreaks in sub-Saharan Africa 2010-2019](https://github.com/HopkinsIDD/cholera_outbreaks_ssa), see `data/outbreak_data.csv`)
* sea level (source: [ESA Climate Data Dashboard](https://climate.esa.int/en/odp/#/dashboard))
* sea surface temperate (source: [ESA Climate Data Dashboard](https://climate.esa.int/en/odp/#/dashboard))
* gridded rainfall data (source: [global summary of monthly meteorological data from NOAA](https://www.ncdc.noaa.gov/cdo-web/datasets))
* gridded air temperature data (source: [global summary of monthly meteorological data from NOAA](https://www.ncdc.noaa.gov/cdo-web/datasets))
* world population data (source: [WorldPop](https://www.worldpop.org/))
* human development indices (source: [INFORM indices](https://drmkc.jrc.ec.europa.eu/inform-index), [Human Development Reports/data](https://hdr.undp.org/data-center/human-development-index#/indicies/HDI))

**Proposed methodology**:
1. Exploratory spatial data analysis (what patterns can be observed from the cholera cases themselves?)
2. Principal component analysis (or similar) to explore correlative indices and narrow down list of covariate factors entered into the model
3. Exploration of machine learning model approaches (e.g., Random Forest, SVMs, etc) to develop a model between cholera cases, environmental and socio-economic factors
4. Provide visuals of model results

_all to be shared, initially, in a series of Jupyter notebooks_

**Hypothesis**:
Environmental and socio-economic factors alone won’t unravel this very complex relationship, but they can help identify spatio-temporal patterns that could help assist in allocating resources and support.


