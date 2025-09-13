FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt ./requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY WindDirToXDir.json ./WindDirToXDir.json
COPY WindDirToYDir.json ./WindDirToYDir.json
COPY code_lluvia.json   ./code_lluvia.json
COPY pipeline.joblib    ./pipeline.joblib
COPY inferencia.py      ./inferencia.py

CMD [ "python", "./inferencia.py" ]
