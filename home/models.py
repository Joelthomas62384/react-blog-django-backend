from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings





class categories(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    


class blog(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL,null=True, blank=True)
    category = models.ForeignKey(categories , on_delete=models.SET_NULL,null=True)
    content = RichTextField()
    date = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title[:5] + " - " + self.author.username 

