from .models import Category,Post

def categories(request):
    categories = Category.objects.all()
    return {'categories':categories}

def posts(request):
    posts = Post.objects.all()
    return {'posts':posts}