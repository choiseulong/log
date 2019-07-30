from django.db import models
from django.utils.timezone import now

class Blog(models.Model) :
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField(default="")
    imgurl = models.TextField(default="")
    def __str__(self) :
        return self.title

    def summary(self) :
        return self.body[:100]
class Visitor(models.Model) :
    visitor_name = models.CharField(max_length=20)
    visitor_contents = models.TextField(default="")
    def __str__(self) :
        return self.visitor_name