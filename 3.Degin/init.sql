CREATE TABLE hs_org_basetable (
  Id int(11) NOT NULL AUTO_INCREMENT,
  Code varchar(32) DEFAULT NULL,
  Name varchar(64) DEFAULT NULL,
  Address varchar(128) DEFAULT NULL,
  Longitude float DEFAULT NULL,
  Langitude float DEFAULT NULL,
  BusinessContact varchar(64) DEFAULT NULL,
  BusinessPhone varchar(20) DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);

CREATE TABLE hs_org_wxconfig (
  Id								int(11) NOT NULL AUTO_INCREMENT,
  Code							varchar(32) DEFAULT NULL,
  OrgCode						varchar(32) DEFAULT NULL,
  WXAppid						varchar(16) DEFAULT NULL,
  WXSecret					varchar(32) DEFAULT NULL,
  WxOrigId					varchar(20) DEFAULT NULL,
  WxToken						varchar(32) DEFAULT NULL,
  EncodingAESKey		varchar(64) DEFAULT NULL,
  CallbackAddress 		varchar(128) DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);


CREATE TABLE hs_org_config (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code        		varchar(32) 			DEFAULT NULL,
  IDCardImage1		varchar(40) 			DEFAULT NULL,
  IDCardImage2		varchar(40) 			DEFAULT NULL,
  IDCardNo    		varchar(20) 			DEFAULT NULL,
  OrgImage    		varchar(40) 			DEFAULT NULL,
  OrgID       		varchar(32) 			DEFAULT NULL,
  BankAccount 		varchar(20) 			DEFAULT NULL,
  BankBranch  		varchar(64) 			DEFAULT NULL,
  ExternData1 		varchar(64) 			DEFAULT NULL,
  ExternData2 		varchar(64) 			DEFAULT NULL,
  ExternData3 		varchar(64) 			DEFAULT NULL,
  ProtCode    		varchar(32) 			DEFAULT NULL,
  OrgKey      		varchar(10) 			DEFAULT NULL,  
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);


CREATE TABLE hs_org_protocol (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code     		Varchar(32) 			DEFAULT NULL,
  OrgCode  		Varchar(32) 			DEFAULT NULL,
  ProCode  		Varchar(32) 			DEFAULT NULL,
  StartDate		date         			,
  StopDate 		date         			,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);

CREATE TABLE hs_protocols (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code		Varchar(32) 			DEFAULT NULL,
  Name		Varchar(64) 			DEFAULT NULL,
  Type		int         			DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);

CREATE TABLE hs_protocol_detail (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  ProCode		Varchar(32) 			DEFAULT NULL,
  Pndex  		int         			DEFAULT NULL,
  Content		text        			DEFAULT NULL,
  PRIMARY KEY (Id)
  );
  
CREATE TABLE hs_teacher (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code     		Varchar(32) 			DEFAULT NULL,
  WxAccount		Varchar(64)  			DEFAULT NULL,
  Name     		Varchar(64) 			DEFAULT NULL,
  Phone    		Varchar(20)  			DEFAULT NULL,
  Passwd 		Varchar(32)   			DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);

CREATE TABLE hs_org_teachers (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code      		Varchar(32) 			DEFAULT NULL,
  TeachPhone		Varchar(20)  			DEFAULT NULL,
  JoinDate  		date        			DEFAULT NULL,
  OrgCode   		Varchar(32)  			DEFAULT NULL,
  SubCode1  		Varchar(32)  			DEFAULT NULL,
  SubCode2  		Varchar(32)  			DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);

CREATE TABLE hs_org_subjects (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code   		Varchar(32)			DEFAULT NULL,
  SysCode		Varchar(32) 			DEFAULT NULL,
  Name   		Varchar(64)			DEFAULT NULL,
  Type   		int         			DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);

CREATE TABLE hs_org_parents (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code      		Varchar(32)			DEFAULT NULL,
  ParentCode		Varchar(32) 			DEFAULT NULL,
  OrgCode   		Varchar(32)			DEFAULT NULL,
  JoinDate  		date       			DEFAULT NULL,
  StopDate  		date        			DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);

CREATE TABLE hs_org_students (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code   		Varchar(32)			DEFAULT NULL,
  StuCode		Varchar(32) 			DEFAULT NULL,
  OrgCode		Varchar(32)			DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);

CREATE TABLE hs_parent_Student (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code      		Varchar(32)			DEFAULT NULL,
  ParentCode		Varchar(32) 			DEFAULT NULL,
  StuCode   		Varchar(32)			DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);

CREATE TABLE hs_students (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Account    		Varchar(20)			DEFAULT NULL,
  Passwd   		  Varchar(32) 			DEFAULT NULL,
  Name       		Varchar(64)			DEFAULT NULL,
  WxAccount  		Varchar(64)			DEFAULT NULL,
  WxHeadImage		Varchar(40)			DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Account (Account)
);

CREATE TABLE hs_parents (
  Id          	int(11) 					NOT NULL AUTO_INCREMENT,
  Code          Varchar(32) 			DEFAULT NULL,
  Name       		Varchar(64)			DEFAULT NULL,
  WxAccount  		Varchar(64)			DEFAULT NULL,
  WxHeadImage		Varchar(40)			DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY WxAccount (WxAccount)
);

CREATE TABLE hs_sys_subujects (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Account  		Varchar(32) 			DEFAULT NULL,
  Password    Varchar(64) 			DEFAULT NULL,
  EMail    	  Varchar(64) 			DEFAULT NULL,
  Alias    		Varchar(64) 			DEFAULT NULL,
  Address  		Varchar(128)			DEFAULT NULL,
  OrgName  		Varchar(128)			DEFAULT NULL,
  Lantudite		Float       			DEFAULT NULL,
  Longdite 		Float       			DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Account (Account)
);
CREATE TABLE hs_class (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code     		Varchar(32)		DEFAULT NULL,
  OrgCode     Varchar(32)		DEFAULT NULL,
  Name     	  Varchar(64)		DEFAULT NULL,
  TeachCode		Varchar(32)		DEFAULT NULL,
  StartDate		date       		DEFAULT NULL,
  StopDate 		date       		DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);

CREATE TABLE hs_class_students (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code     		Varchar(32)		DEFAULT NULL,
  ClassCode   Varchar(32)		DEFAULT NULL,
  StuCode  	  Varchar(32)		DEFAULT NULL,
  InnerCode		Varchar(32)		DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);

CREATE TABLE hs_class_subjects (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code      		Varchar(32)		DEFAULT NULL,
  OrgCode       Varchar(32)		DEFAULT NULL,
  SubCode   	  Varchar(32)		DEFAULT NULL,
  Name      		Varchar(64)		DEFAULT NULL,
  TeachCode     Varchar(32)		DEFAULT NULL,
  IntroImage    Varchar(40)		DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);

CREATE TABLE hs_resource_type (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code   		Varchar(32)		DEFAULT NULL,
  Name      Varchar(64)		DEFAULT NULL,
  State  	  int        		DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);
CREATE TABLE hs_set_resources (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code        		Varchar(32)		DEFAULT NULL,
  OrgCode         Varchar(32)		DEFAULT NULL,
  AccessCount 	  int        		DEFAULT NULL,
  Price       	  Float      		DEFAULT NULL,
  Type        	  int        		DEFAULT NULL,
  SaleCount   	  int        		DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);
CREATE TABLE hs_person_set_resources (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code        		Varchar(32)		DEFAULT NULL,
  PersonCode      Varchar(32)		DEFAULT NULL,
  AccessCount 	  int        		DEFAULT NULL,
  Price       	  Float      		DEFAULT NULL,
  Type        	  int        		DEFAULT NULL,
  SaleCount   	  int        		DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);

CREATE TABLE hs_class_resources (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code      		Varchar(32)		DEFAULT NULL,
  ResCode       Varchar(32)		DEFAULT NULL,
  ClassCode 	  Varchar(32)		DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);

CREATE TABLE hs_person_resource (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code     		Varchar(32)	DEFAULT NULL,
  ResCode     Varchar(32)		DEFAULT NULL,
  FileName    Varchar(64)		DEFAULT NULL,
  RIndex       int        		DEFAULT NULL,
  Name        Varchar(64)		DEFAULT NULL,
  Info     	  text       	DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);

CREATE TABLE hs_sys_config (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code     		Varchar(32)	DEFAULT NULL,
  OrgCode  		Varchar(32)  	DEFAULT NULL,
  CKey        Varchar(32)  		DEFAULT NULL,
  CValue      Varchar(128) 		DEFAULT NULL,
  Unit        Varchar(4)    		DEFAULT NULL,
  CType       int          		DEFAULT NULL,
  CExpress 	  Varchar(1024)	DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);

CREATE TABLE hs_stu_checkin (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code      	 Varchar(32)		DEFAULT NULL,
  StuCode   	 Varchar(32) 		DEFAULT NULL,
  CheckTime    datetime    		DEFAULT NULL,
  Longutide    Float       		DEFAULT NULL,
  Langutide    Float        	DEFAULT NULL,
  OrgCode      Varchar(32) 		DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);
CREATE TABLE hs_teach_checkin (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code      	 Varchar(32)		DEFAULT NULL,
  StuCode   	 Varchar(32) 		DEFAULT NULL,
  CheckTime    datetime    		DEFAULT NULL,
  Longutide    Float       		DEFAULT NULL,
  Langutide    Float        	DEFAULT NULL,
  OrgCode      Varchar(32) 		DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);

CREATE TABLE hs_task_type (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code 	 			Varchar(32)		DEFAULT NULL,
  Name 	 			Varchar(64) 		DEFAULT NULL,
  Type   			int          		DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);


CREATE TABLE hs_tasks (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code       	 Varchar(32) 		DEFAULT NULL,
  TaskType   	 Int          		DEFAULT NULL,
  Name         Varchar(64)   		DEFAULT NULL,
  SimpleInfo   Varchar(128)  		DEFAULT NULL,
  DetaiInfo    Text           	DEFAULT NULL,
  StartTime    datetime       	DEFAULT NULL,
  StopTime     datetime       	DEFAULT NULL,
  AuthorCode   Varchar(32)    	DEFAULT NULL,
  MainCode     Varchar(32)    	DEFAULT NULL,
  State        int            	DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);

CREATE TABLE hs_orders (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code         	 Varchar(32)  		DEFAULT NULL,
  UserCode     	 Varchar(32)   		DEFAULT NULL,
  OrderTime      Datetime       		DEFAULT NULL,
  GoodsCode      Varchar(32)    		DEFAULT NULL,
  Price          Float           	DEFAULT NULL,
  State          int             	DEFAULT NULL,
  Count          int             	DEFAULT NULL,
  DownLoadInfo   Varchar(1024)   	DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);

CREATE TABLE hs_notices (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code        	Varchar(32)  		DEFAULT NULL,
  Title       	Varchar(64)   		DEFAULT NULL,
  SimpleInfo    Varchar(128)  		DEFAULT NULL,
  Info          Text          		DEFAULT NULL,
  ReleaseTime   datetime       	DEFAULT NULL,
  Attach1       Varchar(40)    	DEFAULT NULL,
  Attach2       Varchar(40)    	DEFAULT NULL,
  Attach3       Varchar(40)    	DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);
CREATE TABLE hs_msg (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code        	Varchar(32) 		DEFAULT NULL,
  SendCode    	Varchar(32)  		DEFAULT NULL,
  ReceiveCode   Varchar(32)  		DEFAULT NULL,
  Title         Varchar(64)  		DEFAULT NULL,
  Info          Text          	DEFAULT NULL,
  MsgTime       datetime      	DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);

CREATE TABLE hs_relax_msg (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code        	Varchar(32) 		DEFAULT NULL,
  SendCode    	Varchar(32)  		DEFAULT NULL,
  Info          Text         		DEFAULT NULL,
  ReleaseTime   datetime     		DEFAULT NULL,
  Type          int           	DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);

CREATE TABLE hs_relax_reply (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code        Varchar(32) 		DEFAULT NULL,
  RelaxCode 	Varchar(32) 		DEFAULT NULL,
  SendCode  	Varchar(32)  		DEFAULT NULL,
  Info        Text         		DEFAULT NULL,
  ReplyTime   datetime     		DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);

CREATE TABLE hs_msg_template (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code            Varchar(32) 		DEFAULT NULL,
  OrgCode            Varchar(32) 		DEFAULT NULL,
  TmpContent     	Text       		DEFAULT NULL,
  LastModifyTime  datetime     		DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);
CREATE TABLE hs_suggests (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code      Varchar(32) 		DEFAULT NULL,
  Title    	Varchar(64)		DEFAULT NULL,
  Content  	Text       		DEFAULT NULL,
  UserCode 	Varchar(32)		DEFAULT NULL,
  RelTime  	datetime   		DEFAULT NULL,
  Phone    	Varchar(20)		DEFAULT NULL,
  QQCode   	Varchar(32) 		DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);

CREATE TABLE hs_actives (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code        Varchar(32)		DEFAULT NULL,
  Account   	Varchar(20)	DEFAULT NULL,
  Title     	Varchar(64)	DEFAULT NULL,
  Content   	Text       	DEFAULT NULL,
  StartTime 	datetime   	DEFAULT NULL,
  StopTime  	datetime   	DEFAULT NULL,
  TmpCode   	Varchar(32)	DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);
CREATE TABLE hs_active_media (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code        Varchar(32)		DEFAULT NULL,
  ActCode   	Varchar(32)	DEFAULT NULL,
  MediaFile 	Varchar(40)	DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);
CREATE TABLE hs_bank_account (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code        Varchar(32)		DEFAULT NULL,
  UserCode      Varchar(32)		DEFAULT NULL,
  BankIndex   	int        	DEFAULT NULL,
  BankName    	Varchar(64)	DEFAULT NULL,
  BankAccount 	Varchar(20)	DEFAULT NULL,
  AccountName 	Varchar(64)	DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);

CREATE TABLE hs_deposits (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code     Varchar(32)   DEFAULT NULL,
  UserCode     Varchar(32)   DEFAULT NULL,
  ApplyTime    datetime      		DEFAULT NULL,
  ApplyCount   Float         DEFAULT NULL,
  State        int           DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);
CREATE TABLE hs_medias (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code     	 Varchar(32)  DEFAULT NULL,
  MediaFile  Varchar(40)   DEFAULT NULL,
  Size       int           		DEFAULT NULL,
  Type       int           DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);

CREATE TABLE hs_service_account (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Account    	 Varchar(32)   DEFAULT NULL,
  Passwd       Varchar(32)    DEFAULT NULL,
  EMail        Varchar(64)    DEFAULT NULL,
  Alias        Varchar(64)    DEFAULT NULL,
  Address      Varchar(128)   DEFAULT NULL,
  AccountLeft  Float          DEFAULT NULL,
  LockMount    float          DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Account (Account)
);

CREATE TABLE hs_service_protocol (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code       Varchar(32)  DEFAULT NULL,
  UserCode 	 Varchar(32)  DEFAULT NULL,
  ProCode    Varchar(32)   DEFAULT NULL,
  StartDate  date          DEFAULT NULL,
  StopDate   date          DEFAULT NULL,
  City       Varchar(32)   DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);

CREATE TABLE hs_sale_account (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Account      Varchar(32)   DEFAULT NULL,
  Password   	 varchar(64)   DEFAULT NULL,
  EMail        Varchar(64)    DEFAULT NULL,
  Alias        Varchar(12)    DEFAULT NULL,
  Address      Varchar(128)   DEFAULT NULL,
  AccountLeft  Varchar(128)   DEFAULT NULL,
  LockMount    Float          DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Account (Account)
);
CREATE TABLE hs_sale_order (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code         Varchar(32)   DEFAULT NULL,
  UserCode   	 Varchar(32)   DEFAULT NULL,
  Info         Varchar(200)   DEFAULT NULL,
  Price        Float          DEFAULT NULL,
  RequireDate  date           DEFAULT NULL,
  CustomName   Varchar(64)    DEFAULT NULL,
  CustomPhone  Varchar(20)    DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);
CREATE TABLE hs_sale_order_attach (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code  Varchar(32)   DEFAULT NULL,
  ApplyCode  Varchar(32)   DEFAULT NULL,
  AttchFile	 Varchar(40)   DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);

CREATE TABLE hs_sale_protocol (
  Id          		int(11) 					NOT NULL AUTO_INCREMENT,
  Code  Varchar(32)   DEFAULT NULL,
  UserCode   Varchar(32)   DEFAULT NULL,
  ProCode    Varchar(32)   DEFAULT NULL,
  StartDate  date          DEFAULT NULL,
  StopDate   date          DEFAULT NULL,
  City       Varchar(32)   DEFAULT NULL,
  PRIMARY KEY (Id),
  UNIQUE KEY Code (Code)
);