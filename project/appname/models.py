from django.db import models
 
class Member(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=120,default=None, blank=True, null=True)
    last_name = models.CharField(max_length=120,default=None, blank=True, null=True)
    phone_number = models.CharField(max_length=120,default=None, blank=True, null=True)
    email = models.CharField(max_length=120,default=None, blank=True, null=True)
    role = models.CharField(default='regular', max_length=120, editable=True)
 
    class Meta:
        verbose_name = "Member"
        verbose_name_plural = "Members"
 
    def __unicode__(self):
        return self.name
 
