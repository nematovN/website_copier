import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

# Edge WebDriver sozlamalari
edge_driver_path = "C:\\msedgedriver\\msedgedriver.exe"
edge_options = Options()
edge_options.add_argument("--start-maximized")

service = Service(edge_driver_path)
driver = webdriver.Edge(service=service, options=edge_options)

# **Sayt manzili**
base_url = "enter_your_base_url"
driver.get(base_url)

# **Fayllar uchun katalog yaratish**
project_folder = "apple_site"
os.makedirs(project_folder, exist_ok=True)

assets_folder = os.path.join(project_folder, "assets")
os.makedirs(assets_folder, exist_ok=True)

# **Saytdagi barcha elementlarni yuklash uchun kutish**
time.sleep(5)

# **JS, CSS, rasmlar, fontlar va boshqa resurslarni yuklab olish**
def download_file(url, folder):
    parsed_url = urlparse(url)
    filename = os.path.basename(parsed_url.path)
    file_path = os.path.join(folder, filename)

    if not filename or "." not in filename:
        return None  # Noto‘g‘ri fayl nomlarini o‘tqazib yuboramiz

    try:
        response = requests.get(url, stream=True)
        with open(file_path, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
        return os.path.join("assets", filename)
    except:
        return None

# **HTML faylni yuklab olish va resurslarni mahalliyga o'zgartirish**
def save_page(url, filename):
    driver.get(url)
    time.sleep(5)  # Sahifa to'liq yuklanishi uchun kutish

    soup = BeautifulSoup(driver.page_source, "html.parser")

    for tag in soup.find_all(["link", "script", "img", "source"]):
        attr = "src" if tag.name in ["script", "img", "source"] else "href"
        file_url = tag.get(attr)

        if file_url and not file_url.startswith("data") and "http" in file_url:
            full_url = urljoin(url, file_url)
            local_path = download_file(full_url, assets_folder)

            if local_path:
                tag[attr] = local_path  # HTML'dagi URL'ni o‘zgartiramiz

    # **Sahifani fayl sifatida saqlash**
    html_path = os.path.join(project_folder, filename)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(str(soup))

    print(f"✅ {filename} yuklandi!")

# **Barcha sahifalarni yuklash**
save_page(base_url, "index.html")

# **Saytdagi barcha linklarni topish**
soup = BeautifulSoup(driver.page_source, "html.parser")
page_links = set()

for link in soup.find_all("a", href=True):
    full_url = urljoin(base_url, link["href"])
    if base_url in full_url and full_url not in page_links:
        page_links.add(full_url)

# **Har bir sahifani yuklab olish**
for i, link in enumerate(page_links, start=1):
    filename = f"page_{i}.html"
    save_page(link, filename)

# **Brauzerni yopish**
driver.quit()

print("\n🚀 Sayt to‘liq yuklandi! Barcha fayllar mahalliy saqlangan.")
