#!/bin/bash

echo "Instalando dependencias..."

pip install -r requirements.txt

echo "Iniciando AluraAgente..."

streamlit run streamlit_app.py --server.port 8501 --server.address 0.0.0.0