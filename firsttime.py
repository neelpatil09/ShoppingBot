import os
import sys

####FOR MacOS remove triple quotes on line 5 and 18
"""
#install homebrew
os.system('xcode-select --install')
os.system('curl -fsSL -o install.sh https://raw.githubusercontent.com/Homebrew/install/master/install.sh')
os.system('/bin/bash install.sh')
os.system('brew doctor')

#install python3
os.system('brew install python3')

#install pip3
os.system('curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py')

#install selenium
os.system('pip3 install selenium')

mac os go to security and privacy --> give permission to chromedriver
"""

####FOR Windows remove triple quotes on line and  
"""
#install chocolatey
os.system('choco install microsoft-windows-terminal --pre ')

#install python3
os.system('choco install python3 --pre ')

#install pip3
os.system('python3 get-pip.py')

#install selenium from tarball (not from pip)
os.system('python3 setup.py install')
"""