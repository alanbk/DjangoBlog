from django.conf.urls import url,include
from home.models import Post

from django.views.generic import ListView,DetailView
from . import views

urlpatterns = [
    #url('', views.post_list, name='post_list'),
    url(r'^post$',ListView.as_view(queryset = Post.objects.all().order_by('-created'),template_name="home/post_list.html")),
    url(r'^post/(?P<pk>\d+)$',DetailView.as_view(model = Post ,template_name="home/post_detail.html")),
    url(r'^post/(?P<pk>\d+)$',views.post_detail ,name="post_detail"),
    #url(r'^post/(?P<pk>\d+)/', views.post_detail, name='post_detail'),
    url(r'^post/new', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment, name='add_comment'),
    #url(r'^unlike/(?P<pk>\d)', views.unlike, name = 'unlike'),
    #url(r'^post/like/(?P<pk>\d+/$)', views.like, name = 'like'),
    #url(r'^post/unlike/(?P<id>\w{0,50})$', views.unlike, name = 'unlike'),
    url(r'^post/like/(?P<pk>\d+)/', views.like, name = 'like'),
    url(r'^search/$', views.search, name="search")
]
