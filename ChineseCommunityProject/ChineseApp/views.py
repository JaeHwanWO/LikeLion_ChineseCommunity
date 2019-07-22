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
    posting.body = request.GET['body']
    posting.pubDate = timezone.datetime.now()
    posting.save()
    postings = Posting.objects
    return render(request, 'newPost.html', {'postings': postings})