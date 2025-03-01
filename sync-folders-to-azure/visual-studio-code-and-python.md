# Visual Studio Code and python

## Installing Visual Studio Code
* Installed Visual Studio Code using the .deb link on this page: https://code.visualstudio.com/docs/setup/linux

## Installing python and pip
* To check if you have python (python 3) installed already:
   * Open a terminal in Visual Studio Code
   * Type `python3` and hit `Enter`
   * If you have python 3 installed, you'll see the prompt `>>>`
* Follow the same procedure to check if you have `pip` installed (from the bare command line, not from python)
* If you need to install stuff, read these instructions: https://code.visualstudio.com/docs/python/python-tutorial
   * The instructions to install `pip` didn't seem to work
   * I ran `pip` to see what would happen and the terminal told me to run `apt-get install python3-pip` (or something, can't remember the exact name of the package)

## Setting up Visual Studio Code
* Read these instructions: https://code.visualstudio.com/docs/python/python-tutorial#_install-a-python-interpreter
  * I installed the following VS Code extensions:
    * **Python** from Microsoft
    *   This installs **Python Debugger** as well
    * **Pylance** from Microsoft
    * **Markdown All in One** from Yu Zhang, for editing this file

## Creating a virtual environment
* Read these instructions: https://code.visualstudio.com/docs/python/python-tutorial#_create-a-virtual-environment
  * Hit `Ctrl`+`Shift`+`P`
  * Choose **Python: Create Environment...**
  * Choose **Venv**
  * Not sure why, but you might get more than one choice of interpreter path. I chose the first one, **Python 3.12.7 /usr/bin/python3**
  * This creates the `.venv` folder within the folder oepned in VS Code
     * Note that the **.venv** folder is hidden in the file manager unless you tell it to show hidden files
  * Selected the virtual environment as per the documentation (it was the first item suggested)
* Created this readme file
* Added **hello.py** and ran it

## Problems with the virtual environment
I found that the virtual environment wasn't working when I tried to use `pip`. It seems that if you try to use `pip` outside of a virtual environment, it wants to install the package globally and then `pip` and `apt` get into a fight.
Also, I found first time that `pip` wouldn't install into the virtual environment because I needed to install the package `python3.12-venv` first.

## Deleting and recreating a virtual environment
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