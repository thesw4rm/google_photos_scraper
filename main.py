from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

username = 'EXAMPLE_USERNAME'
password = 'EXAMPLE_PASS'
driver = '../Driver/chromedriver.exe'  # See Selenium docs for different drivers
album_contains = 'Shared' #Some unique part of the album's name

os.environ["webdriver.chrome.driver"] = driver

options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")

driver = webdriver.Chrome(driver,
                          chrome_options=options)
driver.get(
    "https://accounts.google.com/ServiceLogin?passive=1209600&osid=1&continue=https://photos.google.com/login&followup=https://photos.google.com/login#identifier")

try:
    driver.execute_script("""document.getElementById('Email').value = '""" + email + """';$("#next").click();
                setTimeout(function(){document.getElementById('Passwd').value = '""" + password + """';$("#signIn").click();},2000);""");  # setTimeout does same thing as Python's time.sleep
    time.sleep(2);  # Set time.sleep to higher or lower levels depending on Internet connection.
    driver.execute_script("""setTimeout(function(){
            document.querySelector('a[href=\"./albums\"]').click();
         },1000);""")
    time.sleep(4)
    driver.execute_script("""setTimeout(function(){
                document.querySelector('.FmgwTd').parentNode.parentNode.click()
             },1000);""")
    time.sleep(2)
    driver.execute_script("""setTimeout(function(){
                   document.querySelector('.RY3tic').parentNode.click();},2000);""")
    time.sleep(4)
    driver.execute_script("""setTimeout(function(){
                       document.querySelector('div[aria-label=\""""+album_contains+"""\"]').click()},2000);""")

    driver.execute_script("""setTimeout(function(){
                           document.querySelector('div.f6nBjd').click()},2000);""")
    time.sleep(2)
    while 1 == 1:
        driver.execute_script("""setTimeout(function () {
                    var link = document.querySelector('img[jsname="uLHQEd"]').src;

                    setTimeout(function () {
                        var mywindow = window.open('http://localhost:45118/test?thing=' + link, '_blank', 'location=yes,height=570,width=520,scrollbars=yes,status=yes');
                    }, 2000);

                    setTimeout(function () {
                        mywindow.close();
                    }, 4000);
                    document.querySelector(\'[aria-label=\"View next photo\"]\').click();

                });""")  # At this point, I built a tiny PHP server that takes a get Request and writes it to a file. Since we are moving through a carousel, if it sees a duplicate, it will end all Python programs. Please change this URL to your own solution.

        time.sleep(1)

    input("close?")
    driver.close()
except Exception as e1:
    raise e1
    input("close?")
    driver.close() #closes from the prompt because I kept forgetting to close the driver.
