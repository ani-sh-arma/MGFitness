from django.db import models
from django.contrib.auth.models import User

from datetime import date

  
class member(models.Model):

    card_no = models.IntegerField()
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE , default=0)
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=255)
    weight = models.IntegerField()
    height = models.FloatField()
    blood_groups = models.CharField(max_length=3)
    biceps = models.CharField(max_length=10 , default="")
    
    join_date = models.DateField(default=date.today)
    end_date = models.DateField()

    def save(self, *args, **kwargs):
        if not self.join_date:
            self.join_date = date.today()
        super().save(*args, **kwargs)


    def __str__(self):
        return f"{self.name}  ||  {self.card_no}"
    

    
    def get_current_user(user):
        try:
            return member.objects.get(user=user)
        except member.DoesNotExist:
            return None

# Create your models here.
