from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q   # Q is used for complex search queries
from .models import Post, Author, Category
from .forms import PostForm, AuthorForm, CategoryForm, PostSearchForm


def home(request):

    posts = Post.objects.all()

    context = {
        'posts': posts,
        'title': 'Home'
    }
    return render(request, 'blog/home.html', context)



def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})



def create_post(request):

    if request.method == 'POST':

        form = PostForm(request.POST)

        if form.is_valid():

            form.save()
            return redirect('home')  

    else:

        form = PostForm()

    return render(request, 'blog/create_post.html', {'form': form, 'title': 'New Post'})



def create_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('author_list')
    else:
        form = AuthorForm()

    return render(request, 'blog/create_author.html', {'form': form, 'title': 'New Author'})



def author_list(request):
    authors = Author.objects.all().order_by('name')
    return render(request, 'blog/author_list.html', {'authors': authors, 'title': 'Authors'})



def create_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category_list')
    else:
        form = CategoryForm()

    return render(request, 'blog/create_category.html', {'form': form, 'title': 'New Category'})



def category_list(request):
    categories = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categories': categories, 'title': 'Categories'})



def search_posts(request):
    form = PostSearchForm(request.GET)

    results = []

    if form.is_valid():
        query = form.cleaned_data.get('query', '')

        if query:
            results = Post.objects.filter(
                Q(title__icontains=query) |      
                Q(content__icontains=query)      
            )

    context = {
        'form': form,
        'results': results,
        'title': 'Search Posts'
    }
    return render(request, 'blog/search.html', context)