from django.db import migrations


def ensure_menuitem_table(apps, schema_editor):
    MenuItem = apps.get_model("restaurant", "MenuItem")
    table_name = MenuItem._meta.db_table
    existing_tables = schema_editor.connection.introspection.table_names()
    if table_name not in existing_tables:
        schema_editor.create_model(MenuItem)


class Migration(migrations.Migration):
    dependencies = [("restaurant", "0001_initial")]
    operations = [
        migrations.RunPython(ensure_menuitem_table, migrations.RunPython.noop),
    ]
