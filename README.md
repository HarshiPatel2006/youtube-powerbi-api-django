# YouTube Power BI API

Django service that exposes YouTube channel data as JSON for a Power BI dashboard.

## Endpoints

- `GET /` — health message
- `GET /api/channel_id?channel_name=...` — look up a channel ID by name
- `GET /api/data?channel_name=...` or `GET /api/data?channel_id=...` — channel info, videos, top videos and geo data

## Configuration

Environment variables (a local `.env` file is loaded automatically):

| Variable | Purpose |
| --- | --- |
| `YT_API_KEY` | YouTube Data API key (required) |
| `SECRET_KEY` | Django secret key (required unless `DEBUG=1`) |
| `DEBUG` | `1` for local development; off by default |
| `DJANGO_ALLOWED_HOSTS` | Optional extra comma-separated hostnames |

## Run locally

```bash
python -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
DEBUG=1 python manage.py runserver 8080
```

## Deploy (Render)

- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn ytapi.wsgi:application --bind 0.0.0.0:$PORT --timeout 120`
- Environment: `YT_API_KEY`, `SECRET_KEY`, `DEBUG=0`
