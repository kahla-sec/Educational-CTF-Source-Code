FROM ubuntu:19.10
RUN apt-get upgrade
RUN apt-get update
RUN apt-get install -y sudo figlet
RUN useradd -d /home/user1/ -m -p Securinets1SalwaysHere -s /bin/bash user1
RUN echo "user1:Securinets1SalwaysHere" | chpasswd
RUN useradd -d /home/user-privileged/ -m -p Securinets1SalwaysHereAndW0ntLoose -s /bin/bash user-privileged
RUN echo "user-privileged:Securinets1SalwaysHereAndW0ntLoose" | chpasswd
RUN chown root:user1 /home/user1/
COPY flag.txt /home/user1/
WORKDIR /home/user1
COPY sweep.sh .
RUN chown root:user-privileged /home/user1/sweep.sh
RUN chmod 755 /home/user1/sweep.sh
RUN chmod 1775 /home/user1/
RUN chown root:user-privileged /home/user1/flag.txt
RUN chmod 740 /home/user1/flag.txt
RUN rm /etc/sudoers
COPY sudoers /etc/
USER user1
CMD /bin/bash
