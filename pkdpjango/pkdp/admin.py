from django.contrib import admin
from pkdp.models import Member

# Register your models here.


class MemberAdmin(admin.ModelAdmin):
    list_display= ('mem_name', 'mem_age', 'mem_email')

admin.site.register(Member, MemberAdmin)
