FROM python:3.10

WORKDIR /app

COPY . /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

#Run server
CMD ["uvicorn", "test-api:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]