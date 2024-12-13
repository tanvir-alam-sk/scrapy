import scrapy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Property, Base

class PostgresPipeline:
    def __init__(self):
        # Create PostgreSQL engine
        self.engine = create_engine('postgresql://your_username:your_password@localhost:5432/your_database')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)
    
    def process_item(self, item, spider):
        session = self.Session()

        # Insert the item into the database
        property_data = Property(
            title=item['title'],
            rating=item['rating'],
            location=item['location'],
            latitude=item['latitude'],
            longitude=item['longitude'],
            room_type=item['room_type'],
            price=item['price'],
            image_url=item['image_url']
        )

        session.add(property_data)
        session.commit()
        session.close()

        return item
