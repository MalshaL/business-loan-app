FROM python:3.8
# copy the req file to app directory in the docker image
COPY requirements.txt /loan_service/requirements.txt
WORKDIR /loan_service
RUN pip install -r requirements.txt --use-deprecated=legacy-resolver
RUN pip install requests
COPY . /loan_service
EXPOSE 5002
ENTRYPOINT ["python"]
CMD ["loan-service.py", "--host=0.0.0.0"]