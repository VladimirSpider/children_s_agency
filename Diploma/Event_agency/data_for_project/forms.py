from .models import review, fast_online_order, service, our_gallery, service_cost
from django.forms import ModelForm, TextInput, NumberInput, EmailInput, Select, RadioSelect, Textarea, DateTimeInput, FileInput
from django.contrib.auth.models import User

class reviewsForm(ModelForm):
    class Meta:
        model = review
        fields = ['u_name', 'u_surname', 'review']

        widgets = {
            "u_name": TextInput(attrs={
                'class': 'form_review',
                'placeholder': 'Введите ваше имя',
            }),
            "u_surname": TextInput(attrs={
                'class': 'form_review',
                'placeholder': 'Введите вашу фамилию',
            }),
            "review": Textarea(attrs={
                'class': 'form_review',
                'placeholder': 'Ваш отзыв',
            }),
        }


class orderForm(ModelForm):
    class Meta:
        model = fast_online_order
        fields = ['name', 'phone', 'date', 'number_children', 'hero', 'time']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form_order',
                'placeholder': 'Введите ваше имя',
            }),
            "phone": NumberInput(attrs={
                'class': 'form_order',
                'placeholder': 'Введите ваш телефон',
            }),
            "date": DateTimeInput(attrs={
                'class': 'form_order',
                'placeholder': 'Введите желаемую дату и время праздника',
            }),
            "number_children": NumberInput(attrs={
                'class': 'form_order',
                'placeholder': 'Колличество детей',
            }),
            "hero": TextInput(attrs={
                'class': 'form_order',
                'placeholder': 'Выберите героя',
            }),
            "time": TextInput(attrs={
                'class': 'form_order',
                'placeholder': 'Выберите длительность праздника',
            }),
        }

class goodsForm(ModelForm):
    class Meta:
        model = service
        fields = ['service', 'img_service1', 'img_service2', 'img_service3', 'service_name', 'service_description']

        widgets = {
            "service": TextInput(attrs={
                'class': 'form_order',
                'placeholder': 'Вид услуги',
            }),
            "img_service1": FileInput(attrs={
                'class': 'form_order',
                'placeholder': 'Картинка1',
            }),
            "img_service2": FileInput(attrs={
                'class': 'form_order',
                'placeholder': 'Картинка2',
            }),
            "img_service3": FileInput(attrs={
                'class': 'form_order',
                'placeholder': 'Картинка3',
            }),
            "service_name": TextInput(attrs={
                'class': 'form_order',
                'placeholder': 'Название услуги',
            }),
            "service_description": Textarea(attrs={
                'class': 'form_order',
                'placeholder': 'Описание услуги',
            }),
        }

class galleryForm(ModelForm):
    class Meta:
        model = our_gallery
        fields = ['description', 'img', 'date_event']

        widgets = {
            "description": Textarea(attrs={
                'class': 'form_order',
                'placeholder': 'Описание',
            }),
            "img": FileInput(attrs={
                'class': 'form_order',
                'placeholder': 'Картинка',
            }),
            "date_event": DateTimeInput(attrs={
                'class': 'form_order',
                'placeholder': 'Дата и время',
            }),

        }

class costForm(ModelForm):
    class Meta:
        model = service_cost
        fields = ['id_service', 'service_cost_min', 'service_cost_base', 'service_cost_max']

        widgets = {
            "id_service": Select(attrs={
                'class': 'form_order',
                'placeholder': 'Стоимость 30мин.',
            }),
            "service_cost_min": Textarea(attrs={
                'class': 'form_order',
                'placeholder': 'Стоимость 30мин.',
            }),
            "service_cost_base": Textarea(attrs={
                'class': 'form_order',
                'placeholder': 'Стоимость 60мин.',
            }),
            "service_cost_max": Textarea(attrs={
                'class': 'form_order',
                'placeholder': 'Стоимость 90мин.',
            }),

        }
