FROM ibmfunctions/action-python-v3.7

COPY . /src

WORKDIR /src
RUN pip install -r requirements.txt

