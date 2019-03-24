from django.contrib import admin

from .models import Infographic, Language, Tag, InfographicSource, InfographicContent


class InfographicSourceAdminInline(admin.TabularInline):
    model = InfographicSource
    extra = 0


class InfographicContentAdminInline(admin.TabularInline):
    model = InfographicContent
    extra = 0


@admin.register(Infographic)
class InfographicAdmin(admin.ModelAdmin):
    inlines = (InfographicContentAdminInline, InfographicSourceAdminInline)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


@admin.register(InfographicContent)
class InfographicContent(admin.ModelAdmin):
    pass


@admin.register(InfographicSource)
class InfographicSourceAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
