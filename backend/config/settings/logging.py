from pathlib import Path

LOG_DIR = Path(__file__).resolve().parents[2] / "logs"

DJANGO_LOG_DIR = LOG_DIR / "django"
CELERY_LOG_DIR = LOG_DIR / "celery"
GUNICORN_LOG_DIR = LOG_DIR / "gunicorn"
REQUEST_LOG_DIR = LOG_DIR / "requests"

for directory in (
    DJANGO_LOG_DIR,
    CELERY_LOG_DIR,
    GUNICORN_LOG_DIR,
    REQUEST_LOG_DIR,
):
    directory.mkdir(parents=True, exist_ok=True)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {

        "standard": {
            "format": "[{asctime}] [{levelname}] {name}: {message}",
            "style": "{",
        },

        "detailed": {
            "format": (
                "[{asctime}] "
                "[{levelname}] "
                "[{name}] "
                "[PID:{process}] "
                "[TID:{thread}] "
                "{module}.{funcName}:{lineno} "
                "{message}"
            ),
            "style": "{",
        },
    },

    "handlers": {

        "console": {
            "class": "logging.StreamHandler",
            "formatter": "standard",
        },

        "django_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": DJANGO_LOG_DIR / "application.log",
            "formatter": "detailed",
            "maxBytes": 10 * 1024 * 1024,
            "backupCount": 10,
        },

        "django_error": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": DJANGO_LOG_DIR / "error.log",
            "formatter": "detailed",
            "level": "ERROR",
            "maxBytes": 10 * 1024 * 1024,
            "backupCount": 10,
        },

        "request_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": REQUEST_LOG_DIR / "api.log",
            "formatter": "detailed",
            "maxBytes": 10 * 1024 * 1024,
            "backupCount": 10,
        },

        "celery_file": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": CELERY_LOG_DIR / "worker.log",
            "formatter": "detailed",
            "maxBytes": 10 * 1024 * 1024,
            "backupCount": 10,
        },

        "gunicorn_access": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": GUNICORN_LOG_DIR / "access.log",
            "formatter": "standard",
            "maxBytes": 10 * 1024 * 1024,
            "backupCount": 10,
        },

        "gunicorn_error": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": GUNICORN_LOG_DIR / "error.log",
            "formatter": "detailed",
            "level": "ERROR",
            "maxBytes": 10 * 1024 * 1024,
            "backupCount": 10,
        },
    },

    "loggers": {

        "django": {
            "handlers": [
                "console",
                "django_file",
                "django_error",
            ],
            "level": "INFO",
            "propagate": False,
        },

        "django.request": {
            "handlers": [
                "console",
                "request_file",
            ],
            "level": "INFO",
            "propagate": False,
        },

        "celery": {
            "handlers": [
                "console",
                "celery_file",
            ],
            "level": "INFO",
            "propagate": False,
        },

        "gunicorn": {
            "handlers": [
                "console",
                "gunicorn_access",
                "gunicorn_error",
            ],
            "level": "INFO",
            "propagate": False,
        },
    },

    "root": {
        "handlers": [
            "console",
            "django_file",
        ],
        "level": "INFO",
    },
}