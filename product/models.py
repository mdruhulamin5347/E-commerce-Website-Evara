from django.db import models
from django.utils.text import slugify

class Category(models.Model):
    title = models.CharField(max_length=50, null=True, blank=True)
    logo = models.ImageField(upload_to='category/', null=True, blank=True)
    slug = models.SlugField(max_length=50, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)
    def __str__(self):
        return self.title

class SubCategory(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name = 'subcategories')
    def __str__(self):
        return self.title

class Brand(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Color(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Size(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products/')
    image1 = models.ImageField(upload_to='products/', null=True, blank=True)
    image2 = models.ImageField(upload_to='products/', null=True, blank=True)
    image3 = models.ImageField(upload_to='products/', null=True, blank=True)
    image4 = models.ImageField(upload_to='products/', null=True, blank=True)
    image5 = models.ImageField(upload_to='products/', null=True, blank=True)
    image6 = models.ImageField(upload_to='products/', null=True, blank=True)
    image7 = models.ImageField(upload_to='products/', null=True, blank=True)
    image8 = models.ImageField(upload_to='products/', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    product_code = models.CharField(max_length=50)
    brand_name = models.ForeignKey(Brand, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
    new_price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_percentage = models.PositiveIntegerField()
    description = models.TextField()
    warranty_year = models.PositiveSmallIntegerField()
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    is_favorite = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    is_popular = models.BooleanField(default=False)
    is_newadded = models.BooleanField(default=False)
    SKU = models.CharField(max_length=50)
    tags = models.ManyToManyField(Tag)
    available_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.title
    



class carusol_model(models.Model):
    title = models.CharField(max_length=50)
    title2 = models.CharField(max_length=50)
    title3 = models.CharField(max_length=50)
    title4 = models.CharField(max_length=50)
    image = models.ImageField(upload_to='carusol/' , null=True,blank=True)
    def __str__(self):
        return self.title