# Använd en basimage med Python
FROM python:3.9-slim

# Ställ in arbetskatalog
WORKDIR /app

# Kopiera requirements.txt och installera beroenden
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiera källkoden till containern
COPY . .

# Exponera Flask-porten
EXPOSE 5000

# Sätt miljövariabeln för Flask
ENV FLASK_APP=app.py

# Definiera körkommandot
CMD ["flask", "run", "--host=0.0.0.0"]
