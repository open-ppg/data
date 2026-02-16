# PPG Datasets

A [catalog of datasets](https://open-ppg.github.io/data/) containing photoplethysmography (PPG) signals.

## Overview

This searchable catalog is designed to help identify PPG datasets for use in research projects. You can filter datasets by:

- **Signals available:** e.g., datasets with both PPG and ECG signals.
- **Data availability:** e.g., whether approval is required for access.
- **Subject characteristics:** e.g., healthy or patient populations.
- **Number of subjects**

A search bar is also provided to find datasets by name or description.

## Usage

Access the tool [here](https://open-ppg.github.io/data/).

## Technical Details

The webpage is generated using `webpage_generator.py`, which:

- Loads dataset information from `datasets.json`
- Loads a template webpage from `template_webpage.html`
- Generates a new webpage containing the dataset information called `index.html`

This process is automated using GitHub Actions, which runs the script whenever changes are made to `datasets.json` or `template_webpage.html`.

## Contributing

If you know of a dataset that is not included in the catalog, please submit a pull request to add it. You can use the existing entries in `datasets.json` as a template for the information to include about each dataset. Please ensure that the information provided is accurate and up-to-date.