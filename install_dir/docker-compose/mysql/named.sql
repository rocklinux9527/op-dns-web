
use `named`;

INSERT INTO `dns_records` VALUES (21,'test.info','w','CNAME','www',60,NULL,'any',255,28800,14400,86400,86400,2015050917,'ddns.net','ns.ddns.net.'),(18,'test.info','www','A','2.2.2.2',60,NULL,'any',255,28800,14400,86400,86400,2015050917,'ddns.net','ns.ddns.net.'),(22,'test.info','www','A','1.1.1.1',60,NULL,'any',255,28800,14400,86400,86400,2015050917,'ddns.net','ns.ddns.net.');
UNLOCK TABLES;


LOCK TABLES `user` WRITE;
INSERT INTO `user` VALUES (87,'laowang','老王','12fe31d801a521149d338101fe938649','13725578011','112@qq.com',0,0),(88,'eagle','老鹰','12fe31d801a521149d338101fe938649','13725571111','1112@qq.com',0,0);
UNLOCK TABLES;
