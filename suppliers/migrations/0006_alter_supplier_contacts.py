import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("suppliers", "0005_alter_supplier_options_remove_supplier_city_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="supplier",
            name="contacts",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="contacts",
                to="suppliers.contacts",
                verbose_name="Контакты",
            ),
        ),
    ]
