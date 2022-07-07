from django.contrib import admin
from .models import Admin_pass , Student_data , Student_pass , Guard_data ,Guard_pass, Admin_data, Gatepass
# Register your models here.

admin.site.register(Admin_pass)
admin.site.register(Admin_data)

admin.site.register(Student_pass)
admin.site.register(Student_data)

admin.site.register(Guard_pass)
admin.site.register(Guard_data)


admin.site.register(Gatepass)
