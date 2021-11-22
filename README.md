<p align="center">
  <img src="https://raw.githubusercontent.com/selva221724/dummylog/main/readme_src/dummyloglogo.png"  width="70%" height="70%">
  <br><br>
</p>


dummy long is the open source python package to help the python module/plugin developers to create/update the log files in simple syntax and easy convenient format


<!---[<img src="https://img.shields.io/pypi/v/edaSQL">](https://pypi.org/project/edaSQL/)
[<img src="https://img.shields.io/readthedocs/edasql">](https://edasql.readthedocs.io/en/latest/)
[<img src="https://img.shields.io/static/v1?label=license&message=MIT&color=green">](https://opensource.org/licenses/MIT)
<img src="https://img.shields.io/pypi/wheel/edaSQL">
<img src = "https://img.shields.io/pypi/pyversions/edaSQL">
<img src = "https://img.shields.io/github/commit-activity/w/selva221724/edaSQL">
<img src = "https://img.shields.io/github/languages/code-size/selva221724/edaSQL">--->


## Installation

**Install using pip** . [Offical Python Package Here!!](https://pypi.org/project/pypostalwin/)
```shell
pip install dummylog
```

(OR)

Clone this Repository. Run this from the root directory to install

```shell
python setup.py install
```

## Documentation

<img src="https://blog.readthedocs.com/_static/logo-opengraph.png"  width="20%" height="20%">

[Read the detailed documentation in readthedocs.io](https://pypostalwin.readthedocs.io/en/latest/)

## License
The license for dummylog is MIT license 

## Need help?
Stuck on your edaSQL code or problem? Any other questions? Don't
hestitate to send me an email (selva221724@gmail.com).

## Usage

### Import Package
```python
import dummylog
```

### 1. Initialize the Address Parser Object
```python
parser = pypostalwin.AddressParser()
parser.runParser("The White House 1600 Pennsylvania Avenue NW, Washington, DC 20500, USA")
```

<img src="https://raw.githubusercontent.com/selva221724/edaSQL/main/readme_src/notebook_results/db_connected.png">

### 2. Terminate the Address Parser Object
```python
parser.terminateParser()
```

