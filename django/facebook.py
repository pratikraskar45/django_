import selenium
import time
from selenium import webdriver


def Connecting_To_Browser(id_str, pass_str):
    if id_str != "" and pass_str != "":
        browser = webdriver.Chrome("chromedriver.exe")
        try:
            browser.get('https://www.facebook.com')

            email_field = browser.find_element_by_id("email")
            email_field.clear()
            for i in id_str:
                email_field.send_keys(i)
                time.sleep(0.05)

            password_field = browser.find_element_by_name("pass")
            password_field.clear()
            for p in pass_str:
                password_field.send_keys(p)
                time.sleep(0.05)

            time.sleep(0.5)

            password_next_button = browser.find_element_by_name("login")
            password_next_button.click()

            time.sleep(10)
            browser.quit()
        except:
            browser.quit()

    else:
        print("Either ID or PASSWORD is null")


Connecting_To_Browser("<Your Email ID/Number>", "<Your Password>")