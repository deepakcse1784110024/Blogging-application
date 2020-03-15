from django.db import models
from datetime import date

# Create your models here.

class User(models.Model):
    username=models.CharField('username',max_length=100)
    email=models.CharField('User email',max_length=100)
    password=models.CharField('User password',max_length=20)



class Blog(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='images/')
    title=models.CharField('Post title',max_length=100)
    description=models.TextField('Post Description')
    posted_date=models.DateField(default=date.today)
    good_name=models.CharField('Good name',max_length=100)

class Coment(models.Model):

    message=models.TextField('Message')
    date_comment = models.DateField(default=date.today)
    user_id= models.ForeignKey(User,on_delete=models.CASCADE)
    post_id= models.ForeignKey(Blog,on_delete=models.CASCADE)

