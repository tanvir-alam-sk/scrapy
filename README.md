# Trip.com Property Scraper

This project is a Scrapy-based web scraper designed to gather property information from Trip.com. 

## Project Directory Structure

```
tripscraper/
│  
├── scrapy.cfg  
├── requirements.txt  
├── .gitignore  
├── README.md  
├── tests/  
│   ├── __init__.py  
│   ├── test_models.py  
│   ├── test_pipelines.py  
│   ├── test_items.py  
│   └── test_spider.py  
│
├── tripscraper/  
│   ├── __init__.py  
│   ├── items.py  
│   ├── middlewares.py  
│   ├── pipelines.py  
│   ├── settings.py  
│   ├── models.py  
│   └── spiders/  
│       ├── __init__.py  
│       └── city_hotels_spider.py

```

## Project Setup

1. **Clone the Repository**

   ```bash
   git clone https://github.com/tanvir-alam-sk/scrapy tripscraper

   ```
2. **Go to the project directory**

   ```bash
   cd tripscraper

   ```
3. **Install Python Dependencies**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```
4. **If above commands (No. 3) does not work**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```


## Running the Scraper

1. **Basic Command**

   Run the Scrapy spider from `tripscraper/tripscraper/spiders/` directory. When you are in root directory the following commands will run the spider.

   ```bash
   cd tripscraper/spiders/
   scrapy crawl city_hotels
   ```

   This will start scraping and save data to the database. To see the result in database go to the `pgadmin` of your database. Then you will be able to see the results.

## Testing

Run the test suite using `pytest`. It will test with code coverage. You have to run the test from project root directory. If you are in some other directory like `spiders` you have to first go to the project root directory using `cd` command.

```bash
pytest --cov=tripscraper
```

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m 'Add feature'`.
4. Push to the branch: `git push origin feature-name`.
5. Open a pull request.

