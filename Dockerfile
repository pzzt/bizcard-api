# Usa un'immagine Python leggera
FROM python:3.11-slim

# Imposta la directory di lavoro
WORKDIR /app

# Copia i requisiti e installali
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia il codice dell'app
COPY ./app ./app

# Espone la porta 8000
EXPOSE 8000

# Comando per avviare il server
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
