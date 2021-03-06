# Generated by Django 4.0.1 on 2022-01-14 00:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('budget', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IncomeExpense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('Wydatek', 'Wydatek'), ('Wpływ', 'Wpływ')], max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('category', models.CharField(choices=[('Jedzenie', 'Jedzenie'), ('Podróże', 'Podróże'), ('Zakupy', 'Zakupy'), ('Rachunki', 'Rachunki'), ('Rozrywka', 'Rozrywka'), ('Inne', 'Inne')], default='Wybierz', max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='expense',
            name='category',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='project',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Expense',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
    ]
