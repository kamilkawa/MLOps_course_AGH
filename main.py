import argparse
import os
from dotenv import load_dotenv
from settings import Settings
from pathlib import Path
import yaml


def export_envs(environment: str = "dev") -> None:
    env_file = Path(__file__).parent / "config" / f".env.{environment}"
    load_dotenv(env_file, override=True)


def load_secrets(secrets_path: str = "secrets.yaml") -> None:
    secrets_file = Path(__file__).parent / secrets_path
    with open(secrets_file, "r") as f:
        secrets = yaml.safe_load(f)
    for key, value in secrets.items():
        os.environ[key] = str(value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)
    load_secrets()

    settings = Settings()

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("OPENAI_KEY: ", settings.OPENAI_KEY)
