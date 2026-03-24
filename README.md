<think>

</think>

# 🎨 Modern UX Theme - Global para Odoo 16 Community

Tema global e universal que funciona com **TODOS os módulos** automaticamente.

## ✨ Características

- ✅ Funciona com QUALQUER módulo (MRP, Sale, Purchase, Stock, Account, Repair, etc.)
- ✅ Depende APENAS do módulo `web`
- ✅ Cores Indigo modernas (#4f46e5)
- ✅ Contraste WCAG AA (acessibilidade)
- ✅ Totalmente responsivo
- ✅ Rollback fácil se necessário

## 📦 Instalação

```bash
# 1. Copiar para pasta de addons
cp -r modern_ux_theme_global /opt/odoo/custom_addons/

# 2. Reiniciar Odoo em modo dev
./odoo-bin --dev=xml,qweb,scss --workers=0 -d seu_db

# 3. Instalar módulo
./odoo-bin -d seu_db -i modern_ux_theme_global --stop-after-init

# 4. Acessar e recarregar (Ctrl+Shift+R)
