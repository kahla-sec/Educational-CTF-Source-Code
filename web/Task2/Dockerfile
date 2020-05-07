FROM ubuntu:19.10 
RUN apt-get upgrade
RUN apt-get update
RUN apt-get update && apt-get -y upgrade && DEBIAN_FRONTEND=noninteractive apt-get -y install \
    apache2 php7.3 libapache2-mod-php7.3

COPY index.php /var/www/html/
COPY flag.php /var/www/html/
RUN rm /var/www/html/index.html
RUN a2enmod php7.3
RUN a2enmod rewrite

ENV APACHE_RUN_USER www-data
ENV APACHE_RUN_GROUP www-data
ENV APACHE_LOG_DIR /var/log/apache2
ENV APACHE_LOCK_DIR /var/lock/apache2
ENV APACHE_PID_FILE /var/run/apache2.pid

EXPOSE 80
CMD /usr/sbin/apache2ctl -D FOREGROUND

