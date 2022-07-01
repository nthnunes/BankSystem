#command: python setup.py build

from cx_Freeze import setup, Executable

base = None    

executables = [Executable("main.py", base=base)]

packages = ["idna", "os", "datetime"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Bank System",
    options = options,
    version = "1.0",
    description = 'None',
    executables = executables
)