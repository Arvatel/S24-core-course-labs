 # Use the official Python image from the Docker Hub
FROM python:3-alpine3.15
LABEL authors="arvatel"

# Create a non-root user
RUN adduser -D pythonuser
USER pythonuser

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY app.py /app/app.py
COPY templates/index.html /app/templates/index.html
COPY requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV FLASK_APP=app.py

# Run app.py when the container launches
CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]