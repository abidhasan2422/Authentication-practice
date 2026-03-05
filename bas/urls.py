
from django.contrib import admin
from django.urls import path,include
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',views.LCStudentAPI.as_view()),
    path('studentapi/<int:pk>/',views.UDRStudentAPI.as_view()),
     path('auth/', include('rest_framework.urls')),

]
