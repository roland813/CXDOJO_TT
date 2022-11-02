from django.urls import path

from app.views import index, user_data_list_view

urlpatterns = [
    path("", index, name="index"),
    path("data", user_data_list_view, name="user_data_list_view")
]

app_name = "app"
