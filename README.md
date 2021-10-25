
 <h2>Requirements </h2>

Docker desktop Kubernetes (single node cluster)

Mongo server needed 5.0 

ingress nginx controller needed 

python req files are in /backend/*api/requirments.txt folder 

🔸 ingress controller uses test.com domian add it as a hostfile entry

 <h2>DB setup background </h2>

DB path = C:\Program Files\MongoDB\Server\5.0\data 
Mongodb persistant volume must be set up from windows first and data must be added before hand
after disable mongodb service (startup = manual ) from services.msc or mongo pod will crash

 <h2> Generate Docker Images using .bat </h2>

docker image files can (backend) can be generated using /backend/buildall.bat
push to DCR with /docker/push/bat

 <h2>Start app on kubernetes </h2>

✅ Can start  kubernets app from Setup.bat file in [Setupfile](/kubernetes/Setup.bat) 

🔴 Can Destroy kubernets app from Destroy.bat file in [Destroyfile](/kubernetes/Destroy.bat) 

