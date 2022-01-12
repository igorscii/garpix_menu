# Generated by Django 3.1 on 2022-01-11 18:43

from django.db import migrations, models
import garpix_menu.validators
import garpix_utils.file.file_field


class Migration(migrations.Migration):

    dependencies = [
        ('garpix_menu', '0003_menuitem_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='hash',
            field=models.CharField(blank=True, default='', help_text='Если хотите дать ссылку на конкретный элемент страницы. Например - #example', max_length=256, verbose_name='Якорь'),
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='icon',
            field=models.FileField(blank=True, null=True, upload_to=garpix_utils.file.file_field.get_file_path, validators=[garpix_menu.validators.validate_type, garpix_menu.validators.validate_size], verbose_name='Иконка'),
        ),
    ]
