from os import path
from flask_restx import Api
from flask import Blueprint

from app.main.config import authorizations, version

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='Image Classification Project',
          version='1.0',
          description='Face Detection of Lionel Messi, Maria Sahapora, Serena Williams, Virat Kohli and Roger Fedrer',
          authorizations=authorizations
          )

from app.main.controller.image_classification_controller import api as image_clf_ns

api.add_namespace(image_clf_ns, path='/face')

