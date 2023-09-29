from playwright.sync_api import sync_playwright
import os 
from style.models import Image
from app import db
import datetime
from flask import current_app, redirect, url_for
#app.config["UPLOADED_PHOTOS_DEST"] = "static/img"

def take_screenshot_from_url(url, session_data, id):
    # Define the screenshot path and filename
    screenshot_filename = f"screenshot_{id}.png"
    screenshot_directory = os.path.join('static', "screenshots")
    screenshot_path = os.path.join(screenshot_directory, screenshot_filename)

    try:
        with sync_playwright() as playwright:
            webkit = playwright.webkit
            browser = webkit.launch()
            browser_context = browser.new_context(device_scale_factor=12)
            browser_context.add_cookies([session_data])
            page = browser_context.new_page()
            page.goto(url)
            page.locator(".code").screenshot(path=screenshot_path)
            browser.close()
    except Exception as e:
        # Handle exceptions, log errors, or return an appropriate response
        print(f"Error: {e}")
        return None

    try:
        # Update the image path in the database
        image = Image.query.get(id)
        image.image_file = screenshot_path
        db.session.commit()
        return image
    except Exception as e:
        # Handle database update errors
        print(f"Database Error: {e}")
        return None
    
    

# def take_screenshot_from_url(url, session_data, width=1920, height=1080, quality=80):
#     with sync_playwright() as playwright:
#         webkit = playwright.webkit
#         browser = webkit.launch()
#         browser_context = browser.new_context()
#         browser_context.add_cookies([session_data])
#         page = browser_context.new_page()
        
#         # Set the viewport size to control the size of the screenshot
#         page.set_viewport_size(width=width, height=height)
        
#         page.goto(url)

#         # Take a screenshot with the specified options
#         screenshot_bytes = page.screenshot()
        
#         browser.close()
#         return screenshot_bytes


