from flask import Flask, render_template, request
from scrapers.amazon_scraper import AmazonScraper
from scrapers.flipkart_scraper import FlipkartScraper
from scrapers.jiomart_scraper import JioMartScraper
from scrapers.reliance_digital_scraper import RelianceDigitalScraper

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        product_name = request.form['product_name']
        category = request.form.get('category')
        price_range = request.form.get('price_range')

        amazon_scraper = AmazonScraper()
        flipkart_scraper = FlipkartScraper()
        jiomart_scraper = JioMartScraper()
        reliance_scraper = RelianceDigitalScraper()

        results = []
        results.extend(amazon_scraper.fetch_product_data(product_name))
        results.extend(flipkart_scraper.fetch_product_data(product_name))
        results.extend(jiomart_scraper.fetch_product_data(product_name))
        results.extend(reliance_scraper.fetch_product_data(product_name))

        # Sort results by price and get the three cheapest options
        sorted_results = sorted(results, key=lambda x: x['price'])[:3]

        return render_template('results.html', prices=sorted_results)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
