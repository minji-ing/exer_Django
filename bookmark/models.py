from django.db import models
from django.urls import reverse

# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        return "이름 : " + self.site_name + ", 주소 : " + self.url

# 장고는 db를 자동 생성할 때 알아서 시퀀스 역할을 하는 id, 수정일, 입력일
# 등을 자동으로 포함하여 테이블을 생성한다
# 게시글 수정 완료 후 가는 페이지 결정하는 메소드
    def get_absolute_url(self):
        # reverse 메소드는 url 패턴의 이름과 추가 인자를 전달받아 url 생성
        return reverse('detail', args=[self.id])
