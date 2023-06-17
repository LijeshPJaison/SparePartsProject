from django.urls import path,include
# from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('index',views.IndexFunction,name='index'),
    path('add_questions',views.AddQuestionsFunction,name='add_questions'),
    path('inspection',views.InspectionFunction,name='inspection'),
    path('list_inspection',views.ListInspectionFunction,name='list_inspection'),
    path('home',views.HomeFunction, name='home'),
    path('login', views.LoginFunction, name= 'login'),
    path('logout', views.LogoutFunction, name= 'logout'),
    path('signup',views.SignupFunction, name='signup'),
    path('service',views.ServiceFunction, name='service'),
    path('purchase_list',views.PurchaseListFunction, name='purchase_list'),
    path('purchase',views.PurchaseFunction, name='purchase'),
    path('delete/<int:id>',views.DeleteFunction, name='delete'),
    path('delete_questions/<int:id>',views.DeleteQuestionsFunction, name='delete_questions'),
]