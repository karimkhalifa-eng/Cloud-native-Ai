FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY agent.py tools.py /app/

EXPOSE 8000

# Make sure CMD calls uvicorn, NOT python agent.py
CMD ["uvicorn", "agent:app", "--host", "0.0.0.0", "--port", "8000"]