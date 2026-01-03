from bs4 import BeautifulSoup
import requests

class JioMartScraper:
    def fetch_product_data(self, product_name):
        url = f"https://www.jiomart.com/search?q={product_name}"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        products = []
        for item in soup.select('.product'):
            title = item.select_one('.product-name').get_text(strip=True)
            price = item.select_one('.price').get_text(strip=True)
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
        filtered_results = results

        if category:
            filtered_results = [product for product in filtered_results if category.lower() in product['title'].lower()]

        if price_range:
            min_price, max_price = map(float, price_range.split('-'))
            filtered_results = [
                product for product in filtered_results
                if min_price <= float(product['price'].replace('₹', '').replace(',', '').strip()) <= max_price
            ]

        # Sort by price and return the three cheapest options
        filtered_results.sort(key=lambda x: float(x['price'].replace('₹', '').replace(',', '').strip()))
        return filtered_results[:3]