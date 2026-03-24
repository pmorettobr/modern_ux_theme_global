# modern_ux_theme_global/__manifest__.py
{
    'name': 'Modern UX Theme - Global',
    'version': '16.0.1.0.0',
    'category': 'Theme/Backend',
    'summary': 'Tema global seguro para Odoo 16 Community',
    'depends': ['web'],
    
    # ✅ REMOVER web._assets_primary_variables - NÃO override variáveis!
    'assets': {
        # ❌ REMOVER ESTE BLOCO INTEIRO:
        # 'web._assets_primary_variables': [
        #     ('prepend', 'modern_ux_theme_global/static/src/scss/_variables_global.scss'),
        # ],
        
        # ✅ MANTER APENAS assets_backend com CSS explícito
        'web.assets_backend': [
            ('append', 'modern_ux_theme_global/static/src/scss/main.scss'),
        ],
        'web.assets_frontend': [
            ('append', 'modern_ux_theme_global/static/src/scss/main.scss'),
        ],
    },
    'installable': True,
    'application': False,
}
