from django.db import models

# Create your models here.

class Author(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30,null=True)
    email=models.CharField(max_length=30,null=True)
    picture=models.CharField(max_length=100,null=True)
    about=models.TextField(max_length=500,null=True)
    
    def __str__(self):
        return self.firstname+" "+self.lastname
class Tags(models.Model):
    caption=models.CharField(max_length=20)
    def __str__(self) -> str:
        return self.caption

    
                
class Blog(models.Model):
    title=models.CharField(max_length=50,null=False)
    image=models.ImageField(upload_to="images",null=True)
    excerpt=models.CharField(max_length=100)
    date=models.DateField()
    slug=models.SlugField(default="",blank=True, null=False,db_index=True)
    content=models.TextField(max_length=10000)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name="blogs",null=True)
    tags=models.ManyToManyField(Tags,null=True)
    
    def __str__(self) -> str:
        return self.title
    
    
class Comments(models.Model):
    user_name=models.CharField(max_length=100)
    user_email=models.EmailField(max_length=100)
    comment_text=models.TextField(max_length=500)
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE,related_name="blog",null=True)
    