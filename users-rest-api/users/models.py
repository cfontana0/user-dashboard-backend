from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

@python_2_unicode_compatible
class Country(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=55)
    class Meta:
        verbose_name_plural = 'countries'
    def __str__(self):
        return self.name

@python_2_unicode_compatible
class UserFamily(models.Model):
    id = models.AutoField(primary_key=True)
    family_name = models.CharField(max_length=55)
    class Meta:
        verbose_name_plural = 'families'
    def __str__(self):
        return self.family_name

@python_2_unicode_compatible
class UserProfile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='userprofile_user')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='userprofile_country', null=True)
    family = models.ForeignKey(UserFamily, on_delete=models.CASCADE, related_name='members', null=True)
    class Meta:
        verbose_name_plural = 'profiles'
    def __str__(self):
          return self.user.first_name + ' ' + self.user.last_name + ' (' + unicode(self.user) + ')'

@python_2_unicode_compatible
class UserActivity(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='activity_user', null=True)
    browser = models.CharField(max_length=55, null=True)
    os = models.CharField(max_length=55, null=True)
    action = models.CharField(max_length=200, null=True)
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = 'activities'
    def __str__(self):  
          return unicode(self.user) + ' - ' + self.date.strftime('%s %s' % ('%Y-%m-%d' , '%H:%M:%S')) + ' - ' + self.os + ' ' + self.browser