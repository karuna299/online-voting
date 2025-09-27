import os

class Config:
    SECRET_KEY = "dev_key"  # Change in prod

    # Redis settings
    REDIS_HOST = os.getenv("REDIS_HOST", "redis")
    REDIS_PORT = int(os.getenv("REDIS_PORT", 6379))
    REDIS_DB   = int(os.getenv("REDIS_DB", 0))
