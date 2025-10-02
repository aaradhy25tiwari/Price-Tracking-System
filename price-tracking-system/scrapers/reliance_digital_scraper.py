from bs4 import BeautifulSoup
import requests

class RelianceDigitalScraper:
    def fetch_product_data(self, product_name):
        url = f"https://www.reliancedigital.in/search?q={product_name}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        products = []
        for item in soup.select('.product-list .product'):
            title = item.select_one('.product-title').text.strip()
            price = item.select_one('.price').text.strip()
            image = item.select_one('img')['src']
            link = item.select_one('a')['href']

            products.append({
                'title': title,
                'price': price,
                'image': image,
                'link': link
            })

        return products

    def filter_results(self, results, category=None, price_range=None):
        if category:
            results = [product for product in results if category.lower() in product['title'].lower()]

        if price_range:
            min_price, max_price = map(float, price_range.split('-'))
            results = [product for product in results if min_price <= float(product['price'].replace('₹', '').replace(',', '').strip()) <= max_price]

        return sorted(results, key=lambda x: float(x['price'].replace('₹', '').replace(',', '').strip()))[:3]