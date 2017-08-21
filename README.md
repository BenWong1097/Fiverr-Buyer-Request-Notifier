# Fiverr Buyer Request Notifier
- __Background__: Fiverr is a popular platform that gives freelancers an easy method to communicate and broadcast their skills to customers.
- __Problem__: Fiverr does not provide real time notifcations to sellers when a potential buyer puts up an offer.
- __Solution__: The script checks at set intervals for new buyer requests and notifies the user when a new one is made available.
## Getting Started
### Prerequisites
- [Python 3](https://www.python.org/downloads/)
  - Modules required:
    - unittest
    - selenium
    - configparser
  - [More on modules and installing them](https://docs.python.org/2/tutorial/modules.html)
- [Selenium Chrome Webdriver](https://sites.google.com/a/chromium.org/chromedriver/)
  - Make sure that the Google Chrome Browser is installed as well!
### Configuration
- Locate the file named "config.ini"
- Open it in a text editor and fill up/alter the settings to your preferences
- Save the file and make sure that "config.ini" is in the same directory as "notification.py" at all times
### Running the Program
- Open the Command Prompt (cmd.exe)
- Type in "python PATH_TO_SCRIPT"
  - _Replace PATH_TO_SCRIPT with the path to notification.py (EX: C:\Users\notification.py)_
- The script should now be running and stop and emit a tone when a new request is posted
## Built with
- Python
- Selenium Webdriver
## License
This project is under the [MIT License](../../LICENSE.md)
