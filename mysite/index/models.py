from django.db import models


class ImgsAnalytics(models.Model):
    title = models.CharField(max_length=150)
    cover = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class ParcedData(models.Model):
    name = models.CharField(max_length=60, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    key_skills = models.TextField(blank=True, null=True)
    employer_name = models.CharField(max_length=60, blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    currency = models.CharField(max_length=10, blank=True, null=True)
    area_city = models.CharField(max_length=30, blank=True, null=True)
    published_at = models.DateField(blank=True, null=True)
    # python manage.py makemigrations
    # python manage.py migrate
