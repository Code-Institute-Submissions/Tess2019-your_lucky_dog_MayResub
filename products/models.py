from django.db import models


class Categories(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
<<<<<<< HEAD
    products = models.ManyToManyField('Product')
=======
    products =models.ManyToManyField('Product')
>>>>>>> 1a1b4efd67ff8316eda7485806411a1a71bbffe5

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
<<<<<<< HEAD
    category = models.ManyToManyField('category')
=======
    categories = models.ManyToManyField('Categories')
>>>>>>> 1a1b4efd67ff8316eda7485806411a1a71bbffe5
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    designer = models.CharField(max_length=254, null=True, blank=True)
    images_url = models.URLField(max_length=1024, null=True, blank=True)
    images = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name