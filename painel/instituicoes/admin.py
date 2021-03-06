from django.contrib import admin
from instituicoes.models import Instituicoes, Categorias, InstAddresses, InstBankAccounts, InstBankPix, InstContacts
from instituicoes.forms import UploadModelForm

@admin.register(Categorias)
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

@admin.register(Instituicoes)
class InstituicoesAdmin(admin.ModelAdmin):
    list_display = ('inst_name', 'inst_cnpj',)
    search_fields = ('inst_name', 'inst_cnpj',)
    raw_id_fields = ('cat',)
    readonly_fields = ('scheme_image_tag',)
    form = UploadModelForm

@admin.register(InstAddresses)
class InstAddressesAdmin(admin.ModelAdmin):
    list_display = ('get_instituicao_nome',)
    raw_id_fields = ('inst',)

    def get_instituicao_nome(self, obj):
        return obj.inst.inst_name
    get_instituicao_nome.short_description = 'Instituição'
    get_instituicao_nome.admin_order_field = 'inst__inst_name'

@admin.register(InstBankAccounts)
class InstBankAccountsAdmin(admin.ModelAdmin):
    list_display = ('get_instituicao_nome', 'bank_name', 'bank_account_type',)
    raw_id_fields = ('inst',)

    def get_instituicao_nome(self, obj):
        return f'{obj.inst.inst_name} - {obj.bank_name} - {obj.bank_account_ag}'
    get_instituicao_nome.short_description = 'Conta Bancária'
    get_instituicao_nome.admin_order_field = 'inst__inst_name'

@admin.register(InstBankPix)
class InstBankPixAdmin(admin.ModelAdmin):
    list_display = ('get_instituicao_nome',)

    def get_instituicao_nome(self, obj):
        return f'{obj.account.inst.inst_name} - {obj.account.bank_name} - {obj.account.bank_account_ag} - Chave: {obj.pix_key}'
    get_instituicao_nome.short_description = 'Pix'
    get_instituicao_nome.admin_order_field = 'account__inst__inst_name'

@admin.register(InstContacts)
class InstContactsAdmin(admin.ModelAdmin):
    list_display = ('get_instituicao_nome', 'contact_comercial', 'contact_mobile', 'contact_email',)

    def get_instituicao_nome(self, obj):
        return obj.inst.inst_name
    get_instituicao_nome.short_description = 'Instituição'
    get_instituicao_nome.admin_order_field = 'inst__inst_name'