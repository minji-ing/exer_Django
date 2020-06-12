from django.contrib import admin

# Register your models here.
# 내가 만든 모델을 관리자 페이지에서 관리할 수 있도록 등록
from .models import Bookmark

# 관리자 페이지에서 모델 관리
admin.site.register(Bookmark)
