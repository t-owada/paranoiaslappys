from django.db import models
from datetime import datetime
from django.utils import timezone


class BlogData(models.Model):
    # Managing Blog Data
    Title = models.CharField(max_length=255, null=False)
    Author = models.CharField(max_length=255, null=False)
    Date = models.DateField(null=False)

    def __str__(self):
        return self.Title


class BlogParagraph(models.Model):
    BlogData = models.ForeignKey(BlogData, on_delete=models.CASCADE)
    ParagraphText = models.TextField()
    ParagraphImage = models.ImageField(null=True, blank=True, upload_to='img/%Y/%m/%d')

    def __str__(self):
        return 'blog title : 「' + str(self.BlogData) + '」, paragraph id :' + str(self.id)
