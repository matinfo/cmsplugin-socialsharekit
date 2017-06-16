# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin

from .settings import *


class SocialButton(models.Model):
    """ SocialButton model """
    button = models.CharField(
        _('button'),
        max_length=20,
        choices=SOCIALBUTTONS,
        default=None,
        blank=True,
        null=True
    )
    icononly = models.BooleanField(
        _('icon only'),
        default=False
    )
    text = models.CharField(
        _('button label'),
        max_length=50,
        blank=True,
        null=True
    )
    plugin = models.ForeignKey(
        'cmsplugin_socialsharekit.SocialShareKitPlugin',
        related_name="buttons",
        blank=False,
        null=False
    )
    order = models.PositiveIntegerField(
        default=0,
        blank=False,
        null=False,
        db_index=True
    )

    class Meta(object):
        ordering = ['order',]

    def __str__(self):
        if self.button:
            return self.get_button_display()


class SocialShareKitPlugin(CMSPlugin):
    """ Social Share Kit CMS plugin model """
    size = models.CharField(
        _('size'),
        max_length=2,
        choices=SOCIALBUTTON_SIZES,
        default=DEFAULT_SOCIALBUTTON_SIZE
    )
    style = models.CharField(
        _('style'),
        max_length=10,
        choices=SOCIALBUTTON_STYLES,
        default=DEFAULT_SOCIALBUTTON_STYLE
    )
    count = models.BooleanField(
        _('count'),
        default=False
    )
    greyscale = models.BooleanField(
        _('greyscale'),
        default=False
    )

    # extra options
    group_width = models.CharField(
        _('block width'),
        max_length=5,
        default='',
        blank=True,
        null=True,
        help_text=_('Need used in conjunction with button *label*. '
                    'Ex: 120px or 100%.')
    )
    forceinit = models.BooleanField(
        _('forceInit'),
        default=False,
        help_text=_('In case if you want to initialize right away without '
                    'waiting for DOM to load.')
    )

    # position
    sticky = models.BooleanField(
        _('sticky'),
        default=False
    )
    center = models.BooleanField(
        _('center'),
        default=False
    )
    button_position = models.CharField(
        _('buttons position'),
        max_length=10,
        choices=SOCIALBUTTON_POSITIONS,
        default=None,
        blank=True,
        null=True
    )

    def __str__(self):
        return 'Size: {}, Style: {}, Count: {}, Greyscale: {}'.format(
            self.get_size_display(),
            self.get_style_display(),
            'Yes' if self.count else 'No',
            'Yes' if self.greyscale else 'No')

    def copy_relations(self, oldinstance):
        self.buttons.all().delete()

        for button in oldinstance.buttons.all():
            button.pk = None
            button.plugin = self
            button.save()
