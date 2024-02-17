from django.urls import path

from . import views



urlpatterns=[
    path('',views.index,name='starting_page'),
    path('posts',views.posts,name='post_page'),
    path('posts/<slug:slug>',views.single_post,name='page_detail'),
    path('product',views.product_list,name='product_list'),
    path('<slug:slug>',views.product_detail,name='product_detail')
]