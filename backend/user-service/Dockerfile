FROM python:3.8
# copy the req file to app directory in the docker image
COPY requirements.txt /user_service/requirements.txt
WORKDIR /user_service
RUN pip install -r requirements.txt --use-deprecated=legacy-resolver
RUN pip install requests
COPY . /user_service
EXPOSE 5001
ENTRYPOINT ["python"]
CMD ["user-service.py"]