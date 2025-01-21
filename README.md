# FITS Response Matrix Reader

This Python script reads and processes a FITS response file to extract and desparsify the response matrix along with energy bounds and channel information.

## Features

- Reads energy bounds and channel information from a FITS file.
- Desparsifies the response matrix from compressed data format.
- Handles common errors such as file not found, missing extensions, or invalid indices.

## Requirements

To run this script, you need the following Python packages installed:

- `numpy`
- `astropy`

You can install them using pip:

```bash
pip install numpy astropy
