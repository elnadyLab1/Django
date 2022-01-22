# Generated by Django 4.0.1 on 2022-01-22 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('native', models.CharField(blank=True, max_length=20, null=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=5, null=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('native', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('code', models.CharField(blank=True, max_length=5, null=True, unique=True)),
                ('tel_code', models.CharField(blank=True, max_length=5, null=True, unique=True)),
                ('emoji', models.CharField(blank=True, max_length=5, null=True, unique=True)),
                ('continent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='countries', to='Utils.continent')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('native', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('code', models.CharField(blank=True, max_length=5, null=True, unique=True)),
                ('emoji', models.CharField(blank=True, max_length=5, null=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('emoji', models.CharField(blank=True, max_length=5, null=True, unique=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('native', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('rtl', models.BooleanField(default=False)),
                ('symbol', models.CharField(max_length=4, unique=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MaritalStatus',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('emoji', models.CharField(blank=True, max_length=5, null=True, unique=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MobileCompany',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('code', models.CharField(blank=True, max_length=5, null=True, unique=True)),
                ('emoji', models.CharField(blank=True, max_length=5, null=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StageLife',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('from_age', models.SmallIntegerField()),
                ('to_age', models.SmallIntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Village',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('native', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='villages', to='Utils.city')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Street',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('native', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('village', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='streets', to='Utils.village')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Governorate',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('native', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('tel_code', models.CharField(blank=True, max_length=3, null=True, unique=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='governorates', to='Utils.country')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='country',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='countries', to='Utils.language'),
        ),
        migrations.AddField(
            model_name='city',
            name='governorate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='Utils.governorate'),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('native', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('house', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('street', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='address', to='Utils.street')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='titles', to='Utils.gender')),
                ('job', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='titles', to='Utils.job')),
                ('stage_life', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='titles', to='Utils.stagelife')),
            ],
            options={
                'unique_together': {('stage_life', 'job', 'gender')},
            },
        ),
    ]
