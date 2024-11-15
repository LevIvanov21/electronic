import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("suppliers", "0004_rename_contact_contacts_alter_contacts_options"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="supplier",
            options={
                "ordering": ["name"],
                "verbose_name": "поставщик",
                "verbose_name_plural": "поставщики",
            },
        ),
        migrations.RemoveField(
            model_name="supplier",
            name="city",
        ),
        migrations.RemoveField(
            model_name="supplier",
            name="country",
        ),
        migrations.RemoveField(
            model_name="supplier",
            name="email",
        ),
        migrations.RemoveField(
            model_name="supplier",
            name="house_number",
        ),
        migrations.RemoveField(
            model_name="supplier",
            name="product_date",
        ),
        migrations.RemoveField(
            model_name="supplier",
            name="product_model",
        ),
        migrations.RemoveField(
            model_name="supplier",
            name="product_name",
        ),
        migrations.RemoveField(
            model_name="supplier",
            name="street",
        ),
        migrations.AlterField(
            model_name="supplier",
            name="contacts",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="contacts",
                to="suppliers.contacts",
                verbose_name="Контакты",
            ),
        ),
        migrations.AlterField(
            model_name="supplier",
            name="product",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="product",
                to="suppliers.product",
                verbose_name="Продукт",
            ),
        ),
    ]
