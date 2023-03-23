from django.db import models

# Create your models here.
l=(
    ('Tech','Tech'),
    ('IT','IT'),
    ('Health','Health'),
    ('Travelling','Travelling'),
)

class todo(models.Model):
    desc=models.CharField(max_length=260)
    category=models.CharField(max_length=300,choices=l,default='abc')
    date=models.DateField()
    markcompleted=models.BooleanField(default=False)
    def __str__(self):
        return self.category +" "+self.desc
    


