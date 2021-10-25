kubectl apply -f  %~dp0pv.yaml
kubectl apply -f  %~dp0pvc.yaml
kubectl apply -f  %~dp0mongo.yaml
kubectl apply -f  %~dp0db_service.yaml

