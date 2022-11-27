import subprocess
import os

def get_current_environment():
    return os.environ.copy()  //return 'dict'

def update_environment(keyName, newValue, env):
    env[keyName] = newValue

def update_path_for_Python(env_lst, newValue):
    paths_for_python = filter(lambda c: c.find('python') > -1, for c in env_lst)
    return list(paths_for_python)
