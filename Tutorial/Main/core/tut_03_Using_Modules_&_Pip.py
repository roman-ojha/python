""" 
NOTE :: donote make a python project name as the modules name of the python

Module – Module or library is a file that contains definitions of several functions, classes, variables, etc. which is written by someone else for us to use.

Pip – Pip is a package manager for Python i.e., pip command can be used to download any external module in Python. It is something that helps us to get code written by someone else from somewhere.

We can install a module in our system by using pip command :

Open cmd or Powershell in your system.
And then, type pip install module_name and press enter.
Once you do that, the module will start downloading and will install automatically on your computer.
Example, for installing flask I will do this:
-> pip install flask
After pressing the enter key, flask module will going to install

After installing any module in Python, you can import it into your program or your Python projects. For example, to use flask, I will type "import flask" at the top of my Python program.
-> import flask

*) There are two types of modules in Python:
1)Built-in Modules:

    Built-in modules are the modules that are pre-installed in Python i.e., there is no need to download them before using. These modules come with python interpreter itself.
    Example – random, os, etc.
    To get a complete list of built-in modules of python head to the following page of the official documentation - https://docs.python.org/3/py-modindex.html.

2)External Modules:
    These are the modules that are not pre-installed in Python i.e., we need to download them before using them in our program.

    Example – Flask, Pandas, TensorFlow, etc.

-> pip list 
    -> to get all module install in the environment
 """
