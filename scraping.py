## Importing Libraries

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from bs4 import BeautifulSoup
import os
import requests
import pandas as pd
import urllib.request
import streamlit as st
from PIL import Image
import numpy as np

# create object for chrome options
chrome_options = Options()
chrome_options.add_argument('disable-notifications')
chrome_options.add_argument('--disable-infobars')
chrome_options.add_argument('start-maximized')
# To disable the message, "Chrome is being controlled by automated test software"
chrome_options.add_argument("disable-infobars")
# Pass the argument 1 to allow and 2 to block
chrome_options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
    })
####################    Streamlit  ####################
st.set_page_config(layout="wide")

st.sidebar.title("Choose Parameters")

config_select_ecommerce = st.sidebar.multiselect("Select one or more ecommerce for price comparison:", ["All", "Shopee Mall", "LazMall"])

if "All" in config_select_ecommerce:
        config_select_ecommerce = ["Shopee Mall", "LazMall"]

config_search_method = st.sidebar.radio("Select search method:", ["By name of the item","By url"], 0)

if config_search_method == "By name of the item":
    config_input_value = st.sidebar.text_input("Please type in the item you want to do a price comparison", "Tineco")
else:
    for ecommerce in config_select_ecommerce:
        if "Shopee" in ecommerce:
            config_url_shopee = st.sidebar.text_input("Please type in the url for Shopee Mall")
        if "LazMall" in ecommerce:
            config_url_lazmall = st.sidebar.text_input("Please type in the url for LazMall")


####################    Actual code     ####################
def load_image(img):
    im = Image.open(img)
    image = np.array(im)
    return image

st.image(load_image(os.getcwd()+"\Streamlit.jpg"))

def main():
    # Progress
    #Set up progress bar
    st.sidebar.write("-----")
    st.sidebar.subheader("Status")

    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    #chart = st.line_chart(np.random.randn(10, 2))

    status_text.text("In progress... Please Wait.")

    # Invoke the webdriver
    driver = webdriver.Chrome(executable_path = r'C:\Users\desmo\Desktop\Python\Projects\scrape\chromedriver.exe',options = chrome_options)
    delay = 5 #secods
    driver.set_window_position(-10000,0)

    status_text.text("Selenium driver ready. ")

    ####################    Set up table to contain the results      ####################
    col = st.beta_columns(len(config_select_ecommerce)+1)

    #col[i].subheader("Platform")
    col[0].text("")
    col[0].text("")
    col[0].text("")
    col[0].text("")
    col[0].text("")
    col[0].text("")
    col[0].text("")
    col[0].text("")
    col[0].text("")
    col[0].text("")
    col[0].text("")
    col[0].text("")
    col[0].text("")
    col[0].text("")
    col[0].text("")
    col[0].text("")
    col[0].text("")
    col[0].text("")
    #col[i].subheader("Image")
    col[0].subheader("Item")
    col[0].subheader("Price")
    col[0].subheader("Delivery Fee")
    col[0].subheader("Total Price")
    col[0].subheader("Link")

    ####################    Shopee      ####################
    for i in range(len(config_select_ecommerce)):  #Doing this so I can get the index for progress bar

        if "Shopee" in config_select_ecommerce[i]:
            status_text.text("Scraping Shopee Mall now")
            # Shopee Input
            if config_search_method == "By name of the item":
                Input_value=config_input_value
                Input_value_corrected = Input_value.replace(" ","%20")
                shopee_mall_url = "https://shopee.sg/mall/search?keyword="+Input_value_corrected
            else:
                shopee_mall_url = config_url_shopee

            driver.get(shopee_mall_url)

            # List to append scrape results
            shopee_delivery = []
            shopee_price = []
            shopee_itemname = []
            shopee_img = []

            iterate = True
            while iterate:
                try:
                    WebDriverWait(driver, delay)
                    print ("Page is ready")
                    if config_search_method == "By name of the item":
                        sleep(10)
                        shopee_img.append(driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[2]/div/div[2]/div[1]/a/div/div/div[1]/img").get_attribute("src"))
                        driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[2]/div/div[2]/div[1]/a").click()
                    sleep(10)


                    html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
                    #print(html)
                    soup = BeautifulSoup(html, "html.parser")
                    for item in soup.find_all('div', class_='flex items-center deQMhv'):
                        shopee_delivery.append(item.text)
                    for item in soup.find_all('div', class_='attM6y'):
                        if len(item.text) > 90:
                            shopee_itemname.append(item.text[:50] + '..')
                        else:
                            shopee_itemname.append(item.text)
                    for item in soup.find_all('div', class_='_3e_UQT'):
                        shopee_price.append(item.text)

                    if config_search_method == "By url":
                        before_url_shopee = "%20".join("".join(config_url_shopee.split("/-")[1:]).split("-")[:-1])
                        st.write(before_url_shopee)
                        driver.get("https://shopee.sg/mall/search?keyword="+before_url_shopee)
                        sleep(10)
                        shopee_img.append(driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div/div[2]/div/div[2]/div[1]/a/div/div/div[1]/img").get_attribute("src"))
                    iterate = False
                except TimeoutException:
                    print ("Loading took too much time!-Try again")
                    iterate = False

            status_text.text("Printing output from Shopee Mall now...")

            col[i+1].image(load_image(os.getcwd()+"\Image\shopee_mall.png"),width = 200)
            col[i+1].image(shopee_img[0],width=200)
            col[i+1].write(str(shopee_itemname[0]))
            col[i+1].write(str(shopee_price[0]))
            col[i+1].write(str(shopee_delivery[0]))
            col[i+1].write(f"${format(float(shopee_price[0].replace('$','')) + float(shopee_delivery[0].replace('$','')),'.2f')}")
            col[i+1].write(shopee_mall_url, unsafe_allow_html=True)

            progress_bar.progress((i+1)*(1/(len(config_select_ecommerce))))

        if "LazMall" in config_select_ecommerce[i]:
            status_text.text("Scraping LazMall now")
            # Lazmalle Input
            if config_search_method == "By name of the item":
                Input_value=config_input_value
                Input_value_corrected = Input_value.replace(" ","%20")
                lazmall_url = "https://www.lazada.sg/catalog/?from=input&q="+Input_value_corrected+"&service=OS"
            else:
                lazmall_url = config_url_lazmall

            driver.get(lazmall_url)
            sleep(10)
            try:
                slider = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[1]/div[2]/center/div[1]/div/div[1]/div[2]')
                ActionChains(driver).drag_and_drop_by_offset(slider, 400, 0).perform()
                sleep(10)
            except NameError:
                pass
            except NoSuchElementException:
                pass

            # List to append scrape results
            lazmall_delivery = []
            lazmall_price = []
            lazmall_price_ = []
            lazmall_itemname = []
            lazmall_img = []

            iterate = True
            while iterate:
                try:
                    WebDriverWait(driver, delay)
                    print ("Page is ready")
                    if config_search_method == "By name of the item":
                        sleep(10)
                        lazmall_img.append(driver.find_element_by_xpath('//img[@class="index__image___1YObI "]').get_attribute('src'))
                        driver.get(driver.find_element_by_xpath('//a[@age="0"]').get_attribute('href'))

                        sleep(10)
                    elif config_search_method == "By url":
                        sleep(10)
                        lazmall_img.append(driver.find_element_by_xpath("/html/body/div[4]/div/div[3]/div[1]/div/div/div[1]/div/img").get_attribute("src"))

                    html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")
                    #print(html)
                    soup = BeautifulSoup(html, "html.parser")
                    for item in soup.find_all('div', class_='delivery-option-item__shipping-fee'):
                        if (item.text) == "Free":
                            lazmall_delivery.append("$0.00")
                        else:
                            lazmall_delivery.append(item.text)
                    for item in soup.find_all('h1', class_='pdp-mod-product-badge-title'):
                        if len(item.text) > 90:
                            lazmall_itemname.append(item.text[:50] + '..')
                        else:
                            lazmall_itemname.append(item.text)
                    for item in soup.find_all('div', class_='pdp-product-price'):
                        lazmall_price.append(item.text)
                    for item in soup.find_all('div', class_='origin-block'):
                        lazmall_price_.append(item.text)

                    iterate = False
                except TimeoutException:
                    print ("Loading took too much time!-Try again")
                    iterate = False

            status_text.text("Printing output from LazMall now...")

            col[i+1].image(load_image(os.getcwd()+"\Image\lazmall.png"),width = 200)
            col[i+1].image(lazmall_img[0],width=200)
            col[i+1].write(str(lazmall_itemname[0]))
            if len(lazmall_price_) > 0:
                col[i+1].write(str(lazmall_price[0].replace(lazmall_price_[0],"")))
            else:
                col[i+1].write(str(lazmall_price[0]))
            col[i+1].write(str(lazmall_delivery[0]))
            if len(lazmall_price_) > 0:
                col[i+1].write(f"${format(float(str(lazmall_price[0]).replace(lazmall_price_[0],'').replace('$','')) + float(lazmall_delivery[0].replace('$','')),'.2f')}")
            else:
                col[i+1].write(f"${format(float(str(lazmall_price[0]).replace('$','')) + float(lazmall_delivery[0].replace('$','')),'.2f')}")
            col[i+1].write(lazmall_url, unsafe_allow_html=True)

            progress_bar.progress((i+1)*(1/(len(config_select_ecommerce))))


    # close the automated browser
    driver.close()

    status_text.text("Done!")
    st.balloons()

if st.sidebar.button("Click here for results!"):
    main()
