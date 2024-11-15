import django.db.models.deletion
import suppliers.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Supplier",
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
                ("name", models.CharField(max_length=150, verbose_name="название")),
                ("email", models.EmailField(max_length=254, verbose_name="email")),
                ("country", models.TextField(max_length=70, verbose_name="страна")),
                ("city", models.TextField(max_length=70, verbose_name="город")),
                ("street", models.TextField(max_length=150, verbose_name="улица")),
                (
                    "house_number",
                    models.TextField(max_length=10, verbose_name="номер дома"),
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
                (
                    "debt",
                    models.DecimalField(
                        decimal_places=2,
                        default=0.0,
                        max_digits=20,
                        verbose_name="задолженность перед поставщиком",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="время создания"
                    ),
                ),
                (
                    "prev_supplier",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="suppliers.supplier",
                        validators=[suppliers.models.validate_prev_supplier],
                        verbose_name="Поставщик",
                    ),
                ),
            ],
            options={
                "verbose_name": "поставщик",
                "verbose_name_plural": "поставщики",
                "ordering": ["country"],
            },
        ),
    ]
