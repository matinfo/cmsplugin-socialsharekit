# -*- coding: utf-8 -*-

from django.contrib import admin
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from adminsortable2.admin import SortableInlineAdminMixin

from . import models


class SocialButtonInline(SortableInlineAdminMixin, admin.TabularInline):
    model = models.SocialButton
    extra = 1

class SocialShareKitPlugin(CMSPluginBase):
    render_template = 'cmsplugin_socialsharekit/socialsharekit.html'
    allow_children = False
    name = _('Social Share Kit Plugin')
    module = _('Social Share Kit')
    model = models.SocialShareKitPlugin
    inlines = [SocialButtonInline, ]

    fieldsets = (
        (None, {
            'fields': (
                ('size', 'style'),
                ('count', 'greyscale'),

            )
        }),
        (_('Position'), {
            'fields': (
                'button_position',
                ('sticky', 'center'),
            )
        }),
        (_('Extra options'), {
            'fields': (
                ('group_width', 'forceinit'),
            ),
            'classes': ('collapse',)
        }),
    )
    class Media:
        css = {
            'all': ('cmsplugin_socialsharekit/css/admin/sortable.css',)
        }

plugin_pool.register_plugin(SocialShareKitPlugin)
