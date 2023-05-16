from django.db import models


class DeviceType(models.Model):
    type_name = models.CharField(max_length=150, verbose_name='Название')

    def __str__(self):
        return self.type_name


class Manufacture(models.Model):
    name = models.CharField(max_length=150, verbose_name='Производитель')
    country = models.CharField(max_length=90, verbose_name='Страна производства')

    def __str__(self):
        return f"{self.name}-{self.country}"


class Device(models.Model):
    id_type = models.ForeignKey(DeviceType, blank=True, null=True, verbose_name='Тип устройства',
                                on_delete=models.CASCADE)
    manufacture = models.ForeignKey(Manufacture, blank=True, null=True, verbose_name='Тип устройства',
                                    on_delete=models.CASCADE)
    inventory_number = models.IntegerField(verbose_name='Номер')
    serial_number = models.IntegerField(verbose_name='serial_number')
    device_name = models.CharField(max_length=120, verbose_name='Название устр')
    installing_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.device_name


class Settings(models.Model):
    name = models.ForeignKey(DeviceType, blank=True, null=True, verbose_name='Тип устройства', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Properties(models.Model):
    id_device = models.ForeignKey(Device, blank=True, null=True, on_delete=models.CASCADE)
    id_settings = models.ForeignKey(Settings, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id_device}-{self.id_settings}"


class Role(models.Model):
    name = models.CharField(verbose_name='Название должности', max_length=120)
    desc = models.TextField(verbose_name='Описание', blank=True, null=True)

    def __str__(self):
        return self.name


class Deportment(models.Model):
    name = models.CharField(verbose_name='Название отдела', max_length=120)

    def __str__(self):
        return self.name


class Employee(models.Model):
    id_deportment = models.ForeignKey(Deportment, on_delete=models.CASCADE)
    personal_number = models.IntegerField(verbose_name='Идетификационный номер')
    first_name = models.CharField(max_length=150, verbose_name='Фамилия')
    last_name = models.CharField(max_length=150, verbose_name='Имя')
    patronymic = models.CharField(max_length=150, verbose_name='Отчество', blank=True)
    role = models.ForeignKey(Role, blank=True, null=True, verbose_name='Должность', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name}-{self.last_name}"
