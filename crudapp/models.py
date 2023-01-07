from django.db import models

class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phonenumber = models.CharField(max_length=255)
  image = models.ImageField(null=True, blank=True)
  priceperhour = models.DecimalField(max_digits=9, decimal_places=2)

def __str__(self):
    return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url