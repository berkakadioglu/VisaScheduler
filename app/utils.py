"""Small shared path helpers used across the application."""

from pathlib import Path

APP_DIR = Path(__file__).resolve().parent
TEMPLATE_DIR = APP_DIR/"templates"
