# Survey Fix

[![Build Status](https://travis-ci.org/kwohlfahrt/survey_fix.svg?branch=master)](https://travis-ci.org/kwohlfahrt/survey_fix)

This tool fixes flat surveys (i.e. points with 0 elevation and a nearby text
label containing the elevation) into 3D points. Inputs and outputs a DXF format
file.

## Installation

The script requires [Python3](https://python.org). It can be installed with:

```
pip install git+https://github.com/kwohlfahrt/survey_fix.git
```
    
## Usage

This program is simple to use from the command-line:

```
survey_fix input.dxf output.dxf
```

If `survey_fix` is not on your `$PATH`, you may get an error that the command is
not found. In that case, the following may work:

```
python3 -m survey_fix input.dxf output.dxf
```
