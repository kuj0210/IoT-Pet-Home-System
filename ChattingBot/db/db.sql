drop database SystemData;

create database SystemData 
	DEFAULT CHARACTER 
	SET utf8 collate utf8_general_ci;

use SystemData;

create table naverUser(
	user_key varchar(50),
	serial varchar(50),
	Email varchar(100),
	petName varchar(50),
	primary key (user_key, serial)
		) ENGINE=InnoDB default character set utf8 collate utf8_general_ci;

create table TempID(
	user_key varchar(50),
	ID varchar(50),
	primary key (user_key, ID)
		) ENGINE=InnoDB default character set utf8 collate utf8_general_ci;

create table OldImageList(
	addr varchar(100),
	serial VARCHAR(50),
	primary key (addr)
		) ENGINE=InnoDB default character set utf8 collate utf8_general_ci;

create table homeSystem(
	serial varchar(50),
	petCount int default 1, 
	primary key (serial)
	) ENGINE=InnoDB default character set utf8 collate utf8_general_ci;

create table request(
	serial varchar(50),
	requestor varchar(50),
	request varchar(50),
	FOREIGN KEY (serial) REFERENCES homeSystem (serial)
	) ENGINE=InnoDB default character set utf8 collate utf8_general_ci;
		

select * from naverUser;
select * from homeSystem;
insert naverUser value("kEa7lN2aHtb7oXa6EIb1KA","SR0003","beta1360@naver.com","woojin");
insert naverUser value("u9-NF6yuZ8H8TAgj1uzqnQ","SR0002","on_11@naver.com","DDakGGi_GGongGGi");
insert naverUser value("testertester123f","SR0003","beta1360sh@gmail.com","seok");
insert naverUser value("3213123tester123f","SR0003","beta1360sh@gmail.com","seok");
insert homeSystem value("SR0001",1);
insert homeSystem value("SR0002",2);
insert homeSystem value("SR0003",3);

insert request VALUE("SR0003","kEa7lN2aHtb7oXa6EIb1KA","open feed");
insert request VALUE("SR0003","testertester123f","camera open");
insert request VALUE("SR0003","3213123tester123f","open camera");
insert request VALUE("SR0003","3213123tester123f","UPDATE");

select * from naverUser;
select * from homeSystem;
select * from request;
