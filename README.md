# 🏦 Data Scraper – Extractor de Estados de Cuenta en PDF

Esta aplicación desarrollada con **Streamlit** permite analizar **estados de cuenta bancarios en PDF** mediante técnicas de _data scraping_. Está pensada como una herramienta demostrativa para el procesamiento estructurado de datos desde documentos.

## 🚀 Funcionalidades

- **Análisis de PDFs**: Extrae automáticamente todas las transacciones desde uno o varios archivos PDF.
- **Procesamiento en lote**: Permite subir múltiples archivos simultáneamente y consolida todas las transacciones.
- **Exportación**: Descarga los resultados en formato CSV y JSON.
- **Colapsable**: La tabla de resultados se muestra en un panel desplegable para mejorar la navegación.
- **Detección de errores**: Muestra advertencias si no se detectan transacciones.

---

## 🧰 Tecnologías usadas

- `Python`
- `pdfplumber` para extracción de texto desde PDFs
- `pandas` para manipulación de datos
- `Streamlit` para la interfaz web

---

## 📦 Instalación local

```bash
git clone https://github.com/menene/bank-scraper
cd bank-scraper
pip install -r requirements.txt
streamlit run app.py
