#!/usr/bin/bash

service nginx start 
# Convert public RSA key into SSH format.
ssh-keygen -i -m PKCS8 -f key.pem > key.ssh
cp key.ssh  /root/.ssh/authorized_keys 
service ssh start
/bin/bash