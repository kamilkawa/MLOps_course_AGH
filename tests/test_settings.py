from settings import Settings
from main import load_secrets


def test_settings_loaded_correctly():
    load_secrets()
    settings = Settings()
    assert settings.ENVIRONMENT == "test"
    assert settings.APP_NAME == "ml-api"
    assert isinstance(settings.OPENAI_KEY, str)
    assert len(settings.OPENAI_KEY) > 0
