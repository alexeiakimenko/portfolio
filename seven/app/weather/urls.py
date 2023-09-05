<<<<<<< HEAD
from django.urls import path
from .views import *

urlpatterns = [
    path('', weather, name='weather'),
    path('<int:city_pk>/delete', deletecity, name='deletecity'),

]
=======
from django.urls import path
from .views import *

urlpatterns = [
    path('', weather, name='weather'),
    path('<int:city_pk>/delete', deletecity, name='deletecity'),

]
>>>>>>> c56e1a6cee1fb286d87fdf677c9758e9a101d523
