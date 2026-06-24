from django.db import models
from django.contrib.auth.models import User   #for save information of end user like name,email,password

# Create your models here.
#aditional imformation using relation
class UserProfile(models.Model):  
    user = models.OneToOneField(User,on_delete=models.CASCADE)    #delete user profile willbe delete 
    phone = models.BigIntegerField()

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class Prediction(models.Model):  
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='predictions')    #delete user predictions willbe delete 
    N = models.FloatField() 
    P = models.FloatField() 
    K = models.FloatField() 
    temperature = models.FloatField() 
    humidity = models.FloatField() 
    ph = models.FloatField() 
    rainfall = models.FloatField()
    predicted_label = models.CharField(max_length=100) 
    created_at =models.DateTimeField(auto_now_add=True) 

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.user.username} -> {self.predicted_label}"
