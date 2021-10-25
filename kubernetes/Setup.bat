REM Kubernets application deployment.
REM Setup DB

REM setup persistent volume
kubectl apply -f %~dp0database\pv.yaml
REM setup pod
kubectl apply -f %~dp0database\mongo.yaml
REM setup claim
kubectl apply -f %~dp0database\pvc.yaml
REM setup db-service for internal connections with DG
kubectl apply -f %~dp0database\db_service.yaml
REM create DB access url (MONGODB_URI)
kubectl apply -f %~dp0database\login_secret.yaml

REM setup backend APIs

REM setup API-countrylist Development group(DG) and ClusterIP service
kubectl apply -f %~dp0DeploymentGroups\countrylist_DG.yaml
kubectl apply -f %~dp0Services\countrylist_service.yaml
REM setup API-srilankahistory Development group(DG) and ClusterIP service
kubectl apply -f %~dp0DeploymentGroups\srilankahistory_DG.yaml
kubectl apply -f %~dp0Services\srilankahistory_service.yaml
REM setup API-viewcountry Development group(DG) and ClusterIP service
kubectl apply -f %~dp0DeploymentGroups\viewcountry_DG.yaml
kubectl apply -f %~dp0Services\viewcountry_service.yaml
REM setup API-statscountry Development group(DG) and ClusterIP service
kubectl apply -f %~dp0DeploymentGroups\statscountry_DG.yaml
kubectl apply -f %~dp0Services\statscountry_service.yaml

REM setup frontend

kubectl apply -f %~dp0DeploymentGroups\frontend.yaml
kubectl apply -f %~dp0Services\frontend.yaml

REM setup nginx-ingress controller
kubectl apply -f %~dp0Ingress\ingress.yaml