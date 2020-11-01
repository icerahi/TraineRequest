from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.views.generic import DetailView
from smart_selects.db_fields import ChainedForeignKey


class Designation(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "     Designations"



class Zone(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "    Zones"

class Branch(models.Model):
    zone = models.ForeignKey(Zone,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '   Branches'



class Training_Title(models.Model):
    name = models.CharField(max_length=400)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '  Training Titles'

class Profile(models.Model):
    user        = models.OneToOneField(User,unique=True,related_name='profile',on_delete=models.CASCADE)
    designation = models.ForeignKey(Designation,blank=True,null=True,on_delete=models.SET_NULL)
    zone        = models.ForeignKey(Zone,blank=True,null=True,on_delete=models.SET_NULL)
    branch      = ChainedForeignKey(Branch,blank=True,null=True,chained_field='zone',chained_model_field='zone',
                                    show_all=False,auto_choose=True,sort=True)

    created     = models.DateTimeField(auto_now_add=True)

    ChangePass  = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = " Profiles"

@receiver(post_save,sender=User)
def post_save_user(instance,created,*args,**kwargs):
    if created:
        new_profile = Profile.objects.get_or_create(user=instance)



class TraineRequest(models.Model):
    user          = models.ForeignKey(User,on_delete=models.CASCADE)
    employee_id   = models.IntegerField()
    employee_name = models.CharField(max_length=100)
    # email         = models.EmailField()
    designation   = models.ForeignKey(Designation,on_delete=models.CASCADE)
    title         = models.ForeignKey(Training_Title,on_delete=models.CASCADE)
    zone          = models.ForeignKey(Zone,on_delete=models.CASCADE)
    branch = ChainedForeignKey(Branch, blank=True, null=True, chained_field='zone', chained_model_field='zone',
                               show_all=False, auto_choose=True, sort=True)
    created        = models.DateTimeField(auto_now_add=True)

    def __str__(self):

        return self.employee_name

    class Meta:
        ordering = ['designation']
        verbose_name_plural = 'Training Requests'


