from django.urls import path

from amsmain import views
urlpatterns = [
    path('', views.show_index),
    path('singlePortfolio/', views.show_singlePorto),
    path('about/', views.show_about),
    path('contact/', views.show_register),
    path('contact/dashboard/', views.show_dash),
    path('contact/dashboard/delete/<did>', views.delete),
    path('portfolio/', views.show_portfolio),
    # path('/https://www.instagram.com/')

]

