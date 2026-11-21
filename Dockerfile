
FROM python:3.12-slim

WORKDIR /app

COPY mainn.py .
COPY test_mainn.py .

RUN pip install pytest

CMD ["python", "mainn.py"]
