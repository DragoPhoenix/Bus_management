from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Driver)
admin.site.register(Request)
admin.site.register(Bus)
admin.site.register(Schedule)
admin.site.register(Wallet)
admin.site.register(AdminUser)
admin.site.register(Booking)
