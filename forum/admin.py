from django.contrib import admin
from .models import Category, SubCategory, Thread, Post


admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Thread)
admin.site.register(Post)
