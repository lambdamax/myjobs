from django.db import models


class Index(models.Model):
    name = models.CharField(max_length=100)
    shop_id = models.CharField(max_length=100, null=True)
    remark = models.CharField(max_length=500, null=True)
    center = models.CharField(max_length=100, null=True)

    class Meta:
        db_table = 'metuan_index'

    def __repr__(self):
        return '%s-%s' % (self.id, self.name)


class Shop(models.Model):
    index = models.ForeignKey('Index', on_delete=models.DO_NOTHING, null=True)
    name = models.CharField(max_length=50)
    score = models.DecimalField(max_digits=2, decimal_places=1, default=0)
    comments = models.IntegerField(null=True)
    address = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=100, null=True)
    hours = models.CharField(max_length=100, null=True)
    ave_price = models.DecimalField(max_digits=10, decimal_places=1, null=True)
    url = models.CharField(max_length=200, null=True)

    class Meta:
        db_table = 'metuan_shop'

    def __repr__(self):
        return '%s-%s' % (self.id, self.name)


class Product(models.Model):
    name = models.CharField(max_length=50)
    shop = models.ForeignKey('Shop', on_delete=models.DO_NOTHING, related_name='products')

    class Meta:
        db_table = 'metuan_product'

    def __repr__(self):
        return '%s-%s' % (self.id, self.name)
