from django.db import models
from django.conf import settings

choices=(
    ('publish','Publish'),
('draft','draft')
)


 
#...
class BlogAuthor(models.Model):
    author     =       models.ForeignKey(settings.AUTH_USER_MODEL , on_delete=models.CASCADE)
    image      =       models.ImageField()
    bio        =       models.TextField(help_text='Write something about you')

    def __str__(self):
        return self.author.username
        


class Category(models.Model):
    Name      =       models.CharField(max_length=500)
    slug      =       models.CharField(max_length=500)
    def __str__(self):
        return self.Name





    

class code_post(models.Model):
    catagory    =       models.ForeignKey(Category,on_delete=models.CASCADE)
    sub_category=       models.CharField(max_length=100)
    author      =       models.ForeignKey(BlogAuthor, on_delete=models.CASCADE, null=True)
    title       =       models.CharField(max_length=1000)
    slug        =       models.CharField(max_length=1000)
    publish     =       models.CharField(max_length=100,choices=choices)
    image       =       models.ImageField(blank=True)
    description =       models.TextField()
    created_at  =       models.DateTimeField(auto_now=True)
    updated     =       models.DateTimeField(auto_now=True)

    
    class Meta:
        ordering = ["-created_at","-updated"]

    def __str__(self):
        return self.title

class example(models.Model):
    code_post    =       models.ForeignKey(code_post,on_delete=models.CASCADE)
    author      =       models.CharField(max_length=100)
    title       =       models.CharField(max_length=1000,blank=True)
    image       =       models.ImageField(blank=True)
    links       =       models.URLField(blank=True)
    madewith    =       models.CharField(max_length=100,blank=True)
    description =       models.TextField(blank=True)
    compatible  =       models.CharField(max_length=100,blank=True)
    responsive  =       models.CharField(max_length=100,blank=True)
    dependencies=       models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.title
   


