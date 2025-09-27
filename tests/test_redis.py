import pytest

def test_redis_connection(client):
    # Use the Redis client from the Flask app
    r = client.application.redis

    # Set and get a test key
    r.set("test_key", "123")
    value = r.get("test_key")

    assert value == "123"
