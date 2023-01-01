# python-delete-cache

Python script to delete temporary file in Windows

## Transform .py to .exe

First of all, you need to install the auto-py-to-exe library

### Installing via [PyPI](https://pypi.org/project/auto-py-to-exe/)

You can install this lib using PyPI:
```shell
$ pip install auto-py-to-exe
```
Then to run it, execute the followin command in the terminal:
```shell
$ auto-py-to-exe
```

### Installing via GitHub

![](https://warehouse-camo.ingress.cmh1.psfhosted.org/0c90ebcf535ccfa430b4cd278698da05e855f69e/68747470733a2f2f6e6974726174696e652e6e65742f706f7374732f6175746f2d70792d746f2d6578652f6175746f2d70792d746f2d6578652d64656d6f2e676966)

```shell
$ git clone https://github.com/brentvollebregt/auto-py-to-exe.git
$ cd auto-py-to-exe
$ python setup.py install
```

Then to run it, execute the following in the terminal:

```shell
$ auto-py-to-exe
```

#### Running Locally Via Github (no install)

You can run this project locally by following these steps:

1. Clone/download the repo
2. Open cmd/terminal and cd into the project
3. Execute `python -m pip install -r requirements.txt`

Now to run the application, execute `python -m auto_py_to_exe`. A Chrome window in app mode will open with the project running inside.

> Make sure you are in the directory below auto_py_to_exe (you will be after step 3) when calling `python -m auto_py_to_exe` or you will need to reference the folder `auto_py_to_exe` absolutely/relatively to where you currently are.

## Start script when Windows startup

1. Press Win + R
2. Type shell:startup
3. Drag and drop your .exe/.py script into the folder

Note: Your explorer must have to open a directory like this: `C:\Users\USER\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup`

> If you do not want the console, just change the file extension from `.py` to `.pyw`
### Please! Execute this python script as an administrator! Otherwise, it will not work properly!
