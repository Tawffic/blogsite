from django.shortcuts import render
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy

from .models import Post,category
from .forms import PostForm,EditForm
# Create your views here.
#def home(request):
 #   return render(request, 'home.html',{})

class HomeView(ListView):
    model = Post
    template_name ='home.html'
    ordering = ['-post_date']

    def get_context_data(self, *args, **kwargs):
        cat_menu = category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context  ['cat_menu'] = cat_menu
        return context



class Articleview(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = category.objects.all()
        context = super(Articleview, self).get_context_data(*args, **kwargs)
        context  ['cat_menu'] = cat_menu
        return context

class AddpostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    #fields = '__all__'


class AddCategoryView(CreateView):
    model = category
    #form_class = PostForm
    template_name = 'add_category.html'
    fields = '__all__'
class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'updatepost.html'
    #fields= ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
    model= Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

def CategoryView(request,cats):
    category_posts= Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats':cats.title(), 'category_posts':category_posts})




def CategoryListView(request):
    cat_menu_list = category.objects.all()
    return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})
