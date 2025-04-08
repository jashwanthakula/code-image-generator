import os

THEME = "monokai"
CODE_FILE = "sample_code.py"
IMG_FILENAME = "screenshot.png"
IMG_DIRECTORY = "screenshots"

with open(CODE_FILE, "r", encoding="utf-8") as f:
    CODE = f.read()