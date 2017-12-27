from django.urls import path
from members.views import member_form, listData, dataDetails
from django.contrib.auth.decorators import login_required
app_name = 'members'

urlpatterns = [

        path('', member_form, name = 'mainForm'),
        path('list/', login_required(listData.as_view()), name= 'listData'),
        path('list/<int:pk>/', login_required(dataDetails.as_view()), name= 'dataDetails'),
]
