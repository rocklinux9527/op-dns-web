# op-dns-web
1.flask 开发dns web管理平台

***1.容器化快速部署***

```
1.自行部署Docker环境 (参考:https://docs.docker.com/get-docker/)
2.部署docker-compose （参考:https://docs.docker.com/compose/install/）
3.执行部署dns-web 服务
 bash install_shell.sh 输入任意参数
 部署DNS web服务参数如下
 deploy_env_clear  部署前环境清理
 deploy_check  服务部署基础环境检查
 deploy_flask_dns_web  dns-web 环境部署
 部署过程如下:
   $ bash install_shell.sh   deploy_env_clear
    开始清理部署环境
    op-dns-web
    op-mysql-5.7
    环境清理完毕
   $ bash install_shell.sh deploy_flask_dns_web
  开始清理部署环境
   Error: No such container: op-dns-web
   Error: No such container: op-mysql-5.7
   环境清理完毕
  Creating op-mysql-5.7 ... done
  Creating op-dns-web   ... done
  mysql: [Warning] Using a password on the command line interface can be insecure.
  mysql: [Warning] Using a password on the command line interface can be insecure.
```
***2.传统虚拟机部署方式***
```
  1.部署mysql数据库服务;
  2.安装python 3.7 （参考:https://www.python.org/downloads/） 下载并安装
  3.执行pip -r install requirements.txt 
  4.启动服务:
  $ python3.7 boot.py
 * Serving Flask app '__init__'
 * Debug mode: on
  WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on all addresses (0.0.0.0)
 * Running on http://127.0.0.1:5000
 * Running on http://192.168.1.5:5000
  Press CTRL+C to quit
   * Restarting with stat
   * Debugger is active!
   * Debugger PIN: 195-544-672
```
