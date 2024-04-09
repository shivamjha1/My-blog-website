from django.db import models

# Create your models here.

class Author(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30,null=True)
    email=models.CharField(max_length=30,null=True)
    
    def __str__(self):
        return self.firstname+" "+self.lastname
class Tags(models.Model):
    caption=models.CharField(max_length=20)
        
class Blog(models.Model):
    title=models.CharField(max_length=50,null=False)
    image=models.CharField(max_length=50)
    excerpt=models.CharField(max_length=100)
    date=models.DateField()
    slug=models.SlugField(default="",blank=True, null=False,db_index=True)
    content=models.TextField(max_length=500)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name="blogs",null=True)
    tags=models.ManyToManyField(Tags,null=True)
    
    def __str__(self) -> str:
        return self.title