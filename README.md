# Price-Comparison-Streamlit

![alt text](https://github.com/Desmondchoo42/Price-Comparison-Streamlit/blob/main/Streamlit.jpg?raw=true)

## Introduction

This script utilises packages Selenium and Streamlit to compare prices between Shopee Mall and LazMall. The script will check with the user on the item name or the url and output information such as image, item name, price, delivery fee as well as the url in a tabular format for easy comparison. 

## Methodology

There are two options presented to the users in the streamlit interface - (1) Price Comparison using name of the item and (2) By individual url. 

* Options for user in Streamlit interface: 

   * Price Comparison using name of the item
     * Script will search selected E-commerce (Shopee Mall and / or LazMall) by the name of the item and extract the information from the first item of the search result. 
     * Due to this methodology, user is recommended to type in as much details as possible. For example, if user intend to search for the item "Tineco Ifloor Cordless Vacuum",        user should input the entire string into the text input rather than just entering "Tineco vacuum cleaner" in order to get a more accurate result. 

   * By individual url
     * Due to the limitation of the earlier method, user can also input the url for a more accurate comparison.   

* Image extraction
  * Image will be extracted based on the thumbnail of the search result instead of the product PDP page as PDP page might contain video as the first preview image.

* Anti-scraping / Traffic monitoring by Lazada website
  * This script is able to circumvent this by using Selenium ActionChain function (drag and drop). For now, this method is sufficient.    

## Example of the interface - different options and results
* Initial interface - option to input url
![alt text](https://github.com/Desmondchoo42/Price-Comparison-Streamlit/blob/main/Image/Preview%202.jpg?raw=true)


* Output
![alt text](https://github.com/Desmondchoo42/Price-Comparison-Streamlit/blob/main/Image/Preview%201.jpg?raw=true)

## How to use

* Main Package
  * Streamlit
  * Selenium (Requires chromedriver)

* How to use
  * Ensure that chromedriver.exe is present in the working directory together with the title image
  * In terminal, direct to the directory containing the python script and run command "streamlit run scraping.py"    

## Possible improvement in the future

* More E-commerce platforms
  * Currently the time-saving or advantage is not high for price comparison with just two E-commerce platforms. However, this script can be easily adapted to incorporate more E-commerce platforms such as Hachi-Tech, Courts, Harvey Norman or even Qoo10. 

* More information should be extracted so that user can make better pricing decisions
  * Currently this script just extract the price of the item, delivery fee and add them up for user to compare. However, there are other factors that user takes into account before making a purchase. Factors such as number of reviews (both positive and negative), platform vouchers, warranty and even estimated delivery times do play a part in the user's purchasing decision making process. For this to be really useful, such information should be extracted. 

* Potential database to store all the search history by the user 
  * This will allow the user can do a price comparison not just against another E-commerce platform but also along the time horizon - if the price is indeed at its lowest point for "X" days / weeks / months.     

