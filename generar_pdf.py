"""
Script para generar el PDF del proyecto de lógica fuzzy
"""

import markdown
import pdfkit
from pathlib import Path

def generar_pdf():
    """Convierte el archivo markdown a PDF"""
    
    # Leer el archivo markdown
    with open('informe_proyecto.md', 'r', encoding='utf-8') as f:
        markdown_content = f.read()
    
    # Convertir markdown a HTML
    html = markdown.markdown(markdown_content, extensions=['tables', 'codehilite'])
    
    # CSS para mejorar el formato
    css_style = """
    <style>
    body {
        font-family: Arial, sans-serif;
        line-height: 1.6;
        margin: 40px;
        color: #333;
    }
    h1 {
        color: #2c3e50;
        border-bottom: 3px solid #3498db;
        padding-bottom: 10px;
    }
    h2 {
        color: #34495e;
        border-bottom: 1px solid #bdc3c7;
        padding-bottom: 5px;
    }
    h3 {
        color: #7f8c8d;
    }
    table {
        border-collapse: collapse;
        width: 100%;
        margin: 20px 0;
    }
    th, td {
        border: 1px solid #ddd;
        padding: 12px;
        text-align: left;
    }
    th {
        background-color: #f2f2f2;
        font-weight: bold;
    }
    code {
        background-color: #f4f4f4;
        padding: 2px 4px;
        border-radius: 3px;
        font-family: 'Courier New', monospace;
    }
    pre {
        background-color: #f8f8f8;
        padding: 15px;
        border-radius: 5px;
        overflow-x: auto;
    }
    blockquote {
        border-left: 4px solid #3498db;
        margin: 0;
        padding-left: 20px;
        font-style: italic;
    }
    </style>
    """
    
    # Combinar CSS y HTML
    html_completo = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Sistema de Control Fuzzy para Cálculo de Propinas</title>
        {css_style}
    </head>
    <body>
        {html}
    </body>
    </html>
    """
    
    # Configuración para wkhtmltopdf
    options = {
        'page-size': 'A4',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'no-outline': None,
        'enable-local-file-access': None
    }
    
    try:
        # Generar PDF
        pdfkit.from_string(html_completo, 'Proyecto_Logica_Fuzzy.pdf', options=options)
        print("✅ PDF generado exitosamente: Proyecto_Logica_Fuzzy.pdf")
        
    except Exception as e:
        print(f"❌ Error al generar PDF: {e}")
        print("💡 Alternativa: Usa pandoc o convierte manualmente el archivo markdown")
        
        # Guardar HTML como alternativa
        with open('informe_proyecto.html', 'w', encoding='utf-8') as f:
            f.write(html_completo)
        print("📄 Archivo HTML generado como alternativa: informe_proyecto.html")

if __name__ == "__main__":
    print("Generando PDF del proyecto de lógica fuzzy...")
    generar_pdf()