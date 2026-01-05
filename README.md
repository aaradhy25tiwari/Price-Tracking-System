# Price Tracking System

This project is a web application that allows users to track prices of electronic products from various e-commerce websites. It scrapes product data, including prices, images, and links, and displays the three cheapest options based on user input.

## Features

- Scrapes product prices from multiple websites including Amazon, Flipkart, JioMart, and Reliance Digital.
- Allows users to filter results based on category and price range.
- Displays the three cheapest options with their respective prices, images, and product links.

## Project Structure

```markdown
price-tracking-system
├── app.py                     # Main entry point of the application
├── scrapers                   # Package containing scraper classes
│   ├── __init__.py           # Initializes the scrapers package
│   ├── amazon_scraper.py      # Scraper for Amazon
│   ├── flipkart_scraper.py    # Scraper for Flipkart
│   ├── jiomart_scraper.py     # Scraper for JioMart
│   └── reliance_digital_scraper.py # Scraper for Reliance Digital
├── templates                  # HTML templates for the application
│   ├── index.html             # Input form for product search
│   └── results.html           # Display results of the product search
├── static                     # Static files (CSS, images, etc.)
│   └── styles.css             # CSS styles for the application
├── requirements.txt           # Python dependencies for the project
└── README.md                  # Documentation for the project
```

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/aaradhy25tiwari/Price-Tracking-System.git
   cd price-tracking-system
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:

   ```bash
   python app.py
   ```

2. Open your web browser and go to `http://127.0.0.1:5000/`.

3. Enter the product name, select the category, and specify the price range to see the results.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.
