# -*- coding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _


SOCIALBUTTONS = [
    ('facebook', _('Facebook')),
    ('twitter', _('Twitter')),
    ('google-plus', _('Google +')),
    ('pinterest', _('Pinterest')),
    ('tumblr', _('Tumblr')),
    ('linkedin', _('Linkedin')),
    ('vk', _('VK')),
    ('buffer', _('Buffer')),
    ('email', _('Email')),
]
DEFAULT_SOCIALBUTTON = SOCIALBUTTONS[0][0]

SOCIALBUTTON_STYLES = [
    ('square', _('Square')),
    ('round', _('Round')),
    ('rounded', _('Rounded')),
]
DEFAULT_SOCIALBUTTON_STYLE = SOCIALBUTTON_STYLES[0][0]

SOCIALBUTTON_SIZES = [
    ('xs', _('Extra Small')),
    ('s', _('Small')),
    ('sm', _('Regular')),
    ('lg', _('Large')),
]
DEFAULT_SOCIALBUTTON_SIZE = SOCIALBUTTON_SIZES[2][0]

SOCIALBUTTON_POSITIONS = [
    ('left', _('Left side')),
    ('right', _('Right side')),
    ('bottom', _('Bottom')),
]
