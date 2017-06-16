# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='SocialButton',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('button', models.CharField(null=True, verbose_name='button', max_length=20, choices=[('facebook', 'Facebook'), ('twitter', 'Twitter'), ('google-plus', 'Google +'), ('pinterest', 'Pinterest'), ('tumbr', 'Tumbr'), ('linkedin', 'Linkedin'), ('vk', 'VK'), ('buffer', 'Buffer'), ('email', 'Email')], blank=True, default=None)),
                ('icononly', models.BooleanField(verbose_name='icon only', default=False)),
                ('text', models.CharField(verbose_name='button label', max_length=50, blank=True, null=True)),
                ('order', models.PositiveIntegerField(db_index=True, default=0)),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='SocialShareKitPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, to='cms.CMSPlugin', parent_link=True, auto_created=True, related_name='cmsplugin_socialsharekit_socialsharekitplugin')),
                ('size', models.CharField(verbose_name='size', max_length=2, default='sm', choices=[('xs', 'Extra Small'), ('s', 'Small'), ('sm', 'Regular'), ('lg', 'Large')])),
                ('style', models.CharField(verbose_name='style', max_length=10, default='square', choices=[('square', 'Square'), ('round', 'Round'), ('rounded', 'Rounded')])),
                ('count', models.BooleanField(verbose_name='count', default=False)),
                ('greyscale', models.BooleanField(verbose_name='greyscale', default=False)),
                ('group_width', models.CharField(help_text='Need used in conjunction with button *label*. Ex: 120px or 100%.', null=True, verbose_name='block width', max_length=5, blank=True, default='')),
                ('forceinit', models.BooleanField(help_text='In case if you want to initialize right away without waiting for DOM to load.', verbose_name='forceInit', default=False)),
                ('sticky', models.BooleanField(verbose_name='sticky', default=False)),
                ('center', models.BooleanField(verbose_name='center', default=False)),
                ('button_position', models.CharField(null=True, verbose_name='buttons position', max_length=10, choices=[('left', 'Left side'), ('right', 'Right side'), ('bottom', 'Bottom')], blank=True, default=None)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='socialbutton',
            name='plugin',
            field=models.ForeignKey(to='cmsplugin_socialsharekit.SocialShareKitPlugin', related_name='buttons'),
        ),
    ]
