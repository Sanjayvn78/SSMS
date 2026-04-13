# Generated manually to rename timetable fields from period1-7 to p1-7

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_timetable_subject_remove_timetable_time_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='timetable',
            old_name='period1',
            new_name='p1',
        ),
        migrations.RenameField(
            model_name='timetable',
            old_name='period2',
            new_name='p2',
        ),
        migrations.RenameField(
            model_name='timetable',
            old_name='period3',
            new_name='p3',
        ),
        migrations.RenameField(
            model_name='timetable',
            old_name='period4',
            new_name='p4',
        ),
        migrations.RenameField(
            model_name='timetable',
            old_name='period5',
            new_name='p5',
        ),
        migrations.RenameField(
            model_name='timetable',
            old_name='period6',
            new_name='p6',
        ),
        migrations.RenameField(
            model_name='timetable',
            old_name='period7',
            new_name='p7',
        ),
    ]