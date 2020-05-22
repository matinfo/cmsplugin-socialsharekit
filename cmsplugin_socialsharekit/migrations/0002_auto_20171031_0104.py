


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_socialsharekit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socialbutton',
            name='button',
            field=models.CharField(default=None, null=True, verbose_name='button', blank=True, max_length=20, choices=[('facebook', 'Facebook'), ('twitter', 'Twitter'), ('google-plus', 'Google +'), ('pinterest', 'Pinterest'), ('tumblr', 'Tumblr'), ('linkedin', 'Linkedin'), ('vk', 'VK'), ('buffer', 'Buffer'), ('email', 'Email')]),
        ),
    ]
