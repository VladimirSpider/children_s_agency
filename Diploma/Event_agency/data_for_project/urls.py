from django.urls import path
from . import views

#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    path('admin_area_User<int:pk>', views.UserDetailViewAdmin.as_view(), name='User_detail_admin'),
    path('admin_area_User<int:pk>/delete', views.UserDeleteView.as_view(), name='User_delete'),
    path('registration_page', views.registration_page, name='registration_page'),
    path('admin_area', views.admin_area, name='admin_area'),
    path('goods', views.goods, name='goods'),
    path('create_good', views.create_good, name='create_good'),
    path('product<int:pk>', views.serviceDetailViewUser.as_view(), name='service_detail'),
    path('admin_area_product<int:pk>', views.serviceDetailViewAdmin.as_view(), name='service_detail_admin'),
    path('admin_area_product<int:pk>/update', views.serviceUpdateView.as_view(), name='service_update'),
    path('admin_area_product<int:pk>/delete', views.serviceDeleteView.as_view(), name='service_delete'),
    path('reviews', views.our_reviews, name='reviews'),
    path('create_review', views.create_review, name='create_review'),
    path('admin_area_review<int:pk>', views.reviewDetailViewAdmin.as_view(), name='review_detail_admin'),
    path('admin_area_review<int:pk>/delete', views.reviewDeleteView.as_view(), name='review_delete'),
    path('gallery', views.mygallery, name='gallery'),
    path('create_img_gallery', views.create_img_gallery, name='create_img_gallery'),
    path('admin_area_img_gallery<int:pk>', views.img_galleryDetailViewAdmin.as_view(), name='img_gallery_detail_admin'),
    path('admin_area_img_gallery<int:pk>/update', views.img_galleryUpdateView.as_view(), name='img_gallery_update'),
    path('admin_area_img_gallery<int:pk>/delete', views.img_galleryDeleteView.as_view(), name='img_gallery_delete'),
    path('cost', views.cost, name='cost'),
    path('create_cost', views.create_cost, name='create_cost'),
    path('admin_area_cost<int:pk>', views.costDetailViewAdmin.as_view(), name='cost_detail_admin'),
    path('admin_area_cost<int:pk>/update', views.costUpdateView.as_view(), name='cost_update'),
    path('admin_area_cost<int:pk>/delete', views.costDeleteView.as_view(), name='cost_delete'),
    path('fast_online_orders', views.fast_online_order, name='fast_online_order'),
    path('do_fast_online_order', views.do_fast_online_order, name='do_fast_online_order'),
    path('admin_area_online_order<int:pk>', views.online_orderDetailView.as_view(), name='online_order_detail_admin'),
    path('admin_area_online_order<int:pk>/update', views.online_orderUpdateView.as_view(), name='online_order_update'),
    path('admin_area_online_order<int:pk>/delete', views.online_orderDeleteView.as_view(), name='online_order_delete'),
    path('Register', views.Register.as_view(), name="Register"),
    path('LogoutView', views.LogoutView.as_view(), name="logout"),
    path('LoginFormView', views.LoginFormView.as_view(), name="login"),
]

#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL,
#                          document_root=settings.MEDIA_ROOT)






