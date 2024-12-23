# Generated by Django 5.1.3 on 2024-11-29 19:27

import django.core.validators
import django.db.models.deletion
import uuid
import versatileimagefield.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SubVariant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=255)),
                ('stock', models.DecimalField(decimal_places=8, default=0.0, max_digits=20, validators=[django.core.validators.MinValueValidator(0.0)])),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('ProductID', models.BigIntegerField(unique=True)),
                ('ProductCode', models.CharField(max_length=255, unique=True)),
                ('ProductName', models.CharField(max_length=255)),
                ('ProductImage', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='uploads/')),
                ('CreatedDate', models.DateTimeField(auto_now_add=True)),
                ('UpdatedDate', models.DateTimeField(blank=True, null=True)),
                ('IsFavourite', models.BooleanField(default=False)),
                ('Active', models.BooleanField(default=True)),
                ('HSNCode', models.CharField(blank=True, max_length=255, null=True)),
                ('TotalStock', models.DecimalField(blank=True, decimal_places=8, default=0.0, max_digits=20, null=True)),
                ('CreatedUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user%(class)s_objects', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'product',
                'verbose_name_plural': 'products',
                'db_table': 'products_product',
                'ordering': ('-CreatedDate', 'ProductID'),
                'unique_together': {('ProductCode', 'ProductID')},
            },
        ),
        migrations.CreateModel(
            name='StockTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=8, max_digits=20)),
                ('transaction_type', models.CharField(choices=[('purchase', 'Purchase'), ('sale', 'Sale')], max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('sub_variant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='product_inventory.subvariant')),
            ],
        ),
        migrations.CreateModel(
            name='Variant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='variants', to='product_inventory.product')),
            ],
            options={
                'unique_together': {('product', 'name')},
            },
        ),
        migrations.AddField(
            model_name='subvariant',
            name='variant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sub_variants', to='product_inventory.variant'),
        ),
        migrations.AlterUniqueTogether(
            name='subvariant',
            unique_together={('variant', 'option')},
        ),
    ]
