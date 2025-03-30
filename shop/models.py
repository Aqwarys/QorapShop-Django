from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from decimal import Decimal


class Category(models.Model):
    name = models.CharField(max_length=200)
    sub_category = models.ForeignKey(
        'self', on_delete=models.CASCADE, related_name='sub_categories', null=True, blank=True
    )
    is_sub = models.BooleanField(default=False)
    slug = models.SlugField(max_length=2200,
                            unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("shop:category", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def get_sub_categories(self):
        return self.sub_categories.all()

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    image = models.ImageField(upload_to='products/product_images')
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['name']),
            models.Index(fields=['date_created']),
        ]
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def installment(self):
        return Decimal(self.price/24).quantize(Decimal('.01'))
