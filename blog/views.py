from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy

from .models import Post
from .forms import PostForm,EditForm
# Create your views here.
#def home(request):
 #   return render(request, 'home.html',{})

class HomeView(ListView):
    model = Post
    template_name ='home.html'
    ordering = ['-post_date']


class Articleview(DetailView):
    model = Post
    template_name = 'article_details.html'

class AddpostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'

class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'updatepost.html'
    #fields= ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
    model= Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')