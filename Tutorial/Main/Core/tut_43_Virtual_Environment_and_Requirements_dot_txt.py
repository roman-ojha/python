"""
 What virtual environment does?
Virtual Environment saves the current state of our compiler along with the state of their modules and libraries. So in this way even if Python has made certain changes in its module, our virtual environment can still work as before even after years. We can also install different packages and “dataframes” in our virtual environment.

To be more clear, the virtual environment works exactly the same way as the Python we have installed on our windows/mac/Linux currently because a virtual environment is just a clone of the original product. 

    -> You can install vertual environment for the folder by opening folder in terminal and:
        -> pip install virtualenv

    -> to make a virtualenv folder:
        -> virtualenv <folder_Name> == this don't work for my pc so i will write:
            -> python -m virtualenv . (. for to install it in that root folder 
            -> python -m virtualenv <folder_name>

    -> now to activate the virtual environment you have to write this:
            -> .\Environment\Scripts\activate

    -> if you are getting an error then you can set-executionpolicy by opening powershell by admin and write:
            -> set-executionpolicy remotesigned

    -> to comeout from that virtual environment you have to wirte:
            -> deactivate
    -> if you want to install module by going to the environment directory and wirte:
        -> pip install <module_name>
            -> like: pip install sklearn

    -> and you can run the python inside the virtual environment as well
        -> python
    
    -> to uninstall the module then you have to write:
        -> pip uninstall sklearn

    -> if you want to know about all the module that you have install in the environment that you have to get requirements.txt by:
        -> pip freeze > requirements.txt

    NOTE: we have to run this inside the virtual environment

    -> if you want to install the spacific version of the module then you have to write:
        -> pip install <module_name>==<version>
        -> pip install flask==2.0.1

    -> to install all the module inside the requirement.txt then you can write:
        -> pip install -r requirements.txt (in the project folder)

    -> if you want to install the virtual environment and want to take all the module from the system of want the python install in the system then you can write:
        -> virtualenv --system-site-packages textEnvironment ( i don't know this is not working in my pc)
        -> python -m virtualenv --system-site-packages <environment_name>
"""
