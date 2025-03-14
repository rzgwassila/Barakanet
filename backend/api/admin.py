from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    User, Location, Volunteer, CharitableOrganization, 
    Photo, Event, VolunteerRequest, VolunteerHistory
)

admin.site.register(User, UserAdmin)
admin.site.register(Location)
admin.site.register(Volunteer)
admin.site.register(CharitableOrganization)
admin.site.register(Photo)
admin.site.register(Event)
admin.site.register(VolunteerRequest)
admin.site.register(VolunteerHistory)