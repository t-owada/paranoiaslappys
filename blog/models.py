from django.db import models
from datetime import datetime


class BlogData(models.Model):
    # Managing Blog Data
    Title = models.CharField(max_length=255)
    Author = models.CharField(max_length=255)
    Date = models.DateField(default=datetime.now().date(), blank=True)

    def __str__(self):
        return self.Title


# class BlogParagraph(models.Model):
#     BlogData = models.ForeignKey(BlogData, related_name='BlogParagraphs', on_delete=models)
#     Paragraph = models.TextField()
#
#     def __str__(self):
#         # return_string = join(self.BlogData, ' Paragraph id :', self.id)
#         # return return_string
#         return self.id
#
#
# class BlogImage(models.Model):
#     BlogParagraph = models.ForeignKey(BlogParagraph, related_name='BlogImages', on_delete=models)
#     Name = models.CharField(max_length=255)
#     Image = models.ImageField(upload_to='img/')
#
#     def __str__(self):
#         # return_string = join(self.BlogParagraph.BlogData, ' Paragraph id : ', self.BlogParagraph.id, ' Image id : ', self.id)
#         # return return_string
#         return self.id
