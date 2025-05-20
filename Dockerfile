# Use an official Python runtime as a parent image
FROM python:3.13-alpine

# Set the working directory in the container
WORKDIR /app

# Install Poetry
RUN pip install poetry

# Copy only the Poetry files first to leverage Docker caching
COPY pyproject.toml poetry.lock ./

# Install dependencies without creating a virtual environment
RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi --no-root

# Copy the rest of the application code
COPY . .

# Expose the application port
EXPOSE 8000

# Run the application with uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
