# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.12
# run in un buffered mode, which is recommended with python running in docker containers
# doesn't buffer outputs, just prints directly
ENV PYTHONUNBUFFERED 1

ENV PYTHONDONTWRITEBYTECODE 1
# create root directory for our project in the container
RUN mkdir /app

# Set the working directory to /music_service
WORKDIR /app

# Install any needed packages specified in requirements.txt
RUN pipenv install --upgrade pip

COPY requirements.txt /app/

RUN pip install -r requirements.txt
# Copy the current directory contents into the container at /music_service
COPY . /app/

ENTRYPOINT ["python3"]
CMD ["manage.py", "runserver", "0.0.0.0:8080"]