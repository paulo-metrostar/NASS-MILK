# Let's upgrade the visualizations found in the following milk report
- https://downloads.usda.library.cornell.edu/usda-esmis/files/h989r321c/wh247f512/tq57pd47k/mkpr0820.pdf
    - consulted 9/10/2020, 1:45 pm EST

**For now we won't worry about the information described in the text. We'll just focus on the visualizations**

## Monthly Milk Production - 24 Selected States
![Monthly Milk Production 24 Selected States](pictures/monthly-milk-prod-24-states.png)

## Table of Contents
- **data/** 
    - directory containing csv downloads from QS UI
- **pictures/** 
    - directory containing screenshots used in notebooks
- **visualizations/** 
    - directory containing various visualizations produced during notebook work
- **data-mart-tech-specs/** 
    - directory containing objects defining the technical specifications and requirements for the data mart serving the milk report defined above
- **sentinel-nulls.json** 
    - reference showing which non-null values are being used to indicate null values (i.e. sentinel-nulls) for each respective data field (i.e. column header)
- **environment.yml** 
    - defines what is supposed to be a platform-agnostic python package requirements file.
    - python packages are being managed with conda
        - get help installing conda: https://docs.conda.io/projects/conda/en/latest/user-guide/install/
    - Create an environment from the `environment.yml`file: `conda env create -f environment.yml`
    - Activate the new environment: `conda activate nass-milk`
    - Deactivate the environment by activating your base environment: `conda activate`
- **1.0-EDA.ipynb** 
    - Exploratory data analysis
    - document data set download from quick stats (QS)
    - read data into pandas
    - **declutter data**
        - drop empty cols
        - **extract meta-data**
            - move non-varying columns into a metadata object
            - init null-sentinel handling
    - **split data by periodicity**
        - monthly
        - quarterly
        - annaul
    - validate data types
    - initial visualizations
- **2.0-define-upgraded-vis.ipynb** 
    - Streamline and generalize data tidying and visualizing
    - get data from a qs UI download
    - specify pre-processing workflow to arrive at tidy-data requirements for data-mart
        - meta-data
        - tidy-data
        - data-dictionary
    - output plot objects in json, html, and png