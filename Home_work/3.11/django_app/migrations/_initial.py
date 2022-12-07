from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(blank=True, default='', max_length=50, verbose_name='fullname')),
                ('age', models.IntegerField(blank=True, default=0, verbose_name='age')),
                ('parent_fullname', models.CharField(blank=True, default='', max_length=50, verbose_name='parent_fullname')),
            ],
        ),
        migrations.CreateModel(
            name='Ice_cream',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, default='', max_length=50, verbose_name='title')),
                ('manufacturer', models.CharField(blank=True, default='', max_length=50, verbose_name='manufacturer')),
            ],
        ),
        migrations.CreateModel(
            name='Ice_cream_kiosk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_fullname', models.CharField(blank=True, default='', max_length=50, verbose_name='seller_fullname')),
                ('owner', models.CharField(blank=True, default='', max_length=50, verbose_name='owner')),
                ('geolocation', models.CharField(blank=True, default='', max_length=50, verbose_name='geolocation')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(blank=True, default='', max_length=50, verbose_name='fullname')),
                ('age', models.IntegerField(blank=True, default=0, verbose_name='age')),
                ('child_fullname', models.CharField(blank=True, default='', max_length=50, verbose_name='child_fullname')),
            ],
        ),
    ]