from django.db import models
# passward and user name -'a' and 'a'
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc =  models.TextField()
    date=  models.DateField()
    def __str__(self):
        return self.name
class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    desc = models.TextField()
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    