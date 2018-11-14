from django.contrib import admin

from .models import Infographic, Language, InfographicURL, Tag, InfographicSource


# Register your models here.
class InfographicURLAdminInline(admin.TabularInline):
    model = InfographicURL
    extra = 0


class InfographicSourceAdminInline(admin.TabularInline):
    model = InfographicSource
    extra = 0


@admin.register(Infographic)
class InfographicAdmin(admin.ModelAdmin):
    inlines = (InfographicURLAdminInline, InfographicSourceAdminInline)
    pass


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(InfographicURL)
class InfographicURLAdmin(admin.ModelAdmin):
    pass


@admin.register(InfographicSource)
class InfographicSourceAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
