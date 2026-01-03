from bs4 import BeautifulSoup
import requests

class AmazonScraper:
    def fetch_product_data(self, product_name):
        search_url = f"https://www.amazon.com/s?k={product_name.replace(' ', '+')}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        response = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')

        products = []
        for item in soup.select('.s-result-item'):
            title = item.select_one('h2 .a-link-normal')
            price = item.select_one('.a-price .a-offscreen')
            image = item.select_one('.s-image')
            link = item.select_one('h2 .a-link-normal')['href']

            if title and price and image:
                products.append({
                    'title': title.get_text(strip=True),
                    'price': price.get_text(strip=True),
                    'image': image['src'],
                    'link': f"https://www.amazon.com{link}"
                })

        return products

    def filter_results(self, results, category, price_range):
        filtered_results = []
        for product in results:
            if category and category.lower() not in product['title'].lower():
                continue
            
            price = float(product['price'].replace('$', '').replace(',', ''))
            min_price, max_price = map(float, price_range.split('-'))
            if price < min_price or price > max_price:
                continue
            
            filtered_results.append(product)

        # Sort by price and return the three cheapest options
        filtered_results.sort(key=lambda x: float(x['price'].replace('$', '').replace(',', '')))
        return filtered_results[:3]