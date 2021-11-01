# QA Assessment for Automation Engineer role
Link: https://docs.google.com/document/d/1ahXbglt5_O3Ie0D1WqkvhtVbyxVwZGhf_9uqfxf7lfQ/edit

# Contents:
  1. main.py
  2. readme.md
  3. chrome_automation.py
  4. firefox_automation.py
  5. edge_automation.py

# Tools used:
  1. Python
  2. Selenium

# Design Description:
  - The code uses selenium to automate the browser and take event based actions as required in the task.
  - main.py will trigger the corresponding script depending on browser specified. 
  - Each individual <browser>_automation.py script has the same layout and the only change is with regard to browser webdriver and options.
  - All the scripts were running fine locally except for known issues mentioned below.
  - Currently all of it is being implemented using element selection by XPATHs.
  - In case XPATH is changed, corresponding changes need to be included in each of the scripts. This can be improved by making a JSON or XML file listing the XPATHs and keeping it common for the scripts.

# Known Issues:
  - NOTE: sometimes it proceeds in single click at "Usar Nueva Tarjeta" bubble option in selecting card payment screen, sometimes it takes 2 clicks (depending on whether the first click opened the dropdown where we can enter card details or not). In the first case, the script works fine but manually clicking the same element again will close the dropdown and rest of the script will stall until timeout. In the second case script will keep waiting till second click is issued else it will timeout. DEFAULT SETTING IS FOR ONE CLICK, uncomment the respective line(s) for second click if need be.
  - At the end, I was not able to access the successful payment page both manually as well as via automation. REASON - Account is blocked and needs to reset password. So I have printed the same message hard coded at the end.

# Usage:
  Run the following command in Windows environment after going inside the repository.
  
  NOTE: webdriver executable path is optional for all cases, if it is not added to PATH  then you must specify.

```py -3 main.py -b <browser> -x <webdriver_executable_path> -u <username> -p <password> -n <card_number> -m <card_month> -y <card_year> -c <card_cvv> -d <phone_number> -e <test_email>```

# Support:
  For queries and updates feel free to mail me at manan.raheja13@gmail.com

