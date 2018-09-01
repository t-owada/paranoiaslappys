from django.db import models


class TopPageContent(models.Model):
    # Managing top page contents
    CopyText = models.CharField(max_length=255)
    MessageText = models.CharField(max_length=255)

    def __str__(self):
        return self.CopyText
