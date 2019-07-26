from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from rest_framework import serializers

from .models import User
from .tokens import account_activation_token

from utils.common.cipher ipmort AESCipher


# todo: 뒤에 코드 쓰기 https://inma.tistory.com/116?category=984128