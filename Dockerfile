# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . /app/

# Copy the Firebase credentials into the container
COPY firebase/firebase-adminsdk.json /app/firebase/firebase-adminsdk.json
COPY books/geminiaiintegration-74ba0e9e6da4.json /app/book_project/books/

# COPY books/geminiaiintegration-74ba0e9e6da4.json /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Set environment variable for Google application credentials
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/firebase/firebase-adminsdk.json

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the Django application
CMD ["gunicorn", "book_project.wsgi:application", "--bind", "0.0.0.0:8000"]
