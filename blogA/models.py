from django.db import models
from django.utils.timezone import now

class Blog(models.Model) :
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    img = models.ImageField(blank=True)
    def __str__(self) :
        return self.title

    def summary(self) :
        return self.body[:100]