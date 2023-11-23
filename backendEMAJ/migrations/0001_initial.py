# Generated by Django 4.0 on 2023-11-21 00:08

import backendEMAJ.models
from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=100)),
                ('observacao', models.TextField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Pecas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('observacao', models.TextField()),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Processo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroProcesso', models.BigIntegerField()),
                ('representante', models.CharField(max_length=100)),
                ('escritorio', models.CharField(max_length=100)),
                ('observacao', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_uuid', models.CharField(max_length=100, null=True, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('usuario', models.CharField(max_length=100)),
                ('senha', models.CharField(max_length=100)),
                ('role', models.CharField(max_length=100)),
                ('imagem', models.URLField()),
                ('processos', djongo.models.fields.ArrayReferenceField(on_delete=djongo.models.fields.ArrayReferenceField._on_delete, to='backendEMAJ.processo')),
            ],
        ),
        migrations.CreateModel(
            name='Demanda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('escritorio', models.CharField(max_length=100)),
                ('assunto', models.TextField()),
                ('data', models.DateField()),
                ('processo', djongo.models.fields.ArrayReferenceField(on_delete=djongo.models.fields.ArrayReferenceField._on_delete, to='backendEMAJ.processo')),
            ],
        ),
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('resumo', models.TextField()),
                ('tipo', models.CharField(max_length=100)),
                ('forma', models.CharField(max_length=100)),
                ('providencia', models.CharField(max_length=100)),
                ('processo', djongo.models.fields.ArrayReferenceField(on_delete=djongo.models.fields.ArrayReferenceField._on_delete, to='backendEMAJ.processo')),
            ],
        ),
        migrations.CreateModel(
            name='Assistido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_uuid', models.CharField(max_length=100, null=True, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('rg', models.IntegerField(unique=True, verbose_name=20)),
                ('dataNasc', models.DateField(max_length=8)),
                ('email', models.EmailField(max_length=254)),
                ('estadoCivil', models.CharField(max_length=100)),
                ('telefone1', models.IntegerField()),
                ('telefone2', models.IntegerField()),
                ('profissao', models.CharField(max_length=20)),
                ('idade', models.IntegerField()),
                ('renda', models.FloatField()),
                ('dependentes', models.CharField(max_length=100)),
                ('representado', djongo.models.fields.ArrayField(model_container=backendEMAJ.models.Representado, model_form_class=backendEMAJ.models.RepresentadoForm, null=True)),
                ('endereco', models.TextField(max_length=50)),
                ('conhecido', models.CharField(max_length=100)),
                ('atendimento', djongo.models.fields.ArrayReferenceField(on_delete=djongo.models.fields.ArrayReferenceField._on_delete, to='backendEMAJ.atendimento')),
                ('demandas', djongo.models.fields.ArrayReferenceField(on_delete=djongo.models.fields.ArrayReferenceField._on_delete, to='backendEMAJ.demanda')),
                ('documentos', djongo.models.fields.ArrayReferenceField(on_delete=djongo.models.fields.ArrayReferenceField._on_delete, to='backendEMAJ.documento')),
                ('pecas', djongo.models.fields.ArrayReferenceField(on_delete=djongo.models.fields.ArrayReferenceField._on_delete, to='backendEMAJ.pecas')),
            ],
        ),
    ]
