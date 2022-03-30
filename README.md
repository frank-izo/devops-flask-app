### Tools to create the python-flaskapp



# install python3

# install virtualenv and activate. You can use the link below 
# https://tech.serhatteker.com/post/2018-12/virtualenv/

# install flask by using pip. Make sure pip is installed before
pip install Flask 



### Install Docker depends on the platform
# https://docs.docker.com/engine/install/



### Get the Dockerfile ready
```
# use the python:alpine base image
FROM python:3.8.3-alpine

# set the working directory to /go/src/app
WORKDIR /app

# copy all the files from the current directory to the container working directory
COPY . /app

# import dependencies using pip command
RUN pip install --upgrade pip
RUN pip install --user -r requirements.txt

# expose the port 5000
EXPOSE 5000

# start the container
CMD ["python", "app.py""]
```

### Package the application
Steps to package the application using Docker commands:

``` 
# build the image
docker build -t devops-app1 .

# run the image
docker run -d -p 5000:5000 --name devops-app devops:v1.0

# tag the image
# change the Dockerhub username, as applicable to you, for e.g., fizzo/devops-app1:v1.0
docker tag devops-app1 pixelpotato/devops-app1:v1.0

# login into DockerHub
docker login

# push the image
docker push fizzo/devops-app1:v1.0
```


### Step 3. Deploy to Kubernetes 
 Deploy Kubernetes Cluster". The commands below are supposed to be run *only* after you have run the commands above. 
```
# Shortcut method to run the application with headless pods
kubectl run test --image fizzo/devops-app1:v1.0
# Deploy the kubernetes cluster manifest whch comprises of a deployment, service and a traefik-Ingress-Controller 
# that can be used to manage the incoming external requests by using a loadbalancer service
kubectl create -f manifests
# Open node ports 30,000 to 32,767 
# Display the pod name
kubectl get pods
# Display the service
kubectl get svc
# Display the deployment
kubectl get deployment
# Access the application on the local host
python app.py
#127.0.0.0:5000
```
Access the application in the local machine on  http://127.0.0.1:5000










