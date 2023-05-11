from django.contrib import admin
from django.urls import path, include
from Crudapp import views

urlpatterns = [
    path("show_base/" , views.show_base , name="basefile"),
    path("add_show/" ,views.add_show ,name="add_show"  ),
    path("delete/<int:id>/" , views.delete_data , name="deletedata"),
    path("<int:id>/" , views.update_data , name="updatestudent")
    ]