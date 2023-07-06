from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed

class Main(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id') # select * from content_feed가 됨, '-id'는 id가 입력될시 역순으로 나옴      
        return render(request, "main/main.html", context=dict(feed_list=feed_list))

