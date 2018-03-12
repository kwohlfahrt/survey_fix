# Survey Fix

[![Build Status](https://travis-ci.org/kwohlfahrt/survey_fix.svg?branch=master)](https://travis-ci.org/kwohlfahrt/survey_fix)
[![codecov](https://codecov.io/gh/kwohlfahrt/survey_fix/branch/master/graph/badge.svg)](https://codecov.io/gh/kwohlfahrt/survey_fix)

This tool fixes flat surveys (i.e. points with 0 elevation and a nearby text
label containing the elevation) into 3D points. Inputs and outputs a DXF format
file.

## Installation

The script can be installed with [pip](https://pip.pypa.io/en/stable/):

```
pip install git+https://github.com/kwohlfahrt/survey_fix.git
```

### Dependencies

[Python](https://python.org) 3.6 or newer is required. Other dependencies are
`ezdxf` and `click` - these will be automatically installed if pip is used as
shown above.

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

### Limitations

The tool supports two kinds of labelled points:

- POINT entities with a nearby text label
- INSERT entities named 'X', located at their insertion point
