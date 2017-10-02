from django.contrib import admin

from .models import Infographic, Language, InfographicURL, Tag


# Register your models here.
class InfographicURLAdminInline(admin.TabularInline):
    model = InfographicURL
    extra = 0


@admin.register(Infographic)
class InfographicAdmin(admin.ModelAdmin):
    inlines = (InfographicURLAdminInline,)
    pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(InfographicURL)
class InfographicURLAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
