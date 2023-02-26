#!/bin/bash
docker rm  op-dns-web -f 
docker rm  op-mysql-5.7 -f 
rm -rf install_dir/docker-compose/mysql/datadir/
