from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from newsapi import NewsApiClient

import uuid
import boto3

from .models import Blogpost, Comment, Photo
from .forms import CommentForm
S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'catcollector-nn'

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'catcollector-nn'



def home(request):
    newsapi = NewsApiClient(api_key='313c12fcfda3465f89f36b377c088e3b')
    top = newsapi.get_top_headlines(q='coronavirus',
                                    language='en')

    l = top['articles']
    desc = []
    news = []
    img = []

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)

    return render(request, 'home.html', context={"mylist": mylist})


def about(request):
    return render(request, 'about.html')

@login_required
def blogposts_index(request):
    blogposts = Blogpost.objects.filter(user=request.user)
    return render(request, 'blogposts/index.html', {'blogposts': blogposts})

@login_required
def blogposts_all(request):
    blogposts = Blogpost.objects.all()
    return render(request, 'blogposts/get_all_posts.html', {'blogposts': blogposts})

@login_required
def blogposts_detail(request, blogpost_id):
    blogpost = Blogpost.objects.get(id=blogpost_id)
    comment_form = CommentForm()
    return render(request, 'blogposts/detail.html', {'blogpost': blogpost, 'comment_form': comment_form})


def signup(request):
    error_message = ''

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

@login_required
def add_comment(request, blogpost_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.blogpost_id = blogpost_id
        new_comment.save()
<<<<<<< HEAD
    return redirect('detail', blogpost_id = blogpost_id)
=======
    return redirect('detail', blogpost_id=blogpost_id)

>>>>>>> b8a7472c38a771a57e57d1504060b5be7add47fc

@login_required
def add_photo(request, blogpost_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            photo = Photo(url=url, blogpost_id=blogpost_id)
            photo.save()
        except:
            print('An error occurred uploading file to S3')
    return redirect('detail', blogpost_id=blogpost_id)


<<<<<<< HEAD
class BlogpostCreate(CreateView,LoginRequiredMixin):
=======
class BlogpostCreate(LoginRequiredMixin,CreateView):
>>>>>>> b8a7472c38a771a57e57d1504060b5be7add47fc
    model = Blogpost
    fields = ['title', 'body']
    success_url = '/blogposts/'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BlogpostUpdate(UpdateView,LoginRequiredMixin):
    model = Blogpost
    fields = ['title', 'body']


class BlogpostDelete(DeleteView,LoginRequiredMixin):
    model = Blogpost
    success_url = '/blogposts/'