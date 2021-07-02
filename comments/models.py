from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

#database model for handling pages
class Page(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    slug = models.CharField(max_length=300)

    def __str__(self):
        return self.title

#database model for threaded comments
class UserComment(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    comment = models.TextField(max_length=300)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return self.comment[0:20]

