from django.db import models
from django.utils.timezone import now

class Blog(models.Model) :
    objects = models.Manager()
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField(default="")
    imgurl = models.TextField(default="")
    def __str__(self) :
        return self.title
