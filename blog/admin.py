from django.contrib import admin
from . models import Author, Post, Tag, Comment


class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "date", "tags")
    list_display = ("title", "author", "date",)
    prepopulated_fields = {"slug": ("title",)}


class CommentAdmin(admin.ModelAdmin):
    list_display = ("user_name", "post")

admin.site.register(Author)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment, CommentAdmin)
