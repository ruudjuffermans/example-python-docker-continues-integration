# set base image (host OS)
FROM python:3.8
WORKDIR /app

# Install our requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ .


# command to run on container start
CMD [ "python", "./run.py" ]

