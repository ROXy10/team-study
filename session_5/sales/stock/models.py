from django.db import models


class Сontractor(models.Model):
    name = models.CharField("название", max_length=256, blank=False)

    class Meta:
        verbose_name = "контрагент"
        verbose_name_plural = "контрагенты"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Coupons(models.Model):
    name = models.CharField("название", max_length=256, blank=False)
    price = models.DecimalField("цена", blank=False, max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = "купон"
        verbose_name_plural = "купоны"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Stock(models.Model):
    name = models.CharField("название", max_length=256, blank=False)
    period = models.DurationField("период", blank = False)
    client = models.OneToOneField('Сontractor', verbose_name="контрагент", null=True, blank=False, on_delete=models.SET_NULL)
    price = models.DecimalField("цена", blank=False, max_digits=12, decimal_places=2)
    coupon = models.OneToOneField('Coupons', verbose_name="купон", null=True, blank=False, on_delete=models.SET_NULL)
    discounts = models.IntegerField("процент скидки", blank=False, default=0)

    description = models.TextField("описание")
    comments = models.TextField("коментарий")

    class Meta:
        verbose_name = "скидка"
        verbose_name_plural = "скидки"
        ordering = ["name"]

    def __str__(self):
        return "%s %s" % (self.name, self.client)