from django.urls import path
from .views import (category_list, subcategory_list, thread_list, post_list, upvote_post, downvote_post, add_category, 
                    add_subcategory, create_thread)

urlpatterns = [
    path('', category_list, name='category_list'),
    path('category/new/', add_category, name='category_add'),
    path('category/<int:category_id>/', subcategory_list, name='subcategory_list'),
    path('category/<int:category_id>/new/', add_subcategory, name='subcategory_add'),
    path('subcategory/<int:subcategory_id>/', thread_list, name='thread_list'),
    path('subcategory/<int:subcategory_id>/new/', create_thread, name='thread_add'),
    path('thread/<int:thread_id>/', post_list, name='post_list'),
    path('post/<int:post_id>/upvote/', upvote_post, name='upvote_post'),
    path('post/<int:post_id>/downvote/', downvote_post, name='downvote_post'),
]
