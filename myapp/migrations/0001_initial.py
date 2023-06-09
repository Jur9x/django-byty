# Generated by Django 4.2 on 2023-05-10 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Majitel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Majitel',
                'verbose_name_plural': 'Majitelé',
                'ordering': ['osoba'],
            },
        ),
        migrations.CreateModel(
            name='Osoba',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmeno', models.CharField(help_text='Zadejte jméno osoby', max_length=45, verbose_name='Jméno')),
                ('prijmeni', models.CharField(help_text='Zadejte jméno osoby', max_length=45, verbose_name='Přijmení')),
                ('reputace', models.CharField(help_text='Zadejte jméno osoby', max_length=10, verbose_name='Reputatace')),
            ],
            options={
                'verbose_name': 'Osoba',
                'verbose_name_plural': 'Osoby',
                'ordering': ['reputace'],
            },
        ),
        migrations.CreateModel(
            name='Nemovitost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mesto', models.CharField(help_text='Zadejte jméno města', max_length=45, verbose_name='Město')),
                ('ulice', models.CharField(help_text='Zadejte jméno ulice', max_length=45, verbose_name='Ulice')),
                ('cena', models.PositiveIntegerField(help_text='Zadejte cenu', verbose_name='Cena')),
                ('fotka', models.ImageField(help_text='Nahrejte fotku nemovitosti', upload_to='nemovitost', verbose_name='Fotka nemovitosti')),
                ('majitel', models.ForeignKey(default=0, help_text='Vyberte majitele', on_delete=django.db.models.deletion.CASCADE, to='myapp.majitel', verbose_name='Osoba')),
            ],
            options={
                'verbose_name': 'Nemovitost',
                'verbose_name_plural': 'Nemovitosti',
                'ordering': ['majitel'],
            },
        ),
        migrations.CreateModel(
            name='Najemnik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osoba', models.ForeignKey(default=0, help_text='Vyberte najemnika', on_delete=django.db.models.deletion.CASCADE, to='myapp.osoba', verbose_name='Najemnik')),
            ],
            options={
                'verbose_name': 'Najemnik',
                'verbose_name_plural': 'Najemníci',
                'ordering': ['osoba'],
            },
        ),
        migrations.CreateModel(
            name='Najem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vyse_najmu', models.PositiveIntegerField(help_text='Zadejte výši nájmu', verbose_name='Výše nájmu')),
                ('datum_splatnosti', models.DateField(help_text='Zadejte datum splatnosti', verbose_name='Datum splatnosti')),
                ('najemnik', models.ForeignKey(default=0, help_text='Vyberte nájemníka', on_delete=django.db.models.deletion.CASCADE, to='myapp.najemnik', verbose_name='Nájemník')),
                ('nemovitost', models.ForeignKey(default=0, help_text='Vyberte nemovitost', on_delete=django.db.models.deletion.CASCADE, to='myapp.nemovitost', verbose_name='Nemovitost')),
            ],
            options={
                'verbose_name': 'Nájem',
                'verbose_name_plural': 'Nájmy',
                'ordering': ['nemovitost'],
            },
        ),
        migrations.AddField(
            model_name='majitel',
            name='osoba',
            field=models.ForeignKey(default=0, help_text='Vyberte majitele', on_delete=django.db.models.deletion.CASCADE, to='myapp.osoba', verbose_name='Majitel'),
        ),
    ]
