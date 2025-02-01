# Reading and learning

## Installing Visual Studio Code
* Installed Visual Studio Code using the .deb link on this page: https://code.visualstudio.com/docs/setup/linux

## Installing python and pip
* Read these instructions: https://code.visualstudio.com/docs/python/python-tutorial
   * Running `python get-pip.py` did not work because I think the correct command is `python3`
   * Running `python3 get-pip.py` didn't seem to work either
   * I ran `pip` to see what would happen and the terminal told me to run `apt-get install python-pip` (or something, can't remember the exact name of the package)

## Setting up Visual Studio Code and a virtual environment
* Read these instructions: https://code.visualstudio.com/docs/python/python-tutorial#_install-a-python-interpreter
   * Installed the python extension for VS Code (this installs the debugger extension as well)
   * Created folder **/home/badnumbers/Documents/python-file-script/** and told VS Code to open it
   * Created a virtual environment as per the documentation
** Note that the **.venv** folder is hidden in the file manager unless you tell it to show hidden files
** Selected the virtual environment as per the documentation (it was the first item suggested)
* Created this readme file
* Added **hello.py** and ran it

## Problems with the virtual environment
I found that the virtual environment wasn't working when I tried to use `pip`. It seems that if you try to use `pip` outside of a virtual environment, it wants to install the package globally and then `pip` and `apt` get into a fight.
Also, I found first time that `pip` wouldn't install into the virtual environment because I needed to install the package `python3.12-venv` first.
If you've already created a virtual environment and want to recreate it, do the following from the folder containing this script:
```
# Deactivate the current environment
deactivate

# Remove the existing virtual environment folder
rm -rf .venv

# Create a new virtual environment
python3 -m venv .venv

# Activate the new virtual environment
source .venv/bin/activate

# Install packages again
pip install colorama
```