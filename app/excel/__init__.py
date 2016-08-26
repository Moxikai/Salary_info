from flask import Blueprint
excel = Blueprint('excel',__name__)
from .models import Post,Category
from . import views