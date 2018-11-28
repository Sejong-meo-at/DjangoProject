from django.contrib import admin
from .models import WordPost, Comment, WordBook

# Register your models here.
admin.site.register(WordPost)
admin.site.register(Comment)
admin.site.register(WordBook)
