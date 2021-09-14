from django.contrib import admin

# Register your models here.

from django.contrib import admin
from notice.models import Notice


admin.site.site_header = '预约提醒'
admin.site.site_title = '错过亏一个亿'
admin.site.index_title = '最后一次机会'


admin.site.register(Notice)
