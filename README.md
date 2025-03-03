# Website Copier

## Overview
This project is a **website copier** that allows users to download and save the complete structure of a website, including HTML, CSS, JavaScript, and media files. The project is built using **Selenium** and other web scraping tools.

## Features
- Download full website structure (HTML, CSS, JavaScript, and assets)
- Handle dynamic content loaded via JavaScript
- Save pages locally with original structure
- Multi-threaded downloading for efficiency

## Requirements
- Python 3.x
- Selenium
- BeautifulSoup
- Requests
- ChromeDriver or Edge WebDriver (based on your browser)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/nematovN/website_copier.git
   cd website_copier
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Download and set up the appropriate WebDriver for your browser (Chrome or Edge).

## Usage
1. Run the script with the target website URL:
   ```bash
   python copier.py --url "https://example.com"
   ```
2. The copied website will be saved in the `output/` directory.

## Configuration
You can modify the `config.json` file to customize:
- User-Agent headers
- Output directory
- Exclusion rules

## Notes
- Make sure the website you are copying allows scraping (check robots.txt)
- Avoid excessive requests to prevent being blocked
- Do not use this tool for unauthorized or unethical purposes

## License
MIT License

## Author
[NematovN](https://github.com/nematovN)

