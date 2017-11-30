# -*- coding: utf-8 -*-
# Copyright 2017 KMEE
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Sped Fiscal',
    'summary': """
        SPED FISCAL""",
    'version': '11.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'KMEE,Odoo Community Association (OCA)',
    'website': 'www.kmee.com.br',
    'depends': [
        'l10n_br_base',
    ],
    'data': [
        'security/sped_fiscal.xml',
        'views/sped_fiscal.xml',
    ],
    'demo': [
        'demo/gerar_sped_fiscal.yml',
    ],
}
