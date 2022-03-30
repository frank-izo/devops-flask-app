A simple python flaskapp that returns a json response

Build:

docker build -t devops-app1:v1.0 .
Run:

docker run -d -p 5000:5000 --name devops-app devops:v1.0

Test:

curl http://0.0.0.0:5000/
