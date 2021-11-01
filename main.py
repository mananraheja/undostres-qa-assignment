########################################################
# main - Documentation pending                         #
# Author  : Manan Raheja <manan.raheja13@gmail.com>    #
# GitHub  : https://www.github.com/mananraheja         #
# LinkedIn: https://www.linkedin.com/in/mananraheja    #
########################################################

# imports
import argparse as ap
import os, sys


# Driver program
if __name__ == '__main__':
    parser = ap.ArgumentParser()
    parser.add_argument('-b', '--browser', help="Enter the browser name", choices=["chrome", "firefox", "edge"], required=True)    # -- add more browser options here as needed
    parser.add_argument('-x', '--executable', help="Enter the webdriver executable path")
    parser.add_argument('-u', '--username', help="Enter the username", required=True)
    parser.add_argument('-p', '--password', help="Enter the password", required=True)
    parser.add_argument('-n', '--card_number', help="Enter the card number", required=True)
    parser.add_argument('-m', '--card_month', help="Enter the card expiry month", required=True)
    parser.add_argument('-y', '--card_year', help="Enter the card expiry year", required=True)
    parser.add_argument('-c', '--card_cvv', help="Enter the card CVV", required=True)
    parser.add_argument('-d', '--phone_number', help="Enter the phone number", required=True)
    parser.add_argument('-e', '--test_email', help="Enter the test email", required=True)
    args = parser.parse_args()

    # assign the inputs to corresponding labels
    BROWSER            = args.browser
    EXECUTABLE_PATH    = args.executable
    PAYMENT_USERNAME   = args.username
    PAYMENT_PASSWORD   = args.password
    TRIAL_PHONE_NUMBER = args.phone_number
    CARD_NUMBER        = args.card_number
    CARD_MONTH         = args.card_month
    CARD_DATE          = args.card_year
    CARD_CVV           = args.card_cvv
    TEST_EMAIL         = args.test_email

    # common suffix string
    if EXECUTABLE_PATH != None:
        suffix_string = '-x {executable} -u {username} -p {password} -n {card_number} -m {card_month} -y {card_year} -c {card_cvv} -d {phone_number} -e {test_email}'.format(
            executable=EXECUTABLE_PATH,
            username=PAYMENT_USERNAME,
            password=PAYMENT_PASSWORD,
            card_number=CARD_NUMBER,
            card_month=CARD_MONTH,
            card_year=CARD_DATE,
            card_cvv=CARD_CVV,
            phone_number=TRIAL_PHONE_NUMBER,
            test_email=TEST_EMAIL
        )
    else:
        suffix_string = '-u {username} -p {password} -n {card_number} -m {card_month} -y {card_year} -c {card_cvv} -d {phone_number} -e {test_email}'.format(
            username=PAYMENT_USERNAME,
            password=PAYMENT_PASSWORD,
            card_number=CARD_NUMBER,
            card_month=CARD_MONTH,
            card_year=CARD_DATE,
            card_cvv=CARD_CVV,
            phone_number=TRIAL_PHONE_NUMBER,
            test_email=TEST_EMAIL
        )

    # commands based on browser chosen
    commands_dict = {
        "chrome" : r'py -3 chrome_automation.py '  + suffix_string,
        "firefox": r'py -3 firefox_automation.py ' + suffix_string,
        "edge"   : r'py -3 edge_automation.py '    + suffix_string
    }

    # call the corresponding python script
    print("invoking " + BROWSER + " corresponding script: ")
    os.system(commands_dict[BROWSER])

    exit(0)

    '''
    sample run command: (windows environment)
    py -3 main.py -b <browser> -x <webdriver_executable_path> -u <username> -p <password> -n <card_number> -m <card_month> -y <card_year> -c <card_cvv> -d <phone_number> -e <test_email>
    '''