SET FOREIGN_KEY_CHECKS=0;
DELETE FROM `user` WHERE id = 2;
DELETE FROM `eqLogic`;
DELETE FROM `cmd`;
DELETE FROM `object`;
INSERT INTO `user` VALUES (2,'simple','user','a72ed62e8bc9e7bbf0cbc71312bff824e91411d047bf29fd6abf31c3f4b6e8e3ee2883eec141d0fd9130fe1683f3f8a2c0f3909580c50bcf9016e3cf6249c1b8','{\"localOnly\":\"0\",\"lastConnection\":\"\"}','VVZtg2HUxbE4XWStXTVWc2ONs0b0fXtt','[]',1);
INSERT INTO `object` VALUES (1,'My Room',NULL,1,NULL,'{\"parentNumber\":0,\"tagColor\":\"#000000\",\"tagTextColor\":\"#FFFFFF\",\"desktop::summaryTextColor\":\"\",\"mobile::summaryTextColor\":\"\"}','[]','[]');
INSERT INTO `object` VALUES (2,'Second Room',NULL,1,NULL,'{\"parentNumber\":0,\"tagColor\":\"#000000\",\"tagTextColor\":\"#FFFFFF\",\"desktop::summaryTextColor\":\"\",\"mobile::summaryTextColor\":\"\",\"hideOnDashboard\":\"0\",\"summary::global::security\":\"0\",\"summary::global::motion\":\"0\",\"summary::global::door\":\"0\",\"summary::global::windows\":\"0\",\"summary::global::shutter\":\"0\",\"summary::global::light\":\"0\",\"summary::global::outlet\":\"0\",\"summary::global::temperature\":\"0\",\"summary::global::humidity\":\"0\",\"summary::global::luminosity\":\"0\",\"summary::global::power\":\"0\",\"summary::hide::desktop::security\":\"0\",\"summary::hide::desktop::motion\":\"0\",\"summary::hide::desktop::door\":\"0\",\"summary::hide::desktop::windows\":\"0\",\"summary::hide::desktop::shutter\":\"0\",\"summary::hide::desktop::light\":\"0\",\"summary::hide::desktop::outlet\":\"0\",\"summary::hide::desktop::temperature\":\"0\",\"summary::hide::desktop::humidity\":\"0\",\"summary::hide::desktop::luminosity\":\"0\",\"summary::hide::desktop::power\":\"0\",\"summary::hide::mobile::security\":\"0\",\"summary::hide::mobile::motion\":\"0\",\"summary::hide::mobile::door\":\"0\",\"summary::hide::mobile::windows\":\"0\",\"summary::hide::mobile::shutter\":\"0\",\"summary::hide::mobile::light\":\"0\",\"summary::hide::mobile::outlet\":\"0\",\"summary::hide::mobile::temperature\":\"0\",\"summary::hide::mobile::humidity\":\"0\",\"summary::hide::mobile::luminosity\":\"0\",\"summary::hide::mobile::power\":\"0\",\"summary\":{\"security\":[],\"motion\":[],\"door\":[],\"windows\":[],\"shutter\":[],\"light\":[],\"outlet\":[],\"temperature\":[],\"humidity\":[],\"luminosity\":[],\"power\":[]}}','{\"tagColor\":\"#33b8cc\",\"tagTextColor\":\"#ffffff\",\"desktop::summaryTextColor\":\"#ffffff\",\"dashboard::size\":\"\",\"icon\":\"\"}','[]');
INSERT INTO `object` VALUES (3,'Bathroom',2,0,NULL,'{\"parentNumber\":1,\"tagColor\":\"#000000\",\"tagTextColor\":\"#FFFFFF\",\"desktop::summaryTextColor\":\"\",\"mobile::summaryTextColor\":\"\",\"hideOnDashboard\":\"0\",\"summary::global::security\":\"0\",\"summary::global::motion\":\"0\",\"summary::global::door\":\"0\",\"summary::global::windows\":\"0\",\"summary::global::shutter\":\"0\",\"summary::global::light\":\"0\",\"summary::global::outlet\":\"0\",\"summary::global::temperature\":\"0\",\"summary::global::humidity\":\"0\",\"summary::global::luminosity\":\"0\",\"summary::global::power\":\"0\",\"summary::hide::desktop::security\":\"0\",\"summary::hide::desktop::motion\":\"0\",\"summary::hide::desktop::door\":\"0\",\"summary::hide::desktop::windows\":\"0\",\"summary::hide::desktop::shutter\":\"0\",\"summary::hide::desktop::light\":\"0\",\"summary::hide::desktop::outlet\":\"0\",\"summary::hide::desktop::temperature\":\"0\",\"summary::hide::desktop::humidity\":\"0\",\"summary::hide::desktop::luminosity\":\"0\",\"summary::hide::desktop::power\":\"0\",\"summary::hide::mobile::security\":\"0\",\"summary::hide::mobile::motion\":\"0\",\"summary::hide::mobile::door\":\"0\",\"summary::hide::mobile::windows\":\"0\",\"summary::hide::mobile::shutter\":\"0\",\"summary::hide::mobile::light\":\"0\",\"summary::hide::mobile::outlet\":\"0\",\"summary::hide::mobile::temperature\":\"0\",\"summary::hide::mobile::humidity\":\"0\",\"summary::hide::mobile::luminosity\":\"0\",\"summary::hide::mobile::power\":\"0\",\"summary\":{\"security\":[],\"motion\":[],\"door\":[],\"windows\":[],\"shutter\":[],\"light\":[],\"outlet\":[],\"temperature\":[],\"humidity\":[],\"luminosity\":[],\"power\":[]}}','{\"tagColor\":\"#33b8cc\",\"tagTextColor\":\"#ffffff\",\"desktop::summaryTextColor\":\"#ffffff\",\"dashboard::size\":\"\",\"icon\":\"\"}','[]');
INSERT INTO `eqLogic` VALUES (1,'Test eqLogic',NULL,NULL,1,'plugin4tests','{\"createtime\":\"2019-02-10 22:10:30\",\"updatetime\":\"2019-02-01 20:21:16\"}',1,NULL,1,NULL,NULL,'[]','{\"showObjectNameOnview\":1,\"showObjectNameOndview\":1,\"showObjectNameOnmview\":1,\"height\":\"auto\",\"width\":\"auto\",\"layout::dashboard::table::parameters\":{\"center\":1,\"styletd\":\"padding:3px;\"},\"layout::mobile::table::parameters\":{\"center\":1,\"styletd\":\"padding:3px;\"}}',9999,NULL,NULL);
INSERT INTO `eqLogic` VALUES (2,'Second eqLogic',NULL,NULL,1,'plugin4tests','{\"createtime\":\"2019-03-10 22:10:30\",\"updatetime\":\"2019-03-01 20:21:16\"}',0,NULL,0,NULL,NULL,'[]','{\"showObjectNameOnview\":1,\"showObjectNameOndview\":1,\"showObjectNameOnmview\":1,\"height\":\"auto\",\"width\":\"auto\",\"layout::dashboard::table::parameters\":{\"center\":1,\"styletd\":\"padding:3px;\"},\"layout::mobile::table::parameters\":{\"center\":1,\"styletd\":\"padding:3px;\"}}',9999,NULL,NULL);
INSERT INTO `config` VALUES ('plugin4tests','active','1'),('plugin4tests','deamonAutoMode','1'),('core','log::level::plugin4tests','{\"100\":\"1\",\"200\":\"0\",\"300\":\"0\",\"400\":\"0\",\"1000\":\"0\",\"default\":\"0\"}');
INSERT INTO `cmd` VALUES (1,1,'plugin4tests',NULL,NULL,0,'Cmd 1','[]','[]','0','info','binary',NULL,'[]',1,NULL,'[]','[]');
INSERT INTO `cmd` VALUES (2,1,'plugin4tests',NULL,NULL,0,'Cmd 2','[]','[]','0','action','other',NULL,'[]',0,NULL,'[]','[]');
INSERT INTO `cmd` VALUES (3,2,'plugin4tests',NULL,NULL,0,'Cmd 3','[]','[]','0','info','binary',NULL,'[]',1,NULL,'[]','[]');
INSERT INTO `note` VALUES (1,'Note de test','Un peu de contenu');
INSERT INTO `note` VALUES (2,'Une autre note','Peu d\'idée');
INSERT INTO `scenario` VALUES (1,'Test scenario','',1,'schedule','* * * * *','[\"1\"]','[\"\"]',NULL,1,NULL,'{\"name\":\"\"}','','{\"timeDependency\":0,\"has_return\":0,\"logmode\":\"default\",\"allowMultiInstance\":\"0\",\"syncmode\":\"0\",\"timeline::enable\":\"0\"}','expert',99);
INSERT INTO `scenarioElement` VALUES (1,0,'action',NULL,NULL,NULL);
INSERT INTO `scenarioExpression` VALUES (1,0,1,'action',NULL,'log','{\"enable\":\"1\",\"background\":\"0\",\"message\":\"LAUNCHED\"}',NULL);
SET FOREIGN_KEY_CHECKS=1;