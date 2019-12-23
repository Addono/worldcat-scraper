# Worldcat Scraper
Collects book titles from [Worldcat](https://worldcat.org/)'s search pages. See [this](https://gist.github.com/Addono/ad031c113138e0254112c3f5f96645b8) example of a scrape getting the titles of all Dutch fiction books released in 2019.

*Note: Worldcat search only allows you to scroll through the first 5000 hits.*

## Usage
```bash
scrapy runspider spider.py
```

Or if you want to save the output, e.g. as CSV:
```bash
scrapy runspider spider.py --output=res.csv -t csv
```
