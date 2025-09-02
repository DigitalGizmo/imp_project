#!/usr/bin/env python
import os
import sys
from pathlib import Path

if __name__ == "__main__":
    # Updated to point to config.settings instead of impressions.settings
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

    # # Add the impressions directory to Python path so Django can find the apps
    # current_path = Path(__file__).resolve().parent
    # impressions_path = current_path / 'impressions'
    # if str(impressions_path) not in sys.path:
    #     sys.path.insert(0, str(impressions_path))

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    execute_from_command_line(sys.argv)