REM Distory Kubernets application deployment.
REM Destory DB

REM Destory persistent volume
kubectl delete -f %~dp0database\pv.yaml
REM Destory persistent volume claim
kubectl delete -f %~dp0database\mongo.yaml
REM Destory DB pod
kubectl delete -f %~dp0database\pvc.yaml
REM Destory db-service for internal connections with DG
kubectl delete -f %~dp0database\db_service.yaml
REM create DB access url (MONGODB_URI)
kubectl delete -f %~dp0database\login_secret.yaml

REM Destory backend APIs

REM Destory API-countrylist Development group(DG) and ClusterIP service
kubectl delete -f %~dp0DeploymentGroups\countrylist_DG.yaml
kubectl delete -f %~dp0Services\countrylist_service.yaml
REM Destory API-srilankahistory Development group(DG) and ClusterIP service
kubectl delete -f %~dp0DeploymentGroups\srilankahistory_DG.yaml
kubectl delete -f %~dp0Services\srilankahistory_service.yaml
REM Destory API-viewcountry Development group(DG) and ClusterIP service
kubectl delete -f %~dp0DeploymentGroups\viewcountry_DG.yaml
kubectl delete -f %~dp0Services\viewcountry_service.yaml
REM Destory API-statscountry Development group(DG) and ClusterIP service
kubectl delete -f %~dp0DeploymentGroups\statscountry_DG.yaml
kubectl delete -f %~dp0Services\statscountry_service.yaml

REM Destory frontend

kubectl delete -f %~dp0DeploymentGroups\frontend.yaml
kubectl delete -f %~dp0Services\frontend.yaml

REM Destory nginx-ingress controller
kubectl delete -f %~dp0Ingress\ingress.yaml