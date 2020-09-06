from django.urls import path
from . import views

urlpatterns = [
    path("", views.PaymentMethodView.as_view(), name="home"),
    path("code/", views.CodeMethodView.as_view()),
]

