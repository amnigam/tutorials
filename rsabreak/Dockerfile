FROM ubuntu:jammy

ENV DEBIAN_FRONTEND=noninteractive 

# Get all the packages onto our image. 
RUN apt-get update && apt install -y nginx &&\
    apt install -y python3 &&\ 
    apt install -y python3-pip &&\
    apt install -y curl &&\
    apt install -y openssh-server &&\
    mv /etc/ssh/sshd_config /etc/ssh/sshd_config.ORIG &&\
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY requirements.txt ./    
# Conf file for NGINX 
COPY app.conf ./ 
# Startup script to setup the services. 
COPY startup.sh ./
# Certificate for web app. 
COPY CERT.pem ./ 
# Private Key 
COPY id_rsa ./            
# Public Key 
COPY key.pem ./
COPY templates/ ./templates/
# SSHD_CONFIG file for our SSH server
COPY aws-ssh_config /etc/ssh/sshd_config    
# Create the .SSH folder for ROOT and Authorized Keys folder 
RUN mkdir /root/.ssh/ &&\
    touch /root/.ssh/authorized_keys

# Set the necessary permissions for SSH & Startup script. 
RUN chmod +x startup.sh
RUN chmod 700 /root/.ssh/
RUN chmod 600 /root/.ssh/authorized_keys 

# Setup the NGINX server configuration file
RUN touch /etc/nginx/conf.d/app.conf &&\
 cat app.conf > /etc/nginx/conf.d/app.conf 

RUN pip install -r requirements.txt 

COPY app.py ./

CMD ["/bin/bash", "startup.sh"]