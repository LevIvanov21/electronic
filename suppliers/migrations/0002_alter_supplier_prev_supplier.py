import django.db.models.deletion
import suppliers.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("suppliers", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="supplier",
            name="prev_supplier",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="prev",
                to="suppliers.supplier",
                validators=[suppliers.models.validate_prev_supplier],
                verbose_name="Поставщик",
            ),
        ),
    ]
