from flask import current_app
from PIL import Image
import os

def save_image(image_data):
    upload_folder = 'static/uploads'
    full_upload_path = os.path.join(current_app.root_path, upload_folder)
    os.makedirs(full_upload_path, exist_ok=True)

    filename = image_data.filename
    image_path = os.path.join(full_upload_path, filename)

    image_data.save(image_path)
    return f'{upload_folder}/{filename}'