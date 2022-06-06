from django.db import models


class WebsiteCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    date_added = models.DateTimeField()
    date_updated = models.DateTimeField()
    count = models.IntegerField()

    class Meta:
        db_table = 'website_category'

    def __str__(self):
        return self.name


class Website(models.Model):
    url = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    meta_description = models.CharField(max_length=50)
    alexa_rank = models.IntegerField()
    category = models.ForeignKey(WebsiteCategory, on_delete=models.CASCADE)
    date_added = models.DateTimeField()
    date_updated = models.DateTimeField()

    class Meta:
        db_table = 'website'

    def __str__(self):
        return self.title


class WebPage(models.Model):
    website = models.ForeignKey(Website, on_delete=models.CASCADE)
    URL = models.CharField(max_length=50, unique=True)
    date_added = models.DateTimeField()
    date_updated = models.DateTimeField()
    title = models.CharField(max_length=50)
    meta_description = models.CharField(max_length=50)

    class Meta:
        db_table = 'webpage'

    def __str__(self):
        return self.title
