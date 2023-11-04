from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from .models import Category, Post, Comment
from .forms import CommentForm, PostCreateForm, LogInForm, RegisterForm
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator




class PostListView(ListView):
    model = Post
    template_name = 'posts/list.html'
    context_object_name = 'posts'
    ordering = ['-date_added']

class PostView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'posts/post.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('list')
    
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'posts/detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        data['comment_form'] = CommentForm()
        return data
    
def BlogPostLike(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('blogpost_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('detail', args=[str(pk)]))    

    
class PostUpdateView(LoginRequiredMixin,UpdateView):    
    model = Post
    template_name = 'posts/update.html'
    fields = ['image','title','description','category']
    success_url = reverse_lazy('list')
     

def category_posts(request,category_id):
    category = Category.objects.get(id=category_id)
    post_list = Post.objects.filter(category=category)    
    p = Paginator(post_list, 5)
    page_number = request.GET.get("page")
    posts = p.get_page(page_number)
    return render(request,'posts/category_posts.html',{'category':category, 'posts':posts})


class CommentView(LoginRequiredMixin,CreateView):
    model = Comment
    template_name = 'posts/comment.html'
    form_class = CommentForm
    success_url = '/{post_id}/detail'
    ordering = ['-date_added'] 
    
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    

    
class LogInView(LoginView):
    template_name = 'login.html'
    success_url = reverse_lazy('list')
    form_class = LogInForm
    
class RegisterView(CreateView):
    template_name = 'register.html'
    success_url = reverse_lazy('login')
    form_class = RegisterForm
    
class CreateCategoryView(CreateView):
    model = Category
    template_name = 'category.html'
    success_url = reverse_lazy('post')
    fields = "__all__"

def searchview(request):
    if request.method == "GET":
        searched = request.GET['searched']
        posts = Post.objects.filter(title__icontains = searched)
        return render(request, "posts/search.html",{'searched' :searched , 'posts': posts} )
    else: 
        return render(request, "posts/search.html",{'searched' :searched} )



class DeletePostView(DeleteView):
    model = Post
    template_name = 'posts/delete_post.html'
    success_url = reverse_lazy('list')


