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
COPY firebase /app/firebase
COPY book-b860d-4c401e9f8a95.json /app/

RUN python manage.py collectstatic --noinput

ENV GOOGLE_APPLICATION_CREDENTIALS=/app/book-b860d-4c401e9f8a95.json



# Make port 8000 available to the world outside this container
EXPOSE 8000

# Run the Django application
CMD ["gunicorn", "book_project.wsgi:application", "--bind", "0.0.0.0:8000"]
