#!/bin/bash
tagname=jgajardog/newfms-django_0.0.1
host=djangotest
#host=$tagname
#
sudo docker build -t ${tagname} .
sleep 2
sudo docker push ${tagname}
sleep 2
sudo docker pull ${tagname}
sleep 2
sudo docker stop $host
sleep 2
sudo docker rm $host
sleep 2
sudo docker run -h ${host} --name $host -p 8080:8080 -e J_SYSLOG_USE=False -e J_SYSLOG_IP=127.0.0.1 -e J_SYSLOG_PORT=514 -e J_ADMIN_USER=newfms -e J_ADMIN_PASS=sdGT34934  -e J_MYSQL_DB=DESA  -e J_MYSQL_USER=desa -e J_MYSQL_PASSWORD=desa -e J_MYSQL_IP=10.68.3.120 -e J_MYSQL_PORT=3306  -itd ${tagname}
sleep 2
sudo docker logs ${host}

date
