from django.db import models


# class ProductColorModel(models.Model):
#     code = models.CharField(max_length=7)


class ProductTagModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Taglar'


# class ProductModel(models.Model):
#     title = models.CharField(max_length=50)
#     short_description = models.TextField()
#     long_description = models.TextField()
#     price = models.FloatField()
#     discount = models.PositiveIntegerField(default=0)
#     main_image = models.ImageField(upload_to='products/')
#     tag = models.ManyToManyRel(ProductTagModel, related_name='products')
#
