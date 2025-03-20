
from django.shortcuts import render
from .models import Post, Tag

def post_list(request):
    tags = Tag.objects.all()  
    posts = Post.objects.all()  

    tag_filter = request.GET.get('tag') 
    if tag_filter:
        posts = posts.filter(tags__name=tag_filter)  

    return render(request, 'post_list.html', {'posts': posts, 'tags': tags})

posts = posts.prefetch_related('tags')

from django.db.models import Count

def post_list(request):
    tags = Tag.objects.annotate(num_posts=Count('posts'))
    posts = Post.objects.all()

    tag_filter = request.GET.get('tag')
    if tag_filter:
        posts = posts.filter(tags__name=tag_filter)

    return render(request, 'post_list.html', {'posts': posts, 'tags': tags})

def post_list(request):
    search_query = request.GET.get('search', '') 
    posts = Post.objects.all()

    if search_query:
        posts = posts.filter(title__icontains=search_query)
    tag_filter = request.GET.get('tag')
    if tag_filter:
        posts = posts.filter(tags__name=tag_filter)

    tags = Tag.objects.all()
    return render(request, 'post_list.html', {'posts': posts, 'tags': tags, 'search_query': search_query})
def post_list(request):
    search_query = request.GET.get('search', '')
    posts = Post.objects.all().prefetch_related('tags')  # 태그를 미리 가져와서 쿼리 최적화

    if search_query:
        posts = posts.filter(title__icontains=search_query)

    tag_filter = request.GET.get('tag')
    if tag_filter:
        posts = posts.filter(tags__name=tag_filter)

    tags = Tag.objects.all()
    return render(request, 'post_list.html', {'posts': posts, 'tags': tags, 'search_query': search_query})
# views.py
from django.shortcuts import render, redirect
from .models import Post, Tag
from nltk.corpus import stopwords

# 자동 태그 생성 함수
def generate_tags_from_content(content):
    stop_words = set(stopwords.words('english'))
    words = content.split()
    tags = [word for word in words if word.lower() not in stop_words]
    return tags

# 게시글 작성 뷰
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        # 게시글 저장
        post = Post.objects.create(title=title, content=content)

        # 자동 태그 생성
        tags = generate_tags_from_content(content)

        # 태그 추가 (이미 있는 태그만 추가하고, 없는 태그는 새로 생성)
        for tag_name in tags:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            post.tags.add(tag)

        return redirect('post_list')

    return render(request, 'create_post.html')

# 게시글 수정 뷰
def edit_post(request, post_id):
    post = Post.objects.get(id=post_id)

    if request.method == 'POST':
        post.title = request.POST.get('title')
        post.content = request.POST.get('content')
        post.save()

        # 자동 태그 생성
        tags = generate_tags_from_content(post.content)

        # 기존 태그 제거 후 새 태그 추가
        post.tags.clear()  # 기존 태그 제거
        for tag_name in tags:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            post.tags.add(tag)

        return redirect('post_list')

    return render(request, 'edit_post.html', {'post': post})

from django.shortcuts import render, redirect
from .models import Post, Tag
from .utils import generate_tags_from_conten
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')

        # 게시글 저장
        post = Post.objects.create(title=title, content=content)

        # 자동 태그 생성
        tags = generate_tags_from_content(content)

        # 태그 추가
        for tag_name in tags:
            tag, created = Tag.objects.get_or_create(name=tag_name)  # 태그가 없으면 생성
            post.tags.add(tag)  # 게시글에 태그 추가

        return redirect('post_list')  # 게시글 목록 페이지로 리디렉션

    return render(request, 'create_post.html')
def post_list(request):
    posts = Post.objects.all()

    return render(request, 'post_list.html', {'posts': posts})
from django.shortcuts import render, get_object_or_404
from .models import Post, Tag

def posts_by_tag(request, tag_name):
    tag = get_object_or_404(Tag, name=tag_name)  # 태그가 없으면 404 에러 반환
    posts = tag.posts.all()  # 해당 태그가 포함된 게시글만 가져오기
    return render(request, 'post_list.html', {'posts': posts, 'selected_tag': tag_name})
# views.py
from django.shortcuts import render
from .models import Post, Tag

def post_list(request):
    tag_query = request.GET.get('tag', '')  # 검색된 태그 가져오기
    if tag_query:
        posts = Post.objects.filter(tags__name__icontains=tag_query)  # 해당 태그를 포함하는 게시글 검색
    else:
        posts = Post.objects.all()  # 모든 게시글 반환
    return render(request, 'post_list.html', {'posts': posts, 'tag_query': tag_query})

from django.shortcuts import render
from .models import Post, Tag

def posts_by_tag(request, tag_name):
    tag = Tag.objects.filter(name=tag_name).first()  # 해당 태그 찾기
    if tag:
        posts = tag.posts.all()  # 해당 태그가 포함된 게시글 가져오기
    else:
        posts = Post.objects.none()  # 태그가 없으면 빈 리스트

    return render(request, 'blog/post_list.html', {'posts': posts, 'tag_name': tag_name})
from django.shortcuts import render
from .models import Post

def search_posts(request):
    query = request.GET.get('q', '')  # 검색어 가져오기
    posts = Post.objects.filter(title__icontains=query) | Post.objects.filter(content__icontains=query)  # 제목 또는 내용에 검색어 포함된 글 찾기
    return render(request, 'blog/post_list.html', {'posts': posts, 'query': query})
from django.shortcuts import render
from .models import Post

def posts_by_tag(request, tag_name):
    posts = Post.objects.filter(tags__name=tag_name)  # 해당 태그가 포함된 게시글 필터링
    return render(request, 'blog/post_list.html', {'posts': posts, 'tag_name': tag_name})

