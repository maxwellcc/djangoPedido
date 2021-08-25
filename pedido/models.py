from decimal import Decimal

from django.core.validators import MinValueValidator
from django.db import models


class Cliente(models.Model):
    cod_cli = models.BigAutoField(
        primary_key=True,
    )
    nome_cli = models.CharField(
        max_length=40,
        null=False,
        verbose_name='nome do cliente',
    )
    fone = models.CharField(
        max_length=15,
        null=False,
        verbose_name='telefone',
    )
    rua = models.CharField(
        max_length=40,
        null=False,
        verbose_name='nome da rua',
    )
    numero = models.IntegerField(
        null=False,
        verbose_name='número',
    )
    bairro = models.CharField(
        max_length=20,
        null=False,
        verbose_name='bairro',
    )
    complemento = models.CharField(
        max_length=20,
        null=True,
        blank=True,
        verbose_name='complemento',
    )
    cidade = models.CharField(
        max_length=20,
        null=False,
        verbose_name='cidade',
    )
    uf = models.CharField(
        max_length=2,
        null=False,
        verbose_name='unidade federativa',
        default='PB',
    )


class Produto(models.Model):
    cod_prod = models.BigAutoField(
        primary_key=True,
    )
    desc_prod = models.CharField(
        max_length=20,
        null=False,
        verbose_name='descrição do produto',
    )
    unidade = models.CharField(
        max_length=10,
        null=False,
        verbose_name='unidade',
    )
    valor_prod = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        null=False,
        verbose_name='valor do produto',
        validators=[
            MinValueValidator(Decimal('0.00'))
        ]
    )


class Vendedor(models.Model):
    cod_vend = models.BigAutoField(
        primary_key=True,
    )
    nome_vend = models.CharField(
        max_length=40,
        null=False,
        verbose_name='nome do vendedor',
    )
    salario = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        null=False,
        verbose_name='salário',
    )
    faixa_comissao = models.CharField(
        max_length=1,
        null=False,
        verbose_name='faixa de comissao',
        choices=(
            ('A', 'Faixa A'),
            ('B', 'Faixa B'),
            ('C', 'Faixa C'),
        )
    )


class Pedido(models.Model):
    num_pod = models.BigAutoField(
        primary_key=True,
    )
    data_ped = models.DateField(
        null=False,
        verbose_name='data',
    )
    prazo_entrega = models.DateField(
        null=True,
        blank=True,
        verbose_name='data de entrega',
    )
    cliente = models.ForeignKey(
        Cliente,
        null=False,
        verbose_name='cliente',
        on_delete=models.CASCADE,
    )
    vendedor = models.ForeignKey(
        Vendedor,
        null=False,
        verbose_name='vendedor',
        on_delete=models.CASCADE,
    )


class ItemPedido(models.Model):
    pedido = models.ForeignKey(
        Pedido,
        null=False,
        verbose_name='pedido',
        on_delete=models.CASCADE,
    )
    produto = models.ForeignKey(
        Produto,
        null=False,
        verbose_name='produto',
        on_delete=models.CASCADE,
    )
    quantidade = models.PositiveIntegerField(
        null=False,
        verbose_name='quantidade do produto',
    )

    class Meta:
        unique_together = ('pedido', 'produto')
