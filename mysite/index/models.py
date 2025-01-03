from django.db import models


class ImgsAnalytics(models.Model):
    title = models.CharField(max_length=150)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title
