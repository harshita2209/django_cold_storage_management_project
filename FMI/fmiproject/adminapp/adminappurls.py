from django.urls import path
from . import views

urlpatterns=[
    path('adminhome/',views.adminhome,name='adminhome'),
    path('enquiries/',views.enquiries,name='enquiries'),
    path('booking/',views.booking,name='booking'),
    path('purchase/',views.purchase,name='purchase'),
    path('changepassword/',views.changepassword,name='changepassword'),
    path('logout/',views.logout,name='logout'),
    path('book/(?P<ano>\w+)',views.book,name='book'),
    path('pbook/',views.pbook,name='pbook'),
    path('viewbook/(?P<ano>\w+)',views.viewbook,name='viewbook'),
    path('deleteenq/(?P<id>\d+)',views.deleteenq,name='deleteenq'),
    path('addnews/',views.addnews,name='addnews'),
    path('deletenews/(?P<id>\d+)',views.deletenews,name='deletenews'),
    path('changepwd/',views.changepwd,name='changepwd'),
    path('pay/(?P<ano>\w+)',views.pay,name='pay'),
    path('paid/',views.paid,name='paid'),
]