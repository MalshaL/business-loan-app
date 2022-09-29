FROM python:3.8
# copy the req file to app directory in the docker image
COPY requirements.txt /dec_engine/requirements.txt
WORKDIR /dec_engine
RUN pip install -r requirements.txt --use-deprecated=legacy-resolver
COPY . /dec_engine
EXPOSE 3005
ENTRYPOINT ["python"]
CMD ["main.py", "--host=0.0.0.0"]