# Generated by Django 4.2.6 on 2023-11-01 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('entity', '0001_initial'),
        ('plan', '0003_alter_plan_created_by'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanEntity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('purpose', models.TextField()),
                ('entities', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entities', to='entity.entity')),
                ('planid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='planentity', to='plan.plan')),
                ('products', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entityproducts', to='product.badreg')),
            ],
        ),
    ]
