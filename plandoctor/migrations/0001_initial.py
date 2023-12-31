# Generated by Django 4.2.6 on 2023-11-01 13:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('doctor', '0001_initial'),
        ('plan', '0003_alter_plan_created_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanDoctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.TextField()),
                ('doctors', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plandoctor', to='doctor.doctor')),
                ('planid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='plandoctor', to='plan.plan')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.badreg')),
            ],
        ),
    ]
