from django.shortcuts import render
from .models import Posting
from django.utils import timezone

def func(request):
    return render(request, 'main.html')

def home(request):
    postings = Posting.objects
    return render(request, 'home.html', {'Postings': postings })

def create(request):
    posting = Posting()
    posting.title = request.GET['title']
    posting.pubDate = timezone.datetime.now()
    posting.body = request.GET['body']
   # posting.nickName = request.GET['nickName']
   # posting.isNotice = request.GET['isNotice']
   # posting.image = request.GET['image']
    posting.save()
    postings = Posting.objects
    return redirect('/')