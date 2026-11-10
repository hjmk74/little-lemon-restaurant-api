from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):
    initial = True
    dependencies = []
    operations = [
        migrations.CreateModel(
            name="MenuItem",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=100)),
                ("price", models.DecimalField(decimal_places=2, max_digits=6, validators=[django.core.validators.MinValueValidator(0)])),
                ("inventory", models.PositiveIntegerField(default=0)),
                ("description", models.TextField(blank=True)),
            ],
            options={"ordering": ["title"]},
        ),
        migrations.CreateModel(
            name="Booking",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("first_name", models.CharField(max_length=100)),
                ("reservation_date", models.DateField()),
                ("reservation_slot", models.PositiveSmallIntegerField(default=10)),
            ],
            options={"ordering": ["reservation_date", "reservation_slot"]},
        ),
    ]
