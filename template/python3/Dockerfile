# Use Python 3 base image
FROM python:3.8-alpine

# Install the dependencies for mariadb-connector-c
RUN apk add --no-cache mariadb-connector-c-dev gcc musl-dev

# Copy handler code and requirements
WORKDIR /home/app
COPY function/requirements.txt .
RUN pip install -r requirements.txt --target=/home/app/python

COPY function/handler.py .

# Additional OpenFaaS configuration (if applicable)
ENV fprocess="python3 handler.py"
EXPOSE 8080
CMD ["fwatchdog"]
