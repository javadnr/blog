from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from .models import Category, Post, Comment
from .forms import CommentForm, PostCreateForm, LogInForm, RegisterForm
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin




class PostListView(ListView):
    model = Post
    template_name = 'list.html'
    context_object_name = 'posts'
    ordering = ['-date_added']

class PostView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = 'post.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('list')
    
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'detail.html'
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        likes_connected = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
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
    template_name = 'update.html'
    fields = ['image','title','description','category']
    success_url = reverse_lazy('list')
     
class CommentView(LoginRequiredMixin,CreateView):
    model = Comment
    template_name = 'comment.html'
    form_class = CommentForm
    success_url = reverse_lazy('list')
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
        return render(request, "search.html",{'searched' :searched , 'posts': posts} )
    else: 
        return render(request, "search.html",{'searched' :searched} )

# class SearchView(ListView):
#     model = Post
#     template_name = 'search.html'
 
#     def get_queryset(self):
#         query = query = self.request.GET.get("searched")
#         post = Post.objects.filter(title__icontains = query)
#         return post

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('list')