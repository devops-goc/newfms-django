from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_alm/', views.all_alm, name='all_alm'),

    path('logout_view', views.logout_view, name='logout'),
    path('logout_view/', views.logout_view, name='logout'),

    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    path('done', views.done, name='done'),
    path('done/', views.done, name='done'),

    path('ack/<int:id>', views.ack, name='ack'),
    path('delete/<int:id>', views.delete, name='delete'),

    path('tecnologia/<str:buscar>', views.all_tecnologia, name='tecnologia'),
    path('filtro/<str:buscar>', views.all_filtro, name='filtro'),
    path('codigo/<str:buscar>', views.all_codigo, name='codigo'),

]
