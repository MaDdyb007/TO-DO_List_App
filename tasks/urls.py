from django.urls import path
from . import views
urlpatterns = [
    path('',views.add_show, name = "addandshow"),
    path('<int:id>/',views.update, name = "updatedata"),
    path('delete/<int:id>/',views.delete, name = "deletedata"),
    path('complete/<int:id>/',views.complete, name = "completedata"),

]
