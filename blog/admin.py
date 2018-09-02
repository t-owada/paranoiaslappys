from django.contrib import admin
from .models import BlogData, BlogParagraph


class ParagraphInline(admin.StackedInline):
    model = BlogParagraph
    extra = 5


class BlogDataAdmin(admin.ModelAdmin):
    fields = ['Title', 'Author', 'Date']
    inlines = [ParagraphInline]


admin.site.register(BlogData, BlogDataAdmin)
