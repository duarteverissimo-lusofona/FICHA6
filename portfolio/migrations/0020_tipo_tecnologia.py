# Generated for ETAPA 5 - TipoTecnologia and Tecnologia.tipo relation

import django.db.models.deletion
from django.db import migrations, models


def migrar_tipos_tecnologia(apps, schema_editor):
    TipoTecnologia = apps.get_model("portfolio", "TipoTecnologia")
    Tecnologia = apps.get_model("portfolio", "Tecnologia")

    tipos_base = {
        "Frontend": "Tecnologias usadas na interface e apresentação da aplicação.",
        "Backend": "Tecnologias usadas na lógica do servidor.",
        "Base de Dados": "Tecnologias usadas para guardar e consultar dados.",
        "Storage": "Tecnologias usadas para guardar ficheiros estáticos ou media.",
        "Outros": "Tecnologias de apoio ao desenvolvimento.",
    }

    for nome, descricao in tipos_base.items():
        TipoTecnologia.objects.get_or_create(
            nome=nome,
            defaults={"descricao": descricao},
        )

    for tecnologia in Tecnologia.objects.all():
        nome_tipo = (tecnologia.tipo or "").strip() or "Outros"
        if nome_tipo == "Outro":
            nome_tipo = "Outros"

        tipo, _ = TipoTecnologia.objects.get_or_create(nome=nome_tipo)
        tecnologia.tipo_tecnologia = tipo
        tecnologia.save(update_fields=["tipo_tecnologia"])


class Migration(migrations.Migration):

    dependencies = [
        ("portfolio", "0019_remove_unidadecurricular_licenciatura_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="TipoTecnologia",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100, unique=True)),
                ("descricao", models.TextField(blank=True)),
            ],
            options={
                "ordering": ["nome"],
            },
        ),
        migrations.AddField(
            model_name="tecnologia",
            name="tipo_tecnologia",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="portfolio.tipotecnologia",
            ),
        ),
        migrations.RunPython(
            migrar_tipos_tecnologia,
            reverse_code=migrations.RunPython.noop,
        ),
        migrations.RemoveField(
            model_name="tecnologia",
            name="tipo",
        ),
        migrations.RenameField(
            model_name="tecnologia",
            old_name="tipo_tecnologia",
            new_name="tipo",
        ),
        migrations.AlterField(
            model_name="tecnologia",
            name="tipo",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="tecnologias",
                to="portfolio.tipotecnologia",
            ),
        ),
    ]
