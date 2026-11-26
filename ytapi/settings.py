import os
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(BASE_DIR / ".env")

DEBUG = os.getenv("DEBUG", "0").lower() in ("1", "true", "yes")

# A fallback key is only acceptable for local development.
SECRET_KEY = os.getenv("SECRET_KEY") or (
    "local-dev-only-insecure-key" if DEBUG else None
)
if not SECRET_KEY:
    raise RuntimeError("SECRET_KEY environment variable is required when DEBUG is off")

ALLOWED_HOSTS = [
    "youtube-powerbi-api-v7j5.onrender.com",
    "localhost",
    "127.0.0.1",
] + [h.strip() for h in os.getenv("DJANGO_ALLOWED_HOSTS", "").split(",") if h.strip()]

INSTALLED_APPS = []
MIDDLEWARE = []
ROOT_URLCONF = "ytapi.urls"
WSGI_APPLICATION = "ytapi.wsgi.application"
DATABASES = {}
USE_TZ = True
TIME_ZONE = "UTC"
