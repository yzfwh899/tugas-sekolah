import os

def save_image(image_data):
    upload_folder = 'static/uploads'
    os.makedirs(upload_folder, exist_ok=True)
    filename = image_data.filename
    image_path = os.path.join(upload_folder, filename)
    image_data.save(image_path)
    return f'uploads/{filename}'