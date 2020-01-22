from django.contrib import admin
from .models import Disease,Crowdsource

# Register your models here.
# class Details(admin.ModelAdmin):
#     fieldsets=[
#         ("Personal Details",{"fields":["Age","Gender","Created_By","created_date","modified_date"]}),
#         ("Disease",{"fields":["Disease"]})
#     ]
admin.site.register(Disease)
admin.site.register(Crowdsource)