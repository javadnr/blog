from django.urls import path
from .views import DeletePostView, DeletePostView,BlogPostLike, PostView,PostListView,PostDetailView,PostUpdateView, CommentView, LogInView, RegisterView,CreateCategoryView,searchview
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('post',PostView.as_view(),name='post'),
    path('',PostListView.as_view(),name='list'),
    path('<int:pk>/detail/',PostDetailView.as_view(),name='detail'),
    path('<int:pk>/update/',PostUpdateView.as_view(),name='update'),
    path('blogpost-like/<int:pk>',BlogPostLike, name="blogpost_like"),
    path('<int:pk>/comment/',CommentView.as_view(), name="comment"),
    path('login/',LogInView.as_view(), name="login"),
    # path('register/',RegisterView.as_view(), name="register"),
    # path('logout/',LogoutView.as_view(), name="logout"),
    path('category/',CreateCategoryView.as_view(), name="category"),
    path('search/',searchview, name="search"),
    path('delete/<int:pk>/',DeletePostView.as_view(), name="delete"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
