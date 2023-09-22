from django.db import models
from django.urls import reverse


# Create your models here.

    
class Product(models.Model):
    title = models.CharField(max_length=2000)
    description = models.CharField(max_length=2000)

    #create SEO friendly urls
    slug = models.SlugField()

    # The default manager.
    objects = models.Manager() # The default manager.


    def __str__(self):
        return self.title
    #build a url reverser to help us navigate
    def get_absolute_url(self):
        return reverse('product_detail',
                       args=[self.id, self.slug])
