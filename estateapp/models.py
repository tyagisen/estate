from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


class HomeFeatures(models.Model):
    feature_name = models.CharField(max_length=100)
    total_feature = models.IntegerField(default=1, blank=True, null=True)


    def __str__(self):
        return self.feature_name


    class Meta:
        verbose_name_plural = "Home Features"

class Home(models.Model):
    name = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    date_built = models.DateTimeField()
    image = models.ImageField(upload_to='profile_pics')
    house_type = models.CharField(max_length=100)
    street_no = models.IntegerField()
    property_size = models.CharField(max_length=10, null=True)
    property_type = models.CharField(max_length=100, null=True)
    file = models.FileField(upload_to='property')
    features = models.ManyToManyField(HomeFeatures)

    def __str__(self):
        return self.address

