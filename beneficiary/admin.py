from django.contrib import admin
from .models import Household, Person, AssistanceProject, Enrollment

admin.site.register(Household)
admin.site.register(Person)
admin.site.register(AssistanceProject)
admin.site.register(Enrollment)
