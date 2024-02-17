from django.db import models
from django.utils.text import slugify


# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=50)  # fild Ã˜Â³Ã˜ÂªÃ™Ë†Ã™â€ 
    family = models.CharField(max_length=50)
    age = models.IntegerField()
    is_activate = models.BooleanField()

class ProductCategory(models.Model):
    title = models.CharField(max_length=300,verbose_name='عنوان')
    url_title = models.CharField(max_length=300,verbose_name='عنوان در Url')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='دسته بندی'
        verbose_name_plural='دسته بندی ها'

class ProductInformation(models.Model):
    color=models.CharField(max_length=100,verbose_name='رنگ')
    size=models.CharField(max_length=100,verbose_name='سایز')


    def __str__(self):
        return f'{self.color}-----{self.size}'

    class Meta:
        verbose_name='اطلاعات تکمیلی'
        verbose_name_plural='لیست اطلاعات تکمیلی'

class ProductTag(models.Model):
    tag=models.CharField(max_length=200,verbose_name='عنوان تگ')
    def __str__(self):
        return self.tag
    class Meta:
        verbose_name='تگ محصول'
        verbose_name_plural='تگ های محصولات'

class product(models.Model):
    product_tag=models.ManyToManyField(ProductTag,verbose_name='تگ محصول')
    category=models.ForeignKey(ProductCategory,on_delete=models.CASCADE,verbose_name='دسته بندی',null=True)
    product_info=models.OneToOneField(ProductInformation,on_delete=models.CASCADE,null=True,verbose_name='اطلاعات تکمیلی',blank=True)
    title = models.CharField(max_length=100, verbose_name='عنوان محصول')
    price = models.IntegerField(verbose_name='قیمت')
    description = models.CharField(max_length=500, verbose_name='توضیحات')
    is_active = models.BooleanField(verbose_name='فعال/غیرفعال')
    slug = models.SlugField(default='', null=False, db_index=True, verbose_name='url عنوان در',unique=True)
    image= models.ImageField(upload_to='blogs/static/blogs/images',null=True,blank=True, verbose_name='عکس محصول')
    def save(self,*args,**kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self):
        return f'{self.title} --- {self.price}'

    class Meta:
        verbose_name='محصول'
        verbose_name_plural='محصولات'