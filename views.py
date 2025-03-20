
from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all() 
    return render(request, 'blog/post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) 
    return render(request, 'blog/post_detail.html', {'post': post})
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, PostImage
from .forms import PostForm, PostImageForm

def post_create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            post = post_form.save(commit=False)
            post.author = request.user 
            post.save()

            
            for img in request.FILES.getlist('images'):
                PostImage.objects.create(post=post, image=img)
            return redirect('post_list')
    else:
        post_form = PostForm()
    return render(request, 'blog/post_form.html', {'post_form': post_form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('post_list')
    else:
        post_form = PostForm(instance=post)
    return render(request, 'blog/post_form.html', {'post_form': post_form})
from django.shortcuts import get_object_or_404, redirect
from .models import Post

def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')
def load_more_posts(request):
    posts = Post.objects.all()[10:20]  # 10번째부터 20번째까지 가져옴
    posts_data = [{'id': post.id, 'title': post.title, 'content': post.content} for post in posts]
    return JsonResponse({'posts': posts_data})

from .forms import CommentForm

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        comment_form = CommentForm()
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})
from django.db.models import Q
from django.shortcuts import render
from .models import Post

def search(request):
    query = request.GET.get('q', '')
    posts = Post.objects.filter(
        Q(title__icontains=query) | Q(content__icontains=query)
    )
    return render(request, 'blog/search_results.html', {'query': query, 'posts': posts})
def post_list(request):
    posts = Post.objects.all()[:10]  
    recent_posts = Post.objects.all().order_by('-created_at')[:5]
    return render(request, 'blog/post_list.html', {'posts': posts, 'recent_posts': recent_posts})
def tag_posts(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)
    posts = Post.objects.filter(tags=tag)
    return render(request, 'blog/tag_posts.html', {'tag': tag, 'posts': posts})
from django.shortcuts import render
from .models import Comment
from .forms import CommentFormSet

def comment_view(request):
    if request.method == 'POST':
        formset = CommentFormSet(request.POST)
        if formset.is_valid():
            formset.save()
    else:
        formset = CommentFormSet(queryset=Comment.objects.none())
    
    return render(request, 'comments.html', {'formset': formset})
from django.shortcuts import render, redirect
from .forms import PostForm, PostImageFormset
from .models import Post, PostImage

def post_create(request):
    if request.method == 'POST':
        post_form = PostForm(request.POST)
        image_formset = PostImageFormset(request.POST, request.FILES)

        if post_form.is_valid() and image_formset.is_valid():
            post = post_form.save()
            for form in image_formset:
                image = form.save(commit=False)
                image.post = post
                image.save()
            return redirect('post_detail', post_id=post.id)
    else:
        post_form = PostForm()
        image_formset = PostImageFormset()

    return render(request, 'post_create.html', {'post_form': post_form, 'image_formset': image_formset})

