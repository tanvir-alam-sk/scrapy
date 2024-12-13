BOT_NAME = 'trip_scraper'

SPIDER_MODULES = ['trip_scraper.spiders']
NEWSPIDER_MODULE = 'trip_scraper.spiders'

ROBOTSTXT_OBEY = True  # Set to False if the website's robots.txt doesn't allow scraping

# PostgreSQL settings for storing data (via SQLAlchemy)
DATABASE_URI = 'postgresql://your_username:your_password@localhost:5432/your_database'

# You may also configure image pipeline settings if you want to download images
IMAGES_STORE = 'images'  # Folder to store images
