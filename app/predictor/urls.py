from django.urls import path

from . import views

app_name = "predictor"

urlpatterns = [
    path("", views.predict_stock, name="predict_stock"),
]
