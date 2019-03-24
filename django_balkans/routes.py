from django.contrib import admin
from django.urls import path

from board.views import start_page

urlpatterns = [
    path('', start_page, name='start_page'),
    path('admin/', admin.site.urls),
]
