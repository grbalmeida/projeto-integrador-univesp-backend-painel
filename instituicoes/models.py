# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Categorias(models.Model):
    cat_id = models.AutoField(primary_key=True)
    nome = models.CharField(unique=True, max_length=100, blank=True, null=True)
    is_active = models.BooleanField("Publicado?", default=True)

    def __str__(self):
        return self.nome or ''

    class Meta:
        managed = False
        db_table = 'categorias'
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"


class InstAddresses(models.Model):
    addr_id = models.AutoField(primary_key=True)
    inst = models.ForeignKey('Instituicoes', models.DO_NOTHING, blank=True, null=True)
    addr_zipcode = models.CharField(max_length=8, blank=True, null=True)
    addr_street = models.CharField(max_length=100, blank=True, null=True)
    addr_number = models.CharField(max_length=50, blank=True, null=True)
    addr_complement = models.CharField(max_length=100, blank=True, null=True)
    addr_district = models.CharField(max_length=100, blank=True, null=True)
    addr_city = models.CharField(max_length=100, blank=True, null=True)
    addr_state = models.CharField(max_length=100, blank=True, null=True)
    addr_country = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField("Publicado?", default=True)

    def __str__(self):
        return self.inst.inst_name or ''

    class Meta:
        managed = False
        db_table = 'inst_addresses'
        verbose_name = "Endereço"
        verbose_name_plural = "Endereços"


class InstBankAccounts(models.Model):
    account_id = models.AutoField(primary_key=True)
    inst = models.ForeignKey('Instituicoes', models.DO_NOTHING, blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    bank_account_ag = models.CharField(max_length=8, blank=True, null=True)
    bank_account_conta = models.CharField(max_length=100, blank=True, null=True)
    bank_account_type = models.TextField(blank=True, null=True)  # This field type is a guess.
    is_active = models.BooleanField("Publicado?", default=True)

    def __str__(self):
        return f'{self.inst.inst_name} - {self.bank_name} - {self.bank_account_ag}' or ''

    class Meta:
        managed = False
        db_table = 'inst_bank_accounts'
        verbose_name = "Conta Bancária"
        verbose_name_plural = "Contas Bancárias"


class InstBankPix(models.Model):
    pix_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(InstBankAccounts, models.DO_NOTHING, blank=True, null=True)
    pix_key = models.CharField(max_length=100, blank=True, null=True)
    qrcode_file = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField("Publicado?", default=True)

    def __str__(self):
        return f'{self.account.inst.inst_name} - {self.account.bank_name} - {self.account.bank_account_ag} - Chave: {self.pix_key}' or ''

    class Meta:
        managed = False
        db_table = 'inst_bank_pix'
        verbose_name = "Pix"
        verbose_name_plural = "Pix"


class InstContacts(models.Model):
    contact_id = models.AutoField(primary_key=True)
    inst = models.ForeignKey('Instituicoes', models.DO_NOTHING, blank=True, null=True)
    contact_comercial = models.CharField(max_length=11, blank=True, null=True)
    contact_mobile = models.CharField(max_length=12, blank=True, null=True)
    contact_email = models.CharField(max_length=100, blank=True, null=True)
    contact_site = models.CharField(max_length=100, blank=True, null=True)
    contact_instagram = models.CharField(max_length=100, blank=True, null=True)
    contact_facebook = models.CharField(max_length=100, blank=True, null=True)
    contact_twitter = models.CharField(max_length=100, blank=True, null=True)
    contact_linkedin = models.CharField(max_length=100, blank=True, null=True)
    contact_youtube = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField("Publicado?", default=True)

    def __str__(self):
        return f'{self.inst.inst_name} - {self.contact_comercial} - {self.contact_mobile} - {self.contact_email}'

    class Meta:
        managed = False
        db_table = 'inst_contacts'
        verbose_name = "Contato"
        verbose_name_plural = "Contatos"


class Instituicoes(models.Model):
    inst_id = models.AutoField(primary_key=True)
    inst_name = models.CharField(max_length=255, blank=True, null=True)
    inst_cnpj = models.CharField(unique=True, max_length=18, blank=True, null=True)
    logo = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=1000, blank=True, null=True)
    cat = models.ForeignKey(Categorias, models.DO_NOTHING)
    alt_logo = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField("Publicado?", default=True)

    def __str__(self):
        return self.inst_name or ''

    class Meta:
        managed = False
        db_table = 'instituicoes'
        verbose_name = "Instituição"
        verbose_name_plural = "Instituições"