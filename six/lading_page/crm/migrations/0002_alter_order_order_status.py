<<<<<<< HEAD
# Generated by Django 4.2.2 on 2023-08-30 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.ForeignKey(blank=True, default='1', on_delete=django.db.models.deletion.PROTECT, to='crm.statuscrm', verbose_name='Статус'),
        ),
    ]
=======
# Generated by Django 4.2.2 on 2023-08-30 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.ForeignKey(blank=True, default='1', on_delete=django.db.models.deletion.PROTECT, to='crm.statuscrm', verbose_name='Статус'),
        ),
    ]
>>>>>>> c56e1a6cee1fb286d87fdf677c9758e9a101d523