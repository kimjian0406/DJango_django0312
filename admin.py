from django.contrib import admin
from .models import Post, PostImage, Comment, Tag, PostTag

admin.site.register(Post)
admin.site.register(PostImage)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(PostTag)
