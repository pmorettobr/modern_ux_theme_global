# modern_ux_theme_global/__manifest__.py
{
    'name': 'Modern UX Theme - Global',
    'version': '16.0.1.0.0',
    'category': 'Theme/Backend',
    'summary': 'Tema global para Odoo 16 Community - Funciona com TODOS os módulos',
    'description': '''
        Tema GLOBAL e universal para Odoo 16 Community Edition:
        
        ✨ CARACTERÍSTICAS:
        • Funciona com QUALQUER módulo (MRP, Sale, Purchase, Stock, Account, Repair, etc.)
        • Depende APENAS do módulo 'web' (base do sistema)
        • Usa classes base estáveis (não muda com updates de módulos)
        • Cores modernas Indigo (#4f46e5) com contraste WCAG AA
        • Border radius suave (8px) para visual moderno
        • Sombras sutis para profundidade visual
        • Badges estilo pill para melhor escaneabilidade
        • Hover effects com feedback visual claro
        • Totalmente responsivo (mobile, tablet, desktop)
        • Áreas de toque otimizadas (44px mínimo)
        
        🔒 SEGURANÇA:
        • Rollback fácil se necessário
        • Não modifica arquivos do core do Odoo
        • Compatível com atualizações futuras
        • Testado em ambiente de produção
        
        📦 INSTALAÇÃO:
        • Instale UMA VEZ e funciona para TODOS os módulos
        • Não requer configuração adicional
        • Funciona com módulos instalados no futuro automaticamente
    ''',
    'author': 'Seu Nome',
    'website': 'https://seusite.com',
    'license': 'LGPL-3',
    
    # ✅ DEPENDÊNCIA ÚNICA E GLOBAL
    'depends': ['web'],
    
    'assets': {
        # 1. Variáveis (carregadas PRIMEIRO - antes de tudo)
        'web._assets_primary_variables': [
            ('prepend', 'modern_ux_theme_global/static/src/scss/_variables_global.scss'),
        ],
        
        # 2. Estilos base (carregados em TODAS as views backend)
        'web.assets_backend': [
            ('append', 'modern_ux_theme_global/static/src/scss/_components_base.scss'),
            ('append', 'modern_ux_theme_global/static/src/scss/_views_all.scss'),
        ],
        
        # 3. Frontend (login page - opcional)
        'web.assets_frontend': [
            ('append', 'modern_ux_theme_global/static/src/scss/main.scss'),
        ],
    },
    
    'images': ['static/description/preview.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
