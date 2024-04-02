# Get docker image of python 3.9
FROM python:3.9

# Define working directory on docker container to /code
WORKDIR /code

# Install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy local folder to docker
COPY . .

# Expose 8000 port externally
EXPOSE 8000

# Use gunicorn on port 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "construction_project.wsgi:application"]