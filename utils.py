from playwright.sync_api import sync_playwright
from pathlib import Path
from config import IMG_DIRECTORY

def unique_path(directory, filename):
    counter = 0
    while True:
        prefixed_filename = f"{counter:02d}_{filename}"
        path = Path(directory) / prefixed_filename
        if not path.exists():
            return path
        counter += 1

def take_screenshot(url, filename="screenshot.png"):
    with sync_playwright() as playwright:
        webkit = playwright.webkit
        browser = webkit.launch()
        browser_context = browser.new_context(device_scale_factor=2)
        page = browser_context.new_page()
        page.goto(url)
        element = page.locator(".my_code")
        screenshot_bytes = element.screenshot()
        browser.close()
        directory = IMG_DIRECTORY
        file_path = unique_path(directory, filename)
        with open(file_path, mode="wb") as img:
            img.write(screenshot_bytes)
        return file_path

if __name__ == "__main__":
    take_screenshot("http://127.0.0.1:5000")