## Compiling/Running Program
>Our program checks for files under the "data" folder
* if testing all files: ```make```
* if testing with a specific file: ```make file```
    * should prompt for file name, provide just the name without any path or file extension.
    * e. ```pitch_005130```

## Compiling/Running PyTest
1. ```python3 -m venv venv```
    * run this command only once to create virtual environment
2. ```source ./venv/bin/activate```
    * to activate the virtual environment
3. ```pip install -r requirements.txt```
    * to install any dependencies
4. ```make test```
    * should prompt for test name
    * e. ```handler```, ```parser```, ```vector```
5. ```deactivate```
    * to deactivate the virtual environment
