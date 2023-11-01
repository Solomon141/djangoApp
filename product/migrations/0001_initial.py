# Generated by Django 4.2.6 on 2023-11-01 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Lookups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Badreg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pcode', models.CharField(max_length=15, null=True)),
                ('pname', models.CharField(max_length=255, null=True)),
                ('Compositions', models.TextField()),
                ('UnitMeasure', models.CharField(max_length=255, null=True)),
                ('paking', models.CharField(max_length=255, null=True)),
                ('pksize', models.CharField(max_length=255, null=True)),
                ('unitPrice', models.FloatField()),
                ('MH_Count', models.IntegerField()),
                ('badreg_Count', models.IntegerField()),
                ('mh_stockout', models.BooleanField(blank=True, default=False, null=True)),
                ('badreg_stockout', models.BooleanField(blank=True, default=False, null=True)),
                ('expDate', models.CharField(max_length=255, null=True)),
                ('criticalVal', models.CharField(max_length=255, null=True)),
                ('img_hd', models.CharField(max_length=255, null=True)),
                ('img_md', models.CharField(max_length=255, null=True)),
                ('img_sm', models.CharField(max_length=255, null=True)),
                ('img_blob', models.CharField(max_length=255, null=True)),
                ('discount', models.FloatField(null=True)),
                ('drugstore', models.BooleanField(blank=True, default=False, null=True)),
                ('pharm', models.BooleanField(blank=True, default=False, null=True)),
                ('pcat', models.BooleanField(blank=True, default=False, null=True)),
                ('Brand_ID', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='vendor', to='Lookups.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Competitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, null=True)),
                ('badreg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.badreg')),
            ],
        ),
    ]
