import os
import sys

"""Utility function to update sys.path so in our notebooks we can import modules from 
any folder in the application"""


def set_path():
    project_path = os.path.abspath("../")
    if project_path not in sys.path:
        sys.path.insert(0, project_path)
    sys.path.append(f'{project_path}/env/lib/python3.7/site-packages')
    print(f'{project_path} has been inserted into sys.path')


set_path()
