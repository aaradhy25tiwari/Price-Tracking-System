from bs4 import BeautifulSoup
import requests

class FlipkartScraper:
    def fetch_product_data(self, product_name):
        url = f"https://www.flipkart.com/search?q={product_name}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        products = []
        for item in soup.find_all('div', class_='_1AtVbE'):
            title = item.find('a', class_='IRpwTa')
            price = item.find('div', class_='_30jeq3')
            image = item.find('img', class_='_396cs4')
            link = item.find('a', class_='IRpwTa')

            if title and price and image and link:
                products.append({
                    'title': title.text,
                    'price': price.text,
                    'image': image['src'],
                    'link': f"https://www.flipkart.com{link['href']}"
                })

        return products

    def filter_results(self, results, category=None, price_range=None):
        if category:
            results = [product for product in results if category.lower() in product['title'].lower()]
        
        if price_range:
            min_price, max_price = map(int, price_range.split('-'))
            results = [product for product in results if min_price <= int(product['price'].replace('₹', '').replace(',', '').strip()) <= max_price]

        # Sort by price and return the three cheapest options
        results.sort(key=lambda x: int(x['price'].replace('₹', '').replace(',', '').strip()))
        return results[:3]