<p align="center">
  <img src="https://raw.githubusercontent.com/selva221724/dummylog/main/readme_src/dummyloglogo.png"  width="70%" height="70%">
  <br><br>
</p>


**dummylog** is the open source python package to help the python module/plugin developers to create/update the log files in simple syntax and easy format. If you are looking for a single file based log, then dummylog is for you to keep your simple logs

If you are using Flask API or any API decorators with dummylog, it will create a new log every time since decorators will trigger the function as every new instance. 


[<img src="https://img.shields.io/pypi/v/dummylog">](https://pypi.org/project/edaSQL/)
[<img src="https://img.shields.io/static/v1?label=license&message=MIT&color=green">](https://opensource.org/licenses/MIT)
<img src="https://img.shields.io/pypi/wheel/dummylog">
<img src = "https://img.shields.io/pypi/pyversions/dummylog">
<img src = "https://img.shields.io/github/commit-activity/w/selva221724/dummylog">
<img src = "https://img.shields.io/github/languages/code-size/selva221724/dummylog">


## Installation

**Install using pip** . [Offical Python Package Here!!](https://pypi.org/project/dummylog/)
```shell
pip install dummylog
```

(OR)

Clone this Repository. Run this from the root directory to install

```shell
python setup.py install
```

## License
The license for dummylog is MIT license 

## Need help?
Stuck on your dummylog code or problem? Any other questions? Don't
hestitate to send me an email (selva221724@gmail.com).

## Usage

### 1. Import Package
```python
import dummylog
```

### 2. Initialize the dummylog Object
```python
dl = dummylog.DummyLog()

```
#### dummylog.DummyLog() parameters
|S.No |Parameters    | Description | Type | Default Value |
| -------------| ------------- | ------------- | ------------- | ------------- |
|1 | log_name  | Name of the log instance/file  | string  |  datetime.now().strftime('%d_%m_%Y__%H_%M_%S')  |
|2 | logging_level  | [level of logging that user needed](https://docs.python.org/3/library/logging.html#levels)  | string  | "debug"  |
|3 | string_format  | [Formatter for logging](https://docs.python.org/3/library/logging.html#formatter-objects) | string  | "%(asctime)s: %(levelname)s: %(message)s" |
|3 | datetime_format  | Date-time format for logging | string  | "%m/%d/%Y %I:%M:%S %p" |
|4 | log_on_folder  | True if you want to save them in a folder  | bool   | True |
|5 | log_folder_name  | Name of the folder to save the logs | string   | "logs" |

### 3. Enjoy Logging
```python
dl.logger.info('Log File is Created Successfully')

dl.logger.info('Unmayanaa Google Competitors')

dl.logger.error('Vada poche')
```

This will create a log file in the root directory of the python script.

### 4. To Kill the dummylog instance
```python
dl.kill()
```
**Note:** Do not use dummylog in case if you are using the logging module in the same script for other purposes. it will conflict with the logging thread and append things to gather.


### Sample Log File View
<img src="https://raw.githubusercontent.com/selva221724/dummylog/main/readme_src/dummylog.png"  width="100%" height="100%">

## Future Work
- dummylog will be enabled for multithreading
- enhance logging capability
