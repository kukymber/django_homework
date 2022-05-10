from collections import OrderedDict
from datetime import datetime
from urllib.parse import urlparse, urlencode
import requests
from django.utils import timezone
from social_core.exceptions import AuthException, AuthForbidden
from authapp.models import UserProfile

def save_user_profile(request,user,response, *args, **kwargs):
    pass