# Requirements

* To run a local docker and kubernetes all you need is to download (https://docs.docker.com/desktop/)
* or you can use AKS, GKE, EKS
  
# The APP

Python application using Flask framework. The application returns a JSON response when root "/" URL path is accessed:
```json
{
  "timestamp": "<current date and time>",
  "hostname": "<Name of the host (IP also accepted)>",
  "engine": "<Name and/or version of the engine running>",
  "visitor ip": "<the IP address of the visitor>"
}
```
# How to

Testing the application locally

we first build the image:

```bash
$ docker build -t bismarkcastilla/microservice .
```

After generating the image we can upload the image to docker hub

```bash
$ docker push bismarkcastilla/microservice
```

then we can use that image pulling it from docker hub (https://hub.docker.com/r/bismarkcastilla/microservice)

```bash
$ docker pull bismarkcastilla/microservice
```

*downloaded images*

```
$ docker images
REPOSITORY                     TAG         IMAGE ID       CREATED         SIZE
bismarkcastilla/microservice   latest      a4ae0d603b46   8 hours ago     122MB
```

## Run docker image

you can run the image inside a container using `docker run`:

```bash
$ docker run -d -p 5000:5000 bismarkcastilla/microservice
```

test the application using curl and in the browser(type localhost:5000):

```bash
$ curl localhost:5000
{"engine":"3.9.11 (main, Mar 17 2022, 06:08:17) \n[GCC 8.3.0]","hostname":"93b1816a882d","timestamp":"Wed, 23 Mar 2022 20:44:59 GMT","visitor ip":"172.17.0.1"}
```

# Kubernetes

You can run the microservice in your k8 cluster.

The recommended way is to create a new namespace to deploy the microservice using these commands:

```bash
$ kubectl create namespace microservice
$ kubectl apply -f k8-manifest/ -n microservice
```

we use the `kubectl port-forward` command to test the microservice:

```bash
$ kubectl port-forward pods/<podname> 3000:5000 -n microservice
```

You can verify if the service is running
```
$ kubectl get svc -n microservice
NAME           TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
microservice   ClusterIP   10.111.96.190   <none>        5000/TCP   2m44s
```

use curl to verify if microservice is running:

```
$ curl localhost:3000
{"engine":"3.9.11 (main, Mar 17 2022, 06:08:17) \n[GCC 8.3.0]","hostname":"microservice-84dcc479bc-bqbdq","timestamp":"Wed, 23 Mar 2022 20:59:01 GMT","visitor ip":"127.0.0.1"}
```

# Remove configurations

clean up k8 deployment:

```bash
kubectl delete -f k8-manifest/ -n microservice
```

clean up docker deployment:
```bash
$docker images
$docker rmi <imageid>

$ docker ps -a
$ docker stop <containerid>
$ docker rm <containerid>
```