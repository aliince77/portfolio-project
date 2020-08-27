from django.urls import path
import blog.views

urlpatterns = [
    path('', blog.views.allblogs, name='allblogs'),
    path('<int:blog_id>/', blog.views.blogdetail, name='blogdetail'),
]
