from flask import request
from werkzeug.exceptions import RequestEntityTooLarge
from werkzeug.utils import secure_filename
from app.main.util.apiresponse import apiResponse
from app.main.config import UPLOAD_FOLDER, image_name_size
from app.main.service import image_helper
import os

def image_save(new_request):
    try:
        data = new_request.files
    except RequestEntityTooLarge as e:
        return apiResponse(False,f"File is Size is Too Large",None,str(e)).__dict__, 413
    
    file = data['image']
    
    if 'image' not in data:
        message = 'No image part in the request'

    elif file.filename == '':
        message = 'No image selected for uploading'
        
    elif len(file.filename) > image_name_size:
        message = 'File name is too Large'
    elif file:
        # resp, status = Auth.get_logged_in_user(request)
        # user_id = resp['data']['id']
        # folder = UPLOAD_FOLDER
        filename = secure_filename(file.filename)
        # extension = file.filename.split(".")[-1]
        # filename = f"{filename}.{extension}"

        file_path = UPLOAD_FOLDER + f"/{filename}"
        if os.path.exists(file_path) or os.path.isfile(file_path):
            os.remove(file_path)

        image_path = image_helper.save_image(data["image"],name = filename)

        message = None
        
    return image_path, message
