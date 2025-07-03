FROM python:3.12.4

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1




# Upgrade libpq-dev
RUN apt-get update \
    && apt-get install --only-upgrade -y libpq-dev \
    && apt-get clean

# Install Python dependencies (this step will be cached if requirements.txt doesn't change)
COPY requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r /code/requirements.txt

# Set the working directory in the container
WORKDIR /code

# Copy the Django project files to the working directory
COPY ./app /code/app
COPY ./gpt_app /code/gpt_app
COPY ./manage.py /code/
COPY build.sh /code/

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port on which your Django app will run
EXPOSE 8000

# Run the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]