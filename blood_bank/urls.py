from django.contrib import admin
from django.urls import path, include
from bank import urls

admin.site.site_header = "Blood Bank"
admin.site.index_title = "Welcome to Blood Bank NFG"

urlpatterns = [
    path('siteAdminApproveByNFG/', admin.site.urls),
    path('', include('bank.urls')),
]