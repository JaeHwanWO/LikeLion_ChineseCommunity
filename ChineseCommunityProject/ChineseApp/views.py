from django.shortcuts import render, redirect, get_object_or_404
from .models import Posting
from django.utils import timezone
from django.core.mail import EmailMessage
from django.core.mail import send_mail

def func(request):
    return render(request, 'main.html')

def home(request):
    postings = Posting.objects
    return render(request, 'home.html', {'Postings': postings })

def new(request):
   return render(request, 'new.html')


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

   # email 보내보기
   # email = EmailMessage('subject text', 'body text', 'ChineseCommunityDeveloper@gmail.com', to=['yy991125@naver.com'])
   # email.send()
   send_mail('인증 메일입니다', '인증번호는 ()입니다', 'ChineseCommunityDeveloper@gmail.com', ['yy991125@naver.com'], fail_silently=False,)

   return render(request, 'home.html', {'postings': postings})

def detail(request, posting_id):
   posting_detail = get_object_or_404(Posting, pk=posting_id)
   return render(request, 'detail.html', {
      'posting': posting_detail
   })

def send_email():
   return render(request, 'email_auth.html')