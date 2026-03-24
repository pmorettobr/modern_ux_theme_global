# -*- coding: utf-8 -*-
# modern_ux_theme_global/__manifest__.py
{
    'name': 'Modern UX Theme - Global',
    'version': '16.0.1.0.0',
    'category': 'Theme/Backend',
    'summary': 'Tema global seguro para Odoo 16 Community - Funciona com TODOS os módulos',
    'description': '''
        Tema GLOBAL e universal para Odoo 16 Community Edition:
        
        ✨ CARACTERÍSTICAS:
        • Funciona com QUALQUER módulo (MRP, Sale, Purchase, Stock, Account, Repair, etc.)
        • Depende APENAS do módulo 'web' (base do sistema)
        • Cores modernas Indigo (#4f46e5) com contraste WCAG AA
        • Border radius suave (8-12px) para visual moderno
        • Totalmente responsivo (mobile, tablet, desktop)
        • Seguro - sem override de variáveis de sizing do Odoo
        
        🔒 SEGURANÇA:
        • Rollback fácil se necessário
        • Não modifica arquivos do core do Odoo
        • Compatível com atualizações futuras
    ''',
    'author': 'Seu Nome',
    'website': 'https://seusite.com',
    'license': 'LGPL-3',
    'depends': ['web'],
    'assets': {
        # ✅ Override APENAS de cores (sem unidades de medida)
        #'web._assets_primary_variables': [
         #   ('prepend', 'modern_ux_theme_global/static/src/scss/_variables_global.scss'),
        #],
        # ✅ CSS explícito para sizing (border-radius, padding, etc.)
        'web.assets_backend': [
            ('append', 'modern_ux_theme_global/static/src/scss/main.scss'),
        ],
        # ✅ Login page também usa o tema
        'web.assets_frontend': [
            ('append', 'modern_ux_theme_global/static/src/scss/main.scss'),
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
