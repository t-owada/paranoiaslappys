from django.db import models


class BlogData(models.Model):
    # Managing Blog Data
    Title = models.CharField(max_length=255)
    Author = models.CharField(max_length=255)
    Date = models.DateField(null=False)

    def __str__(self):
        return self.Title


class BlogParagraph(models.Model):
    BlogData = models.ForeignKey(BlogData, on_delete=models.CASCADE)
    ParagraphText = models.TextField()
    ParagraphImage = models.ImageField(null=True, blank=True, upload_to='img_blog/%Y/%m/%d')

    def __str__(self):
        return 'blog title : 「' + str(self.BlogData) + '」, paragraph id :' + str(self.id)
