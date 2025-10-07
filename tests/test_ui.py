import subprocess
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def test_homepage():
    # Detect installed Chromium version
    chromium_version = subprocess.check_output(["chromium", "--version"]).decode().strip().split()[-1]
    chrome_major_version = chromium_version.split(".")[0]  # e.g., 141

    # Set Chrome options for headless
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Install ChromeDriver matching installed Chromium
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager(version=chrome_major_version).install()),
        options=chrome_options
    )

    # Open the app
    driver.get("http://localhost:5000")  # service name inside Docker network

    # Simple assertion
    assert "Vote" in driver.page_source

    # Quit driver
    driver.quit()