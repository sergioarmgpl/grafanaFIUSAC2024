# grafanaFIUSAC2024
To use this repo run the following steps:
1. Create the namespace and apply the YAML files into a Kubernetes Cluster
```
kubectl apply -f namespace.yaml
kubectl apply -f .
```
2. Check the client service
```
kubectl logs deploy/client -n monitoring -f
```
3. Access the dashboard in http://127.0.0.1:3000
```
kubectl port-forward -n monitoring --address 0.0.0.0 svc/grafana 3000:3000
```
4. Set the Redis datasource as 
```
redis://redis.monitoring.svc:6379
```
5. Then create your dashboard