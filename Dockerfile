 # change if required

FROM python:latest
LABEL maintainer="bhawick@outlook.com"

WORKDIR /data
COPY ./requirements.txt .
# network analysis workshop
#COPY ./workspace/setup.py .


# Install node via NPM
# see https://github.com/jupyterlab/jupyterlab/issues/4327
RUN apt update && apt-get install -y npm
RUN npm install -g npm

# Install Jupyter
RUN pip install jupyter && pip install jupyterlab && pip install jupytext
RUN pip install --no-cache-dir -r requirements.txt

# Service available from 8888
EXPOSE 8888
