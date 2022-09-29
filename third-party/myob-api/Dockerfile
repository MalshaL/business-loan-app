FROM python:3.8
# copy the req file to app directory in the docker image
COPY requirements.txt /myob_api/requirements.txt
WORKDIR /myob_api
RUN pip install -r requirements.txt --use-deprecated=legacy-resolver
COPY . /myob_api
EXPOSE 3007
ENTRYPOINT ["python"]
CMD ["main.py"]