####FOR MacOS
IMPORTANT: Move the downloaded folder 'purchaseBot' to Desktop
IMPORTANT: IF YOU RUN THE BOT ON A PRODUCT THAT IS CURRENTLY AVAILABLE, THE BOT WILL BUY IT FOR YOU. 
           DO NOT ACCIDENTALLY RUN IT ON A PRODUCT YOU DO NOT WANT TO BUY. 
1. Open the zip file 'chromedriver_mac64.zip'. A new file 'chromedriver' will appear
2. Go and open the file of the bot you want to use (WalmartBot.py, BestBuyBot.py, or GamestopBot.py)
3. Go to the folder 'purchaseBot' and right-click on the chromemanager file (not the zip!) and copy the 
   location of it (copy the 'Where')
4. Find the line of code "driver = webdriver.Chrome('chromedriver')" and replace 'chromedriver' with 
   'the-path-you-just-copied-from-step-3'. Save and close.
5. Go to 'config.py' and replace the fields with information about you. Save and close.
6. Open Terminal (Command + Space then type Terminal)
7. Install homebrew using Terminal: 
    - Type: xcode-select --install (then hit return)
    - Type: curl -fsSL -o install.sh https://raw.githubusercontent.com/Homebrew/install/master/install.sh (then hit return)
    - Type: /bin/bash install.sh (then hit return)
8. Install python3 using Terminal:
    - Type: brew install python3 (then hit return)
9. Install pip3 using Terminal:
    - Type: curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py (then hit return)
10. Install selenium using Terminal:
    - Type: sudo pip3 install selenium (then hit return)
    - NOTE: You will have to enter your computer password for this step. Type then hit return.
11. In Terminal, type: clear
12. In Terminal, type:
    - cd Desktop
    - cd purchaseBot
    - python3 WalmartBot.py/BestBuyBot.py/GamestopBot.py (choose one bot to run right now)
    - For example: python3 WalmartBot.py (this will launch the WalmartBot)
    - THERE WILL BE AN ERROR WHEN YOU DO THIS. THIS IS NECESSARY
    - Open System Preferences --> Security and Privacy --> Unlock the lock --> Click 'Allow anyways' next to the chromedriver error. 
    - Lock the lock and then close System Preferences.
13. That's it! You can download VSCode or any such software, open the .py file of the bot you want to run, and run the code of the bot you want to 
    OR:
    - Close any existing Terminal instance.
    - Open Terminal again then type the next three lines, hitting return after each one.
    - cd Desktop
    - cd purchaseBot
    - python3 WalmartBot.py/BestBuyBot.py/GamestopBot.py (choose one bot to run right now)

USAGE INSTRUCTIONS:

AFTER INSTALLING, you can run/reload the bot whenever you want by following STEP 13. 

Start the bot and keep it running 1-2 minutes before a drop. The reasoning for this is because you want to get
past Captcha as soon as possible. Reloading it many times before a drop will make you run into Captcha and solve it.
It is better to do this before a drop so the site does not make you do it while you are attempting to buy. This will stop 
the bot and you will not be able to buy the product.

If you run into Captcha, solve it then reload the bot. If the page is reloading every time you try to solve it,
open the website in a separate guest window of Chrome and solve the Captcha. Then reload the bot. It will work fine for the
next dozen to 2 dozen page reloads.


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