from django.urls import path
from . import views

urlpatterns = [
    path('displayindex/', views.displayindex, name="displayindex"),
    path('displaystudent/', views.displaystudent, name="displaystudent"),
    path('studentdata/', views.studentdata, name="studentdata"),
    path('studentdetails/', views.studentdetails, name="studentdetails"),
    path('studentedit/<int:dataid>/', views.studentedit, name="studentedit"),
    path('studentupdate/<int:dataid>/', views.studentupdate, name="studentupdate")
]