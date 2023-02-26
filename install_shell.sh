#!/bin/bash
#set -e
function cleanDeploy(){
echo -e "\e[32m 开始清理部署环境\e[0m"
/bin/sh deploy_env_clear.sh
echo -e "\e[32m 环境清理完毕\e[0m"
}

function checkDockerCompose(){
echo -e "\e[32m 开始检查Docker-compose环境\e[0m"
checkDockerCompose=$(docker-compose -v |wc -l)
if [ $checkDockerCompose -eq 1 ]
then
   cd ./install_dir/docker-compose/
   echo -e "\e[32m 开始容器化DNS WEB服务部署\e[0m"
   docker-compose up -d
   reultDeploy=$(docker-compose ps |grep -E "op-dns-web|op-mysql-5.7" |grep "Up" |wc -l)
   if [ $reultDeploy -eq 2 ] 
   then
      echo -e "\e[32m 等待25秒,Mysql 服务初始化\e[0m"
      sleep 25
      checkMysql=$(docker exec -i op-mysql-5.7  mysql -uroot -p123456 -e "select version();" |wc -l)
      if [  $checkMysql  -ne 0 ]
      then
          docker exec -i  op-dns-web python command.py
          docker exec -i op-mysql-5.7  mysql -uroot -p123456 -e "use named; source /opt/named.sql;"
          echo 0 
      else
          echo -e "\e[31m Mysql 程序sql导入失败\e[0m"
      fi
      docker restart op-dns-web
      sleep 3 
    else
       echo -e "\e[31m 容器化DNS WEB服务部署失败啦!\e[0m"
       echo 1  
   fi 

   echo -e "\e[32m DNS web 部署完毕,访问机器http://localhost:80  Success\e[0m"
else
    echo -e "\e[31m docker-compose环境没有安装自行,https://docs.docker.com/compose/install/ 获取并安装\e[0m"  
    echo 1
fi
}

 
function main(){
url="http://127.0.0.1/login/"
code=`curl -I -m 30 -o /dev/null -s -w %{http_code}"/n" $url |awk -F '/' '{print $1}'`
if [ $code -eq 200 ]
then
   echo -e "\e[31m 应用已经存在或者端口被占用程序终止,请手动停止服务在执行脚本\e[0m"
else
   count=0
   while [ $count -le 3 ]
   do
    cleanDeploy
    reult=`checkDockerCompose`
    code=`curl -I -m 30 -o /dev/null -s -w %{http_code}"/n" $url|awk -F '/' '{print $1}'` 
    if [ $code -eq  200 ]
    then
       break
    fi
    count=$((count+1)) 
    done 
fi
}

function checkDocker(){
chcek=$(ps -ef |grep docker |wc -l)
if [ $chcek -ne 0 ];then echo -e "\e[32m Dokcer服务存在具备部署服务条件,下一步可选择执行deploy_flask_dns_web\e[0m";else  echo -e "\e[31m docker不存在请检查并自行安装docker\e[0m";fi
}



case $1 in
    "all")
        main 
        ;;
    "deploy_env_clear")
        cleanDeploy 
        ;;
    "deploy_flask_dns_web")
        main 
        ;;
    "deploy_check")
        checkDocker
     ;;
    *)
        echo -e "\033[32m 部署DNS web服务参数如下 \033[0m"
        echo -e "\033[32m deploy_env_clear \033[0m 部署前环境清理"
        echo -e "\033[32m deploy_check \033[0m 服务部署基础环境检查"
        echo -e "\033[32m deploy_flask_dns_web \033[0m dns-web 环境部署"
        ;;
esac







