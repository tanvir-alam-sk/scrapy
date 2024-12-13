import scrapy
from trip_scraper.items import TripScraperItem
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Property
import requests;
import re
import json


DATABASE_URL= "postgresql://your_username:your_password@postgres:5432/your_database"


class TripSpider(scrapy.Spider):
    name = 'trip_spider'
    allowed_domains = ['trip.com']  # Replace with actual domain if needed
    start_urls = [
        'https://uk.trip.com/hotels',  # Replace with the actual URL you want to scrape
    ]

    def __init__(self, *args, **kwargs):
        super(TripSpider, self).__init__(*args, **kwargs)
        self.engine = create_engine('postgresql://your_username:your_password@localhost:5432/your_database')
        self.Session = sessionmaker(bind=self.engine)
        self.session = self.Session()

    def parse(self, response):
        response=requests.get("https://uk.trip.com/hotels")
        if response.status_code == 200:
            # Search for the JavaScript variable in the page source
            match = re.search(r'window\.(\w+)\s*=\s*(\{.*?\});', response.text, re.DOTALL)
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
        # Example: Scrape multiple properties (adjust based on actual website structure)

        properties = response.xpath('//div[@class="hotel-listing"]')  # Update with the correct XPath
        for prop in properties:
            item = TripScraperItem()

            print("-------------------------------hallo---------------------------")

            item['title'] = prop.xpath('.//h3/text()').get()
            item['rating'] = float(prop.xpath('.//span[@class="rating"]/text()').get())
            item['location'] = prop.xpath('.//span[@class="location"]/text()').get()
            item['latitude'] = float(prop.xpath('.//span[@class="latitude"]/text()').get())
            item['longitude'] = float(prop.xpath('.//span[@class="longitude"]/text()').get())
            item['room_type'] = prop.xpath('.//span[@class="room-type"]/text()').get()
            item['price'] = float(prop.xpath('.//span[@class="price"]/text()').get().replace('$', ''))

            # Image URL extraction (adjust according to actual website)
            image_url = prop.xpath('.//img[@class="property-image"]/@src').get()
            item['image_url'] = image_url

            # Save data into PostgreSQL database
            self.save_to_db(item)

            yield item

    def save_to_db(self, item):
        # Save each item into the database
        property_data = Property(
            title=item['title'],
            rating=item['rating'],
            location=item['location'],
            latitude=item['latitude'],
            longitude=item['longitude'],
            room_type=item['room_type'],
            price=item['price'],
            image_url=item['image_url'],
        )

        self.session.add(property_data)
        self.session.commit()

    def close(self, reason):
        self.session.close()
