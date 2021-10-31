from flask_restx import Resource
from app.main.service.image_prediction_service import celebrity_image_classification
from app.main.util.image_classification_dto import ImageClassificationDto
from flask import request

api = ImageClassificationDto.api 
_image_upload = ImageClassificationDto.image_upload

@api.route('/predict')
class FaceDetection(Resource):
    @api.doc('Image Upload')
    @api.expect(_image_upload) 
    def post(self):
        """Image Upload"""
        return celebrity_image_classification(request)