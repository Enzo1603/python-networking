FROM python:3.12-alpine

WORKDIR /app


# Setzen von Umgebungsvariablen
# - PYTHONDONTWRITEBYTECODE verhindert, dass Python .pyc Dateien erstellt werden
# - PYTHONUNBUFFERED stellt sicher, dass Python-Logs sofort in den Docker-Log ausgegeben werden.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

ADD . /app/


# Installieren von Poetry und Python-Dependendecies
RUN pip install --trusted-host pypi.python.org --no-cache-dir poetry
RUN poetry config virtualenvs.create false && \
    poetry install --no-dev

# Entfernen der Build-Abhängigkeiten, um die Größe des Images zu reduzieren
# RUN apk del build-base

# Ports veröffentlichen
EXPOSE 7000
EXPOSE 7001
EXPOSE 7002/udp

# Umgebungsvariablen setzen, um Flask im Produktionsmodus zu starten
ENV FLASK_ENV=production

# Starten des Servers
# CMD ["flask", "run", "--host=0.0.0.0"]
CMD ["python", "/app/app.py"]
