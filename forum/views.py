from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

from .models import Category, SubCategory, Thread, Post
from .forms import CategoryForm, CreateSubCategoryForm, ThreadForm, PostForm


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'forum/category_list.html', {'categories': categories})

def subcategory_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    subcategories = category.subcategories.all()
    return render(request, 'forum/subcategory_list.html', {'category': category, 'subcategories': subcategories})

def thread_list(request, subcategory_id):
    subcategory = get_object_or_404(SubCategory, id=subcategory_id)
    threads = subcategory.threads.all()
    paginator = Paginator(threads, 10)  # Pagination, 10 threads per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'forum/thread_list.html', {'subcategory': subcategory, 'page_obj': page_obj})

def post_list(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    posts = thread.posts.all()
    paginator = Paginator(posts, 10)  # Pagination, 10 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.created_by = request.user
            post.save()
            # on reinitialise le formulaire
            form = PostForm()
            return redirect('post_list', thread_id=thread_id)
    else:
        form = PostForm()
    
    return render(request, 'forum/post_list.html', {'thread': thread, 'page_obj': page_obj, 'form': form})

@login_required
def upvote_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.upvotes.all():
        post.upvotes.remove(request.user)
    else:
        post.upvotes.add(request.user)
        post.downvotes.remove(request.user)
    return JsonResponse({'total_votes': post.total_votes()})

@login_required
def downvote_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user in post.downvotes.all():
        post.downvotes.remove(request.user)
    else:
        post.downvotes.add(request.user)
        post.upvotes.remove(request.user)
    return JsonResponse({'total_votes': post.total_votes()})

@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()
        
    return render(request, 'forum/category_new.html', {'form': form})

@login_required
def add_subcategory(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CreateSubCategoryForm(request.POST)
        if form.is_valid():
            subcategory = form.save(commit=False)
            subcategory.category = category
            subcategory.save()
            return redirect('subcategory_list', category_id=category_id)
    else:
        form = CreateSubCategoryForm()
        
    return render(request, 'forum/subcategory_new.html', {'form': form, 'category': category})

@login_required
def create_thread(request, subcategory_id):
    subcategory = get_object_or_404(SubCategory, id=subcategory_id)
    if request.method == 'POST':
        form = ThreadForm(request.POST)
        if form.is_valid():
            thread = form.save(commit=False)
            thread.subcategory = subcategory
            thread.created_by = request.user
            thread.save()
            return redirect('thread_list', subcategory_id=subcategory_id)
    else:
        form = ThreadForm()
        
    return render(request, 'forum/thread_new.html', {'form': form, 'subcategory': subcategory})
