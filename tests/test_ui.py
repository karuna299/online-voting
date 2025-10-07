from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def test_homepage():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Use pre-installed Chromium driver from Docker
    driver = webdriver.Chrome(service=Service("/usr/bin/chromium-driver"), options=chrome_options)

    driver.get("http://localhost:5000")  # inside Docker network

    assert "Vote" in driver.page_source

    driver.quit()