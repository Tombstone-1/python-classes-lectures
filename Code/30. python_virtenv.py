# Python virtual enviroment
"""
A virtual environment in Python is an isolated environment on your computer, where you can run and test your Python projects.
It allows you to manage project-specific dependencies without interfering with other projects or the original Python installation.

Think of a virtual environment as a separate container for each Python project. Each container:

Has its own Python interpreter
Has its own set of installed packages
Is isolated from other virtual environments
Can have different versions of the same package

"""
# python has the built-in venv module for creating virtual enviroment.
# same for windows/linux/mac

'''
python -m venv myvirtualenviroment
'''
# you can this way make you own virtual enviroment an keep your project seperate from other projects.

# to activate virtual enviroment
# for windows.
'''
myvirtualenviroment\Scripts\activate
'''

# for linux and mac
'''
source myvirtualenviroment/bin/activate
'''

# install packages inside in virtual enviroment
'''
pip install package_name
'''

# for deactivating enviroment.
# for windows
'''
myvirtual\Scripts\deactivate
'''

# for linux/ macos
'''
deactivate
'''








