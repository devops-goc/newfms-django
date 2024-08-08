from django.contrib import admin
from .models import Alarma

class AlarmaAdmin(admin.ModelAdmin):
    list_display= ('ID', 'TECNOLOGIA', 'FILTRO','CODIGO','HUB','AMO','DESCRIPCION','SEVERIDAD','FIRSTTIMEx','LASTTIMEx','CONTADOR','USER','ACK')
    search_fields = ['ID','AMO', 'DESCRIPCION','TECNOLOGIA','FILTRO','CODIGO','HUB']
    list_filter = ('TECNOLOGIA', 'FILTRO','CODIGO','HUB', )

    def FIRSTTIMEx(self, obj):
        return obj.FIRSTTIME.strftime("%Y/%m/%d %H:%M:%S")
    def LASTTIMEx(self, obj):
        return obj.LASTTIME.strftime("%Y/%m/%d %H:%M:%S")

    LASTTIMEx.short_description = 'lasttime'
    FIRSTTIMEx.short_description = 'firsttime'
    LASTTIMEx.admin_order_field = 'lasttime'

admin.site.register(Alarma,AlarmaAdmin)
