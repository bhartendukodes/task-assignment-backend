FROM python:3.11-slim

WORKDIR /app

# Install dependencies
COPY requirements-lite.txt .
RUN pip install --no-cache-dir -r requirements-lite.txt

# Copy application
COPY . .

# Expose port
EXPOSE 8000

# Run application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]