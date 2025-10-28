from django.contrib import admin
from actors.models import Actor


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    fields = ('name',)

