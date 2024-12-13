import time
import requests;
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json


# driver=webdriver.Chrome()
# driver.get("https://uk.trip.com/hotels")
response=requests.get("https://uk.trip.com/hotels")
if response.status_code == 200:
    # Search for the JavaScript variable in the page source
    match = re.search(r'window\.(\w+)\s*=\s*(\{.*?\});', response.text, re.DOTALL)
    print(match)
    if match:
        # Extract the matched JavaScript object
        js_object = match.group(2)  # The second group should contain the JavaScript object

        # Try parsing the data as JSON
        try:
            data = json.loads(js_object)
            data= data.get('initData', None)  
            data= data.get('htlsData', None)  
            with open('inbound_cities.json', 'w') as f:
                json.dump(data["inboundCities"], f, indent=4)
            with open('outbound_cities.json', 'w') as f:
                json.dump(data["outboundCities"], f, indent=4)
        except json.JSONDecodeError as e:
            print("Error parsing JSON:", e)
    else:
        print("Could not find JavaScript object in the response.")
else:
    print(f"Failed to fetch the page. Status code: {response.status_code}")