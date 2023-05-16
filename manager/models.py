from django.db import models


class DeviceType(models.Model):
    """Модель описывающие типы устройств"""
    type_name = models.CharField(max_length=150, verbose_name='Название')

    class Meta:
        verbose_name = "Тип устройств"
        verbose_name_plural = "Типы устройства"

    def __str__(self):
        return self.type_name


class Manufacture(models.Model):
    """Модель описывающя производителя"""

    name = models.CharField(max_length=150, verbose_name='Производитель')
    country = models.CharField(max_length=90, verbose_name='Страна производства')

    class Meta:
        verbose_name = "Производитель"
        verbose_name_plural = "Производители"

    def __str__(self):
        return f"{self.name}-{self.country}"


class Device(models.Model):
    """Модель описывающие структуру устройства,серийный номер"""

    id_type = models.ForeignKey(DeviceType, blank=True, null=True, verbose_name='Тип устройства',
                                on_delete=models.CASCADE)
    manufacture = models.ForeignKey(Manufacture, blank=True, null=True, verbose_name='Тип устройства',
                                    on_delete=models.CASCADE)
    inventory_number = models.IntegerField(verbose_name='Номер')
    serial_number = models.IntegerField(verbose_name="Серийный номер")
    device_name = models.CharField(max_length=120, verbose_name='Название устр')
    installing_date = models.DateTimeField(auto_now=True, verbose_name="Дата установки")

    class Meta:
        verbose_name = "Устройства"
        verbose_name_plural = "Устройство"

    def __str__(self):
        return self.device_name


class Settings(models.Model):
    """Модель описывающий структуру настройки"""

    name = models.ForeignKey(DeviceType, blank=True, null=True, verbose_name='Тип устройства', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Настройка"
        verbose_name_plural = "Настройки"

    def __str__(self):
        return self.name


class Properties(models.Model):
    """Модель описывающая свойства"""

    id_device = models.ForeignKey(Device, blank=True, null=True, on_delete=models.CASCADE)
    id_settings = models.ForeignKey(Settings, blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Свойства"
        verbose_name_plural = "Свойство"

    def __str__(self):
        return f"{self.id_device}-{self.id_settings}"


class Role(models.Model):
    """Модель описывающий должности"""

    name = models.CharField(verbose_name='Название должности', max_length=120)
    desc = models.TextField(verbose_name='Описание', blank=True, null=True)

    class Meta:
        verbose_name = "Должность"
        verbose_name_plural = "Должности"

    def __str__(self):
        return self.name


class Deportment(models.Model):
    """Модель описываюший структуру отдела"""

    name = models.CharField(verbose_name='Название отдела', max_length=120)

    class Meta:
        verbose_name = "Отдел"
        verbose_name_plural = "Отделы"

    def __str__(self):
        return self.name


class Employee(models.Model):
    """Модель описывающий структуру сотрудника"""

    id_deportment = models.ForeignKey(Deportment, on_delete=models.CASCADE)
    personal_number = models.IntegerField(verbose_name='Идентификационный номер')
    first_name = models.CharField(max_length=150, verbose_name='Фамилия')
    last_name = models.CharField(max_length=150, verbose_name='Имя')
    patronymic = models.CharField(max_length=150, verbose_name='Отчество', blank=True)
    role = models.ForeignKey(Role, blank=True, null=True, verbose_name='Должность', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"

    def __str__(self):
        return f"{self.first_name}-{self.last_name}"
