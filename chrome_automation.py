########################################################
# chrome - Documentation pending                       #
# Author  : Manan Raheja <manan.raheja13@gmail.com>    #
# GitHub  : https://www.github.com/mananraheja         #
# LinkedIn: https://www.linkedin.com/in/mananraheja    #
########################################################

# imports
import os, sys, time
import argparse as ap
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


if __name__ == '__main__':
    parser = ap.ArgumentParser()
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
    EXECUTABLE_PATH    = args.executable
    PAYMENT_USERNAME   = args.username
    PAYMENT_PASSWORD   = args.password
    TRIAL_PHONE_NUMBER = args.phone_number
    CARD_NUMBER        = args.card_number
    CARD_MONTH         = args.card_month
    CARD_DATE          = args.card_year
    CARD_CVV           = args.card_cvv
    TEST_EMAIL         = args.test_email

    # Storing button XPATHs
    xpath_buttons_dict = {
        "RECARGA_CELLULAR_BUTTON_XPATH": r'//*[@id="mainBlueContainer"]/div[1]/a[1]',
        "NUMERO_TEXTBOX_XPATH"         : r'//*[@id="col-sm-12"]/form/div/div[1]/div[1]/div[2]/ul/li[2]',
        "SIGUIENTE_BUTTON_XPATH"       : r'//*[@id="col-sm-12"]/form/div/div[1]/div[1]/div[3]/div/button',
        "USAR_NUEVA_TARJETA_XPATH"     : r'//*[@id="radio-n"]/td/label/a/span',
        "TARJETA_BUTTON_XPATH"         : r'//*[@id="new-card-toggle"]/div/p',
        "AGREGAR_BUTTON_XPATH"         : r'//*[@id="applypromocardsaved"]',
        "PAGAR_CON_TARJETA_XPATH"      : r'//*[@id="paylimit"]/span',
        "CAPTCHA_XPATH"                : r'//*[@id="loginForm"]/div[4]/div/div/iframe',
        "ACCESSO_BUTTON_XPATH"         : r'//*[@id="loginBtn"]'
    }

    # Storing textbox input XPATHs
    xpath_inputs_dict = {
        # "OPERADOR_TEXTBOX_XPATH"        : r'//*[@id="col-sm-12"]/form/div/div[1]/div[1]/div[2]/ul/li[1]/div/div/label', -- not in use
        "NUMERO_DE_CELUAR_INPUT_XPATH"  : r'//*[@id="col-sm-12"]/form/div/div[1]/div[1]/div[2]/ul/li[2]/div/div/input',
        "NUMERO_DE_TARJETA_XPATH"       : r'//*[@id="cardnumberunique"]',
        "MES_MONTH_XPATH"               : r'//*[@id="payment-form"]/div[3]/div[1]/div/div[1]/input',
        "ANO_YEAR_XPATH"                : r'//*[@id="payment-form"]/div[3]/div[1]/div/div[3]/input',
        "CVV_XPATH"                     : r'//*[@id="payment-form"]/div[3]/div[2]/div/input',
        "CORREO_ELECTRONICO_EMAIL_XPATH": r'//*[@id="payment-form"]/div[4]/div/div/input',
        "PAYMENT_EMAIL_XPATH"           : r'//*[@id="usrname"]',
        "PAYMENT_PASSWORD_XPATH"        : r'//*[@id="psw"]',
        "MONTO_DE_RECARGA_XPATH"        : r'//*[@id="col-sm-12"]/form/div/div[1]/div[1]/div[2]/ul/li[3]/div/div/input'
    }


    # Storing misc XPATHs
    xpath_misc_dict = {
        "RECARGA_CELLULAR_DROPDOWN_LIST_XPATH": r'//*[@id="col-sm-12"]/form/div/div[1]/div[1]/div[2]/ul/li[1]',
        "TELCEL_XPATH"                        : r'//*[@id="col-sm-12"]/form/div/div[1]/div[1]/div[2]/ul/li[1]/div/div/div/ul/li[1]/a/div/b',
        "TRIAL_AMOUNT_XPATH"                  : r'//*[@id="col-sm-12"]/form/div/div[1]/div[1]/div[2]/ul/li[3]/div/div/div/ul[1]/li[1]/a/div[1]/b'
    }

    # selecting webdriver based on browser
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])  # to remove logging error messages in stdout

    if EXECUTABLE_PATH != None:
        browser = webdriver.Chrome(executable_path=EXECUTABLE_PATH, options=options)
    else:
        browser = webdriver.Chrome(options=options)

    # base_url
    BASE_URL = "https://prueba.undostres.com.mx/"
    
    # Loading the Base URL using 
    browser.get(BASE_URL)

    # print page title
    page_title = browser.title
    print("page title = " + str(page_title))

    # STEP 1 - Click on Recarga Celular

    print("clicking recarga_cellular button")
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_buttons_dict["RECARGA_CELLULAR_BUTTON_XPATH"]))).click()

    print("printing elements in recarga_cellular list")

    # opening dropdown list to select TELCEL
    dropdown_items = browser.find_elements_by_xpath(xpath_misc_dict["RECARGA_CELLULAR_DROPDOWN_LIST_XPATH"])
    for item in dropdown_items:
        i_text = item.text
        print(i_text + " " + str(len(i_text)))
        if i_text == 'Operador':
            print("Clicking on Operador textbox")
            item.click()
            print("clicking Telcel button")
            WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_misc_dict["TELCEL_XPATH"]))).click()


    # STEP 2 - Clicking on Número de celular (10 dígitos)
    
    dropdown_items = browser.find_elements_by_xpath(xpath_buttons_dict["NUMERO_TEXTBOX_XPATH"])
    for item in dropdown_items:
        i_text = item.text
        print(i_text + " " + str(len(i_text)))
        if i_text == 'Número de celular (10 dígitos)':
            print("Clicking on Número de celular (10 dígitos) textbox")
            item.click()
            WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_inputs_dict["NUMERO_DE_CELUAR_INPUT_XPATH"]))).send_keys(TRIAL_PHONE_NUMBER)

    # STEP 3 - Clicking on Monto de Recarga
    
    print("Selecting 10$ recharge amount")
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_inputs_dict["MONTO_DE_RECARGA_XPATH"]))).click()
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_misc_dict["TRIAL_AMOUNT_XPATH"]))).click()

    # STEP 4 - Clicking submit button
    
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_buttons_dict["SIGUIENTE_BUTTON_XPATH"]))).click()

    # STEP 5 - Clicking Tarjeta button
    
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_buttons_dict["TARJETA_BUTTON_XPATH"]))).click()

    # STEP 6 - Clicking Usar Nueva Tarjeta button
    
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_buttons_dict["USAR_NUEVA_TARJETA_XPATH"]))).click()
    time.sleep(5)
    # WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_buttons_dict["USAR_NUEVA_TARJETA_XPATH"]))).click()  # need to click it 2 times sometimes...

    # STEP 7 - Enter the card details
    
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_inputs_dict["NUMERO_DE_TARJETA_XPATH"]))).send_keys(CARD_NUMBER)
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_inputs_dict["MES_MONTH_XPATH"]))).send_keys(CARD_MONTH)
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_inputs_dict["ANO_YEAR_XPATH"]))).send_keys(CARD_DATE)
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_inputs_dict["CVV_XPATH"]))).send_keys(CARD_CVV)
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_inputs_dict["CORREO_ELECTRONICO_EMAIL_XPATH"]))).send_keys(TEST_EMAIL)

    # STEP 8 - Click Pagar con tarjeta button
    
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_buttons_dict["PAGAR_CON_TARJETA_XPATH"]))).click()

    # STEP 9 - Enter email ID and password and Captcha and Accesso button
    
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_inputs_dict["PAYMENT_EMAIL_XPATH"]))).send_keys(PAYMENT_USERNAME)
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_inputs_dict["PAYMENT_PASSWORD_XPATH"]))).send_keys(PAYMENT_PASSWORD)

    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_buttons_dict["CAPTCHA_XPATH"]))).click()
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH, xpath_buttons_dict["ACCESSO_BUTTON_XPATH"]))).click()

    # STEP 10 - Check for successful payment webpage
    
    # unable to access this page as the account was blocked. ERROR - User account has been blocked, need to reset credentials
    print("Submitted details successfully, but cannot proceed to successful payment as user account is blocked.")
    print("ERROR: Tu cuenta ha sido bloqueada por favor restablece tu contraseña.")

    # Close the script 
    browser.quit()
    print("Script ran successfully.")
    exit(0)

    '''
    sample run command: (windows environment)
    py -3 chrome_automation.py -x <webdriver_executable_path> -u <username> -p <password> -n <card_number> -m <card_month> -y <card_year> -c <card_cvv> -d <phone_number> -e <test_email>
    '''
