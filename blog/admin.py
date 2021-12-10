from django.contrib import admin

from .models import Post
from .models import Comment

admin.site.register(Post)

admin.site.register(Comment)


class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "name", "email", "body", "date_added")
    search_fields = ("name", "email", "post")
