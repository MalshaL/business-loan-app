FROM python:3.8
# copy the req file to app directory in the docker image
COPY requirements.txt /acc_service/requirements.txt
WORKDIR /acc_service
RUN pip install -r requirements.txt --use-deprecated=legacy-resolver
RUN pip install requests
COPY . /acc_service
EXPOSE 5003
ENTRYPOINT ["python"]
CMD ["accounting-service.py"]