# Bash Category #

![IMG](https://imgur.com/26mU44D.png)

## Jail Bash tasks: ##

> Taskbash1 -> Taskbash5

**Notice:** If you want to try the tasks just run jail.sh file for each task

### Production Server Configuration ###

The commands are the same for each bash jail task:

**Build the docker image**

```
sudo docker build . -t task1
```

**Instantiate a container**

```
sudo docker run -it -d -p 10000:1234 task1
```

**Run SSH Service**

1- Login to container

```
sudo docker exec -t container_id /bin/bash
```

2- Launch SSH service:

```
service ssh start
```

You will have an ssh service listening on port 10000 with the user "ctf" and password "Securinetsxkahla"

## Privesc tasks: ##

> Taskbash6 -> Taskbash7

### **Configuration** ###

You will have to firstly build the task image and then for the production server you have to navigate to SSH_Container and build an image of the container that will listen for ssh connexions and manage each connexion by connecting it to a separate container

### 1st Image ###

**1-Build the docker image**

```
sudo docker build . -t priv
```
**Notice:** If you want to test the task locally just login to the container:

**Instantiate a container**

```
sudo docker run -it priv /bin/bash
```

### 2nd Image ###

In the production server we will build the image of the container that will manage ssh connexions for us , navigate to SSH_Container and:

**1-Build the docker image**

```
sudo docker build . -t taskpriv
```

**2-Instanciate a container**

```
sudo docker run -it -v /var/run/docker.sock:/var/run/docker.sock -d -p 10000:1234 taskpriv
```
 The **-v /var/run/docker.sock:/var/run/docker.sock** option for binding docker sockets of the host machine and the container and as a result the container can access the images of the host machine and see its running cotainers and vice versa

You will have an ssh service listening on port 10000 with the user "ctf" and password "Securinetsxkahla" and each session is separated in a unique container (notice that if the session is closed the created container will be removed => more free ressources \o/)
