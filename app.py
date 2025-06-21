# app.py
import streamlit as st
import pandas as pd
from parser import parse_pdf_transactions

st.set_page_config(
    page_title="🔵 Data Scraper",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.sidebar.title("🔵 Data Scraper")
option = st.sidebar.radio(
    "Selecciona una opción", ["About", "Análisis de estados de cuenta"]
)

if option == "About":
    st.title("🏦 Acerca de la aplicación")

    st.markdown(
        """
        Esta herramienta permite analizar estados de cuenta bancarios en formato PDF.

        ### ¿Qué hace esta app?
        - Extrae transacciones desde PDFs generados por bancos.
        - Muestra la información como una tabla con **fecha**, **descripción** y **monto** en **GTQ**.
        - Puede utilizarse como ejemplo de scraping de datos estructurados desde documentos.

        ### Tecnologías utilizadas:
        - `Streamlit` para la interfaz gráfica.
        - `pdfplumber` para extraer el texto de los PDFs.
        - `pandas` para organizar los datos.

        ### Notas:
        - Los PDFs deben tener texto seleccionable. No funciona con imágenes escaneadas.
        - Este proyecto es solo con fines demostrativos.
        """
    )

elif option == "Análisis de estados de cuenta":
    st.title("📄 Análisis de Estado de Cuenta")

    uploaded_files = st.file_uploader(
        "Sube uno o más archivos PDF justo como los recibiste en tu Email",
        type="pdf",
        accept_multiple_files=True,
    )

    if uploaded_files:
        all_transactions = pd.DataFrame()
        for file in uploaded_files:
            transactions = parse_pdf_transactions(file)
            all_transactions = pd.concat(
                [all_transactions, transactions], ignore_index=True
            )

        if all_transactions.empty:
            st.warning("No se encontraron transacciones en los PDF(s).")
        else:
            st.success(
                f"✅ {len(all_transactions)} Transacciones extraídas correctamente"
            )

            with st.expander("Ver transacciones extraídas", expanded=False):
                st.dataframe(all_transactions)

            csv = all_transactions.to_csv(index=False).encode("utf-8")
            json = all_transactions.to_json(orient="records", force_ascii=False)

            col1, col2 = st.columns(2)

            with col1:
                st.download_button(
                    "📥 Descargar CSV",
                    csv,
                    "transacciones.csv",
                    "text/csv",
                    use_container_width=True,
                )

            with col2:
                st.download_button(
                    "📥 Descargar JSON",
                    json,
                    "transacciones.json",
                    "application/json",
                    use_container_width=True,
                )
