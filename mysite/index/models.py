from django.db import models


def get_currencies():
    return [
        ("DMN", "Востребованность"),
        ("GEO", "География"),
    ]


class GeneralSkillsAnalytics(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    year = models.IntegerField(verbose_name="Год")
    image = models.ImageField(upload_to='images/', verbose_name="График")
    text = models.TextField(default="", verbose_name="Таблица html")

    class Meta:
        ordering = ["-year"]

    def __str__(self):
        return self.title


class FiltredSkillsAnalytics(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    year = models.IntegerField(verbose_name="Год")
    image = models.ImageField(upload_to='images/', verbose_name="График")
    text = models.TextField(default="", verbose_name="Таблица html")

    class Meta:
        ordering = ["-year"]

    def __str__(self):
        return self.title


class GeneralAnalytics(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    image = models.ImageField(upload_to='images/', verbose_name="График")
    text = models.TextField(default="", verbose_name="Таблица html")

    def __str__(self):
        return self.title


class FiltredAnalytics(models.Model):
    title = models.CharField(max_length=150,  verbose_name="Заголовок")
    image = models.ImageField(upload_to='images/', verbose_name="График")
    text = models.TextField(default="", verbose_name="Таблица html")
    id_page = models.CharField(
        default="INDX", max_length=5, choices=get_currencies)

    def __str__(self):
        return self.title
