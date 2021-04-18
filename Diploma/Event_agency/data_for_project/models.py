from django.db import models

# Create your models here.

class service(models.Model):
    service = models.CharField('Услуги', max_length=50, default='')
    img_service1 = models.ImageField('Изображение услуги', upload_to='static/data_for_project/img/img_goods', blank=True)
    img_service2 = models.ImageField('Изображение услуги', upload_to='static/data_for_project/img/img_goods', blank=True)
    img_service3 = models.ImageField('Изображение услуги', upload_to='static/data_for_project/img/img_goods', blank=True)
    service_name = models.CharField('Название услуги', max_length=50, default='')
    service_description = models.TextField('Описание услуг')

    def __str__(self):
        return self.service_name

    def get_absolute_url(self):
        return f'/admin_area_product{self.id}'


    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class review (models.Model):
    u_name = models.CharField('Имя', max_length=50, default='')
    u_surname = models.CharField('Фамилия', max_length=50, default='')
    review = models.TextField('Отзыв')

    def __str__(self):
        return self.u_name

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

class service_cost (models.Model):
    id_service = models.ForeignKey(service, on_delete=models.CASCADE)
    service_name = models.TextField('Название услуги')
    service_cost_min = models.TextField('Стоимость 30мин')
    service_cost_base = models.TextField('Стоимость 60мин')
    service_cost_max = models.TextField('Стоимость 90мин')

    def __str__(self):
        return f'{self.service_name}'

    def get_absolute_url(self):
        return f'/admin_area_cost{self.id}'

    class Meta:
        verbose_name = 'Цена'
        verbose_name_plural = 'Цены'

class fast_online_order (models.Model):
    name = models.CharField('Имя', max_length=50, default='')
    phone = models.CharField('Телефон', max_length=50, default='')
    date = models.DateTimeField('Дата и время праздника')
    number_children = models.CharField('Колличество детей', max_length=50, default='')
    hero = models.CharField('Герой', max_length=50, default='')
    time = models.CharField('Длительность программы', max_length=50, default='')

    def __str__(self):
        return self.phone

    def get_absolute_url(self):
        return f'/admin_area_online_order{self.id}'

    class Meta:
        verbose_name = 'Быстрый заказ'
        verbose_name_plural = 'Быстрые заказы'

class our_gallery(models.Model):
    description = models.TextField('Описание')
    img = models.ImageField('Изображение', upload_to='static/data_for_project/img/img_gallery', blank=True)
    date_event = models.DateTimeField('Дата и время события')

    def __str__(self):
        return self.description

    def get_absolute_url(self):
        return f'/admin_area_img_gallery{self.id}'

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'
