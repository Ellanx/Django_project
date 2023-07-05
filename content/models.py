from django.db import models

class Feed(models.Model):
    content = models.TextField()
    image = models.TextField()
    profile_image = models.TextField()
    user_id = models.TextField()
    like_count = models.IntegerField() # 좋아요 숫자 , 숫자가 들어가기때문에 interger사용