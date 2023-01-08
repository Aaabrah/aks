from django.db import models


class ContactMessageModel(models.Model):
    name = models.CharField(max_length=40)
    company_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    lavozim = models.CharField(max_length=40)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'


class BannerModel(models.Model):
    collection = models.CharField(max_length=155)
    title = models.CharField(max_length=255)
    description = models.TextField()
    banner_image = models.ImageField(upload_to='banners/')
    banner_url = models.CharField(max_length=255)
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'banner'
        verbose_name_plural = 'bannerlar'


