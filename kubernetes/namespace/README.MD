# Namespace Management
## To create a namespace, use the following command according to your namespace file
```
kubectl create -f .\kubernetes\namespace\namespace-devops.yaml
```

## To create a Context for a namespace and switch to it:
```
kubectl config set-context devops --namespace=devops
```
```
kubectl config use-context devops
```