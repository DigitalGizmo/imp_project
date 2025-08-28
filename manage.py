#!/usr/bin/env python
import os
import sys
from pathlib import Path

if __name__ == "__main__":
    # Updated to point to config.settings instead of impressions.settings
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.production")

    # Add the impressions directory to Python path so Django can find the apps
    current_path = Path(__file__).resolve().parent
    impressions_path = current_path / 'impressions'
    if str(impressions_path) not in sys.path:
        sys.path.insert(0, str(impressions_path))

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)