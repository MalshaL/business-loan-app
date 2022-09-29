FROM python:3.8
# copy the req file to app directory in the docker image
COPY requirements.txt /xero_api/requirements.txt
WORKDIR /xero_api
RUN pip install -r requirements.txt --use-deprecated=legacy-resolver
COPY . /xero_api
EXPOSE 3006
ENTRYPOINT ["python"]
CMD ["main.py", "--host=0.0.0.0"]