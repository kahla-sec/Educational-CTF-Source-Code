# Misc Category #

1) Build the docker image:

```
sudo docker build . -t task1
```

2) Instanciate a container:

```
sudo docker run -it -d -p 8080:1234 task1
```

Now you can use the port 8080 to connect 
