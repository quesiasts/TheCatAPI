from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(help_text='armazena o endereço da foto')),
                ('breed', models.CharField(help_text='armazena a raça', max_length=100)),
                ('object', models.CharField(blank=True, help_text='armazena o tipo do objeto presente na foto', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CatBreed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='representa o nome da raça', max_length=100)),
                ('origin', models.CharField(help_text='origem da raça', max_length=100)),
                ('temperament', models.CharField(help_text='temperamentos da raça', max_length=200)),
            ],
        ),
    ]