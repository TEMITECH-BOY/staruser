from django.db import models
from django.contrib.auth.models import User



# Create your models here.
GENDER_CHOICES=(
    ('M','Male'),
    ('F','Female'),

)
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    fullname= models.CharField(max_length=255)
    phone= models.CharField(max_length=13,blank=True, null=True)
    gender= models.CharField(max_length=50,choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='profile', default="profile/default.png",blank=True,null=True)
    created = models.DateTimeField(auto_now_add=False)


    def __str__(self):
        return self.fullname

   
