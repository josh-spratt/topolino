from src.config import Config


def test_config():
    assert Config.URL == "https://disneyworld.disney.go.com/resorts/#/value"
    assert Config.HEADERS == {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36"
    }
