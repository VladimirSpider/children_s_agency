from django.shortcuts import render, redirect
from .models import service, our_gallery, service_cost, review, fast_online_order
from .forms import orderForm, reviewsForm, goodsForm, galleryForm, costForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
from django.contrib.auth.models import User

class UserDetailViewAdmin(DetailView):
    model = User
    template_name = 'data_for_project/details_User_admin.html'
    context_object_name = 'User'#просто ключ

class UserDeleteView(DeleteView):
    model = User
    success_url = '/admin_area'
    template_name = 'data_for_project/delete_User.html'

def admin_area(request, service=service, service_cost=service_cost):
    goods = service.objects.all()
    all_reviews = review.objects.order_by('review')
    mygallery = our_gallery.objects.all()
    all_orders = fast_online_order.objects.all()
    users = User.objects.all()
    service_sort = ''
    if request.method == 'POST':
        service_sort = request.POST['service_sort']
    service = service.objects.all()
    our_cost = ''
    if service_sort == '':
        our_cost = service_cost.objects.all()
    else:
        our_cost = service_cost.objects.filter(id_service__service_name=service_sort)
    return render(request, 'data_for_project/all_admin.html', {'goods': goods,
                                                              'all_reviews': all_reviews,
                                                              'mygallery': mygallery,
                                                              'all_orders': all_orders,
                                                               'service':service,
                                                               'our_cost':our_cost,
                                                               'service_sort':service_sort,
                                                               'users':users})

def goods(request):
    goods = service.objects.all()
    return render(request, 'data_for_project/goods.html', {'goods': goods})

def create_good(request):
    error = ''
    if request.method == 'POST':
        form = goodsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_area')
        else:
            error = 'Форма заполнена неверно'

    form = goodsForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'data_for_project/create_goods.html', data)

class serviceDetailViewUser(DetailView):
    model = service
    template_name = 'data_for_project/details_view.html'
    context_object_name = 'service'#просто ключ

class serviceDetailViewAdmin(DetailView):
    model = service
    template_name = 'data_for_project/details_view_admin.html'
    context_object_name = 'service'#просто ключ

class serviceUpdateView(UpdateView):
    model = service
    template_name = 'data_for_project/update_view.html'
    form_class = goodsForm

class serviceDeleteView(DeleteView):
    model = service
    success_url = '/admin_area'
    template_name = 'data_for_project/delete_view.html'

def our_reviews(request):
    all_reviews = review.objects.order_by('review')
    return render(request, 'data_for_project/reviews.html', {'all_reviews': all_reviews})

def create_review(request):
    error = ''
    if request.method == 'POST':
        form = reviewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reviews')
        else:
            error = 'Форма заполнена неверно'


    form = reviewsForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'data_for_project/create_review.html', data)

class reviewDetailViewAdmin(DetailView):
    model = review
    template_name = 'data_for_project/details_review_admin.html'
    context_object_name = 'review'#просто ключ

class reviewDeleteView(DeleteView):
    model = review
    success_url = '/admin_area'
    template_name = 'data_for_project/delete_review.html'

def cost(request, service=service, service_cost=service_cost ):
    service_sort= ''
    if request.method == 'POST':
        service_sort = request.POST['service_sort']
    service = service.objects.all()
    our_cost = ''
    if service_sort == '':
        our_cost = service_cost.objects.all()
    else:
        our_cost = service_cost.objects.filter(id_service__service_name=service_sort)
    return render(request, 'data_for_project/cost.html', {'service':service,
                                                              'our_cost':our_cost,
                                                              'service_sort':service_sort})

def create_cost(request):
    error = ''
    if request.method == 'POST':
        form = costForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_area')
        else:
            error = 'Форма заполнена неверно'

    form = costForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'data_for_project/create_cost.html', data)

class costDetailViewAdmin(DetailView):
    model = service_cost
    template_name = 'data_for_project/details_cost_admin.html'
    context_object_name = 'service_cost'#просто ключ

class costUpdateView(UpdateView):
    model = service_cost
    template_name = 'data_for_project/update_cost.html'
    form_class = costForm

class costDeleteView(DeleteView):
    model = service_cost
    success_url = '/admin_area'
    template_name = 'data_for_project/delete_cost.html'


def online_orders(request):
    all_orders = fast_online_order.objects.all()
    return render(request, 'data_for_project/do_fast_online_order.html', {'all_orders': all_orders})


def do_fast_online_order(request, service=service):
    error = ''
    hero=''
    if request.method == 'POST':
        hero=request.POST['hero']
        form = orderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            error = 'Форма заполнена неверно'
            hero = 'пусто'


    form = orderForm()
    service=service.objects.all()

    data = {
        'form': form,
        'error': error,
        'service': service,
        'hero': hero
    }
    return render(request, 'data_for_project/do_fast_online_order.html', data)

class online_orderDetailView(DetailView):
    model = fast_online_order
    template_name = 'data_for_project/details_online_order.html'
    context_object_name = 'online_order'#просто ключ

class online_orderUpdateView(UpdateView):
    model = fast_online_order
    template_name = 'data_for_project/update_online_order.html'
    form_class = orderForm

class online_orderDeleteView(DeleteView):
    model = fast_online_order
    success_url = '/admin_area'
    template_name = 'data_for_project/delete_online_order.html'

def mygallery(request):
    mygallery = our_gallery.objects.all()
    return render(request, 'data_for_project/gallery.html', {'mygallery': mygallery})

def create_img_gallery(request):
    error = ''
    if request.method == 'POST':
        form = galleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_area')
        else:
            error = 'Форма заполнена неверно'

    form = galleryForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'data_for_project/create_img_gallery.html', data)

class img_galleryDetailViewAdmin(DetailView):
    model = our_gallery
    template_name = 'data_for_project/details_img_gallery_admin.html'
    context_object_name = 'our_gallery'#просто ключ

class img_galleryUpdateView(UpdateView):
    model = our_gallery
    template_name = 'data_for_project/update_img_gallery.html'
    form_class = galleryForm

class img_galleryDeleteView(DeleteView):
    model = our_gallery
    success_url = '/admin_area'
    template_name = 'data_for_project/delete_img_gallery.html'

##############################################################################

# Вариант регистрации на базе класса FormView
class Register(FormView):
    # Указажем какую форму мы будем использовать для регистрации наших пользователей, в нашем случае
    # это UserCreationForm - стандартный класс Django унаследованный
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/goods"

    # Шаблон, который будет использоваться при отображении представления.
    template_name = "data_for_project/register.html"

    def form_valid(self, form):
        form.save()
        # Функция super( тип [ , объект или тип ] )
        # Возвратите объект прокси, который делегирует вызовы метода родительскому или родственному классу типа .
        return super(Register, self).form_valid(form)

    #def form_invalid(self, form):
    #    return super(MyRegisterFormView, self).form_invalid(form)

#################################################################

def registration_page(request):
    return render(request, 'data_for_project/registration_page.html')

# Функция для установки сессионного ключа.
# По нему django будет определять, выполнил ли вход пользователь.
from django.contrib.auth import login

class LoginFormView(FormView):
    form_class = AuthenticationForm

    # Аналогично регистрации, только используем шаблон аутентификации.
    template_name = "data_for_project/login.html"

    # В случае успеха перенаправим на главную.
    success_url = "/"

    def form_valid(self, form):
        # Получаем объект пользователя на основе введённых в форму данных.
        self.user = form.get_user()

        # Выполняем аутентификацию пользователя.
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

##############################################################

class LogoutView(View):
    def get(self, request):
        # Выполняем выход для пользователя, запросившего данное представление.
        logout(request)

        # После чего, перенаправляем пользователя на главную страницу.
        return HttpResponseRedirect("/registration_page")

##############################################################
