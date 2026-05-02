# Përdor imazhin bazë të Python
FROM python:3.9-slim

# Vendos direktorinë e punës
WORKDIR /app

# Kopjo file-t e projektit
COPY . .

# Instalimi i varësive
RUN pip install --no-cache-dir -r requirements.txt

# Ekspozimi i portit për Streamlit
EXPOSE 8501

# Komanda default për të nisur aplikacionin Streamlit
CMD ["streamlit", "run", "app/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]
