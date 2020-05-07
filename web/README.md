# Web Category #

![IMG](https://imgur.com/sNOaHtc.png)

## Deployment ##

For the deployment you have to first build the docker image :
 ```
 sudo docker build . -t task1
 ```
 
 And then run a detached container:
 
 ```
 sudo docker run -it -d -p 8080:PORT task1
 ```
 
 For the PORT it's the following for each task:
 
 1) Task1: 80
 
 2) Task2: 80
 
 3) Task3: 8020
 
 4) Task4: 1234
 
 5) Task5: 5555
 
 **Note:** For the fifth task you have to login to the container and launch mysql service , i were a little bit lazy to automate this :( :
 
 * Login to the container:
 
 ```
 sudo docker exec -it container_id /bin/bash
 ```
 
 * Run the following command:
 
 ```
 service mysql start
 ```
 
 and finally launch mysql by just typing mysql and execute the queries found in **sqlcommand** file found in Task5 
 
