# PPG Datasets

A catalog of datasets containing photoplethysmography (PPG) signals.

## Overview

This searchable catalog is designed to help identify PPG datasets for use in research projects. You can filter datasets by:

- **Signals available:** e.g., datasets with both PPG and ECG signals.
- **Data availability:** e.g., whether approval is required for access.
- **Subject characteristics:** e.g., healthy or patient populations.
- **Minimum number of subjects.**

A search bar is also provided to find datasets by name or description.

## Status

The catalog currently contains dummy data with known errors and requires updates to include more datasets.

## Usage

Access the tool [here](#).

## Technical Details

The webpage is generated using `webpage_generator.py`, which:

- Loads dataset information from `datasets.json`
- Loads a template webpage from `template_webpage.html`
- Generates a new webpage containing the dataset information called `ppg_datasets.html`