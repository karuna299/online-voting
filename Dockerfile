FROM python:3.11-slim

# Install system dependencies for Chromium
RUN apt-get update && apt-get install -y \
    wget \
    gnupg \
    unzip \
    curl \
    chromium \
    chromium-driver \
    && [ ! -f /usr/bin/chromedriver ] && ln -s /usr/bin/chromium-driver /usr/bin/chromedriver || true \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Pre-cache ChromeDriver to avoid downloading at runtime
RUN python -c "from webdriver_manager.chrome import ChromeDriverManager; from selenium.webdriver.chrome.service import Service; Service(ChromeDriverManager().install())"

# Copy app source
COPY . .

# Run the app
CMD ["python", "run.py"]