from django.urls import path
from django.contrib.auth.decorators import login_required
from establishment.views import (addEstablishment, editEstablishment, listEstablishment,
                                 viewEstablishment, delEstablishment, index)
from django.urls import reverse

app_name = 'establishment'
urlpatterns = [
        path('', index, name= 'Index'),
        path('list/', listEstablishment.as_view(), name = 'List'),
        path('list/<int:pk>/', viewEstablishment.as_view(), name = 'Single'),
        path('add/', addEstablishment.as_view(), name = 'Add'),
        path('edit/<int:pk>/', editEstablishment.as_view(), name = 'Edit'),
        path('del/<int:pk>/', delEstablishment.as_view(), name = 'Del'),

]
