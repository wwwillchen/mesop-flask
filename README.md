# Mesop Flask

This example shows you how to use Mesop and Flask together

## How to run

This project uses `uv` so you will need to [install it](https://docs.astral.sh/uv/#getting-started).

### Development mode

You can run it like this:

```sh
uv run main.py
```

### Production mode

You can use `gunicorn` to run the app in production mode:

```sh
uv run gunicorn main:combined_app
```

> Note: `uv run` is just a wrapper to use the gunicorn command with the uv virtual environment.

