 #RUN docker image pull alpine

 FROM alpine:edge

 # Install python and pip
 RUN apk add --update py2-pip

 # install Python modules needed by the Python app
 COPY requirements.txt /usr/src/app/
 RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt

 # copy files required for the app to run
 COPY service.py /usr/src/app/
 COPY getTrends.py /usr/src/app/

 # tell the port number the container should expose
 EXPOSE 5000

 # run the application
 CMD ["python", "/usr/src/app/getTrends.py"]
 CMD ["python", "/usr/src/app/service.py"]
