# Use the official Python image from the Docker Hub
FROM python:3.12

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy the rest of the application
COPY . /app/

# Run the Django collectstatic command to gather static files
RUN python manage.py collectstatic --noinput

# Expose the Django app's port
EXPOSE 8000

# Start the Django app server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]