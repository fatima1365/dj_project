from django.db import models

# Create your models here.
class ContactUs(models.Model):
    title = models.CharField(max_length=300,verbose_name='عنوان')
    email = models.EmailField(max_length=300,verbose_name='ایمیل')
    name = models.CharField(max_length=200,verbose_name='نام')
    family_name = models.CharField(max_length=300, verbose_name='نام خانوادگی')
    message=models.TextField(max_length=350,verbose_name='متن پیام')
    created_data=models.DateField(verbose_name='تاریخ ایجاد')
    is_read_admin = models.BooleanField(default=False,verbose_name='خوانده شده توسط ادمین')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'راه های تماس با ما'




