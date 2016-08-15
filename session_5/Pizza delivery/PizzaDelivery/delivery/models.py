from django.db import models


class Pizza(models.Model):
    name = models.CharField("название", max_length=256, blank=False)
    price = models.DecimalField("цена", blank=False, max_digits=12, decimal_places=2)
    description = models.TextField("описание")
    photo = models.ImageField("фотография", upload_to="houses/photos", default="", blank=True)

    class Meta:
        verbose_name = "пица"
        verbose_name_plural = "пицы"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Courier(models.Model):
    name = models.CharField("Имя", max_length=256, blank=False)

    class Meta:
        verbose_name = "курьер"
        verbose_name_plural = "курьеры"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Client(models.Model):
    first_name = models.CharField("Имя", max_length=256, blank=False)
    last_name = models.CharField("Фамилия", max_length=256, blank=False)
    client_phone = models.ForeignKey('Phone', verbose_name="телефон", blank=True, null=True, on_delete=models.PROTECT)
    client_address = models.ForeignKey('Address', verbose_name="адрес", blank=True, null=True, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "клиент"
        verbose_name_plural = "клиенты"
        ordering = ["last_name"]

    def __str__(self):
        return "%s %s" % (self.last_name, self.first_name)


class Phone(models.Model):
    owner = models.OneToOneField('Client', verbose_name="клиент", blank=True, null=True, on_delete=models.SET_NULL)
    phone = models.CharField("телефон", max_length=256, blank=False)

    class Meta:
        verbose_name = "телефон"
        verbose_name_plural = "телефоны"
        ordering = ["owner"]

    def __str__(self):
        return "%s %s" % (self.owner, self.phone)


class Address(models.Model):
    owner = models.OneToOneField('Client', verbose_name="клиент", blank=True, null=True, on_delete=models.SET_NULL)
    address = models.CharField("адрес", max_length=512, blank=False)

    class Meta:
        verbose_name = "адрес"
        verbose_name_plural = "алреса"
        ordering = ["owner"]

    def __str__(self):
        return "%s %s" % (self.owner, self.address)


class Bonus(models.Model):
    owner = models.OneToOneField('Client', verbose_name="клиент", blank=True, null=True, on_delete=models.SET_NULL)
    amount_order = models.IntegerField("количество заказов", blank=False, default=0)
    cash_back = models.DecimalField("возврат", blank=False, max_digits=12, decimal_places=2, default=0)

    class Meta:
        verbose_name = "бонус"
        verbose_name_plural = "бонусы"
        ordering = ["owner"]

    def __str__(self):
        return "%s amount order=%s cash back=%s" % (self.owner, self.amount_order, self.cash_back)


class Order(models.Model):
    date_time = models.DateTimeField(auto_now=False, auto_now_add=False, blank=False)
    client = models.OneToOneField('Client', verbose_name="клиент", blank=False, null=True, on_delete=models.SET_NULL)
    courier = models.OneToOneField('Courier', verbose_name="курьер", blank=False, null=True, on_delete=models.SET_NULL)
    address = models.OneToOneField('Address', verbose_name="адрес", blank=False, null=True, on_delete=models.SET_NULL)
    order_table = models.ForeignKey('OrderTable', verbose_name="табличная часть", blank=False, null=True,
                                    on_delete=models.PROTECT, related_name='order_table')

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ["date_time"]

    def __str__(self):
        return "%s %s %s" % (self.date_time, self.id, self.client)


class OrderTable(models.Model):
    order = models.OneToOneField('Order', verbose_name="заказ", blank=True, null=True, on_delete=models.SET_NULL)
    pizza = models.OneToOneField('Pizza', verbose_name='пица', blank=False, null=True, on_delete=models.SET_NULL)
    amount = models.IntegerField("количество", blank=False)
    price = models.DecimalField("цена", blank=False, max_digits=12, decimal_places=2, default=0)
    sum = models.DecimalField("сумма", blank=False, max_digits=12, decimal_places=2, default=0)

    class Meta:
        verbose_name = "Таблична часть заказа"
        verbose_name_plural = "Табличные части заказа"
        ordering = ["order"]

    def __str__(self):
        return "%s" % (self.order)
