import django.db.models.deletion
import suppliers.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("suppliers", "0002_alter_supplier_prev_supplier"),
    ]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="email")),
                ("country", models.TextField(max_length=70, verbose_name="страна")),
                ("city", models.TextField(max_length=70, verbose_name="город")),
                ("street", models.TextField(max_length=150, verbose_name="улица")),
                (
                    "house_number",
                    models.TextField(max_length=10, verbose_name="номер дома"),
                ),
            ],
            options={
                "verbose_name": "контакт",
                "verbose_name_plural": "контакты",
                "ordering": ["country"],
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "product_name",
                    models.CharField(max_length=250, verbose_name="название продукта"),
                ),
                (
                    "product_model",
                    models.CharField(max_length=50, verbose_name="модель продукта"),
                ),
                (
                    "product_date",
                    models.DateField(verbose_name="дата выхода продукта на рынок"),
                ),
            ],
            options={
                "verbose_name": "продукт",
                "verbose_name_plural": "продукты",
                "ordering": ["product_name"],
            },
        ),
        migrations.AddField(
            model_name="supplier",
            name="contacts",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="contacts",
                to="suppliers.contact",
                validators=[suppliers.models.validate_prev_supplier],
                verbose_name="Контакты",
            ),
        ),
        migrations.AddField(
            model_name="supplier",
            name="product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product",
                to="suppliers.product",
                validators=[suppliers.models.validate_prev_supplier],
                verbose_name="Продукт",
            ),
        ),
    ]
