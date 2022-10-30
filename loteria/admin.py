#!/usr/bin/env python
from django.core.urlresolvers import reverse
from django.contrib import admin
#from django.contrib.admin import widgets
#from django.forms.TimeField import widget

from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
from elarropao.settings import TINYMCE_JS_ROOT, TINYMCE_JS_URL
from elarropao.loteria.models import Loteria, Sorteo, Animalito, Signo, Resultado_Kino, Resultado_Triple, Resultado_Triple_Gordo, Resultado_Papaya, Publicidad, Noticia
from elarropao.loteria.models import Profile
from elarropao.loteria.models import CampoColor

admin.autodiscover()

class Media:
        js = [TINYMCE_JS_URL, TINYMCE_JS_ROOT+'js/TinyMCEAdmin.js',]


class CampoColorAdmin(admin.ModelAdmin):
    list_display = ['color']
    ordering = ['color']
    
admin.site.register(CampoColor, CampoColorAdmin)

class LoteriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'imagen')
    
admin.site.register(Loteria, LoteriaAdmin)

class SorteoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo', 'hora', 'tipo', 'loteria')
    list_filter = ('loteria', 'hora')
    ordering = ['loteria', 'nombre', 'hora']

    class Meta:
        model = Sorteo
'''
    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('hora'):
            return db_field.formfield(widget=SelectTimeWidget(
                minute_step=15, second_step=30, twelve_hr=True, 
            ))
        return super(SorteoAdmin, self).formfield_for_dbfield(db_field, **kwargs)
'''
admin.site.register(Sorteo, SorteoAdmin)

class AnimalitoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'imagen')

admin.site.register(Animalito, AnimalitoAdmin)

class SignoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'imagen')

admin.site.register(Signo, SignoAdmin)

class Resultado_TripleAdmin(admin.ModelAdmin):
    list_display = ('numero', 'animalito', 'signo', 'fecha', 'sorteo')
    ordering = ['sorteo', 'fecha', 'numero']
    list_filter = ('fecha',)
    #    search_fields = ('^suscriptor__nombres', '^suscriptor__apellidos')
 
admin.site.register(Resultado_Triple, Resultado_TripleAdmin)

class Resultado_KinoAdmin(admin.ModelAdmin):
    list_display = ('numero_sorteo', 'fecha', 'sorteo')
    list_filter = ('fecha',)
 
admin.site.register(Resultado_Kino, Resultado_KinoAdmin)

class Resultado_Triple_GordoAdmin(admin.ModelAdmin):
    list_display = ('numero_sorteo', 'fecha', 'sorteo')
    list_filter = ('fecha',)
 
admin.site.register(Resultado_Triple_Gordo, Resultado_Triple_GordoAdmin)

class Resultado_PapayaAdmin(admin.ModelAdmin):
    list_display = ('numero_sorteo', 'fecha', 'sorteo')
    list_filter = ('fecha',)
 
admin.site.register(Resultado_Papaya, Resultado_PapayaAdmin)

class PublicidadAdmin(admin.ModelAdmin):
    list_display = ('archivo', 'tipo', 'contenedor', 'orden')
    ordering = ['contenedor', 'orden']
    list_filter = ('contenedor', 'tipo')

admin.site.register(Publicidad, PublicidadAdmin)

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'publicar')
    list_filter = ('publicar',)
    search_fields = ('titulo', 'publicar')

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name in ('nota'):
            return db_field.formfield(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
            ))
        return super(NoticiaAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(Noticia, NoticiaAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    ordering = ['email']
    search_fields = ['first_name', 'email']
    actions = ['make_mailing_list',]


    def make_mailing_list(self, request, queryset):
        from emencia.django.newsletter.models import Contact
        from emencia.django.newsletter.models import MailingList

        subscribers = []

        for profile in queryset:
            contact, created = Contact.objects.get_or_create(email=profile.email,
                                                             defaults={'first_name': profile.first_name,
                                                                       'last_name': profile.last_name,
                                                                       'content_object': profile}
                                                            )
        subscribers.append(contact)
        new_mailing = MailingList(name='New mailing list',
                                  description='New mailing list created from admin/profile')
        new_mailing.save()
        new_mailing.subscribers.add(*subscribers)
        new_mailing.save()

        self.message_user(request, '%s succesfully created.' % new_mailing)

    make_mailing_list.short_description = 'Create a mailing list'

admin.site.register(Profile, ProfileAdmin)

