# Hellow World 
This is a simple python app to run on Kubernetes

## Docker

### Build Docker Image
```
docker build . -t devops-helloworld:1.0.0
```

### Run Docker image
#### For the first run
```
docker run --name helloworld devops-helloworld:1.0.0
```
#### Re-run already container
```
docker start helloworld -a
```