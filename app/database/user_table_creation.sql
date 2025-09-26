create table skillName(
skillNameId int primary key AUTO_INCREMENT,
name varchar(255) Not Null,
is_active boolean default true,
created_by int  not null default 1,
created_at  datetime not null default now(),
changed_by int,
changed_at datetime on update current_timestamp,
deleted_by int,
deleted_at datetime,
uniqueIdentifier varchar(36) not null unique default (UUID()),
version datetime default current_timestamp on update current_timestamp
);

create table proficiency(
proficiencyId int primary key AUTO_INCREMENT,
name varchar(255) Not Null,
is_active boolean default true,
created_by int  not null default 1,
created_at  datetime not null default now(),
changed_by int,
changed_at datetime  on update current_timestamp,
deleted_by int,
deleted_at datetime,
uniqueIdentifier varchar(36) not null unique default (UUID()),
version datetime default current_timestamp on update current_timestamp
);

create table skillNameMapping(
skillNameMappingId int primary key AUTO_INCREMENT,
technicalId int,
foreign key (technicalId) references technical(technicalId),
skillNameId int,
foreign key (skillNameId) references skillName(skillNameId),
is_active boolean default true,
created_by int  not null default 1,
created_at  datetime not null default now(),
changed_by int,
changed_at datetime on update current_timestamp,
deleted_by int,
deleted_at datetime,
uniqueIdentifier varchar(36) not null unique default (UUID()),
version datetime default current_timestamp on update current_timestamp
);

create table proficiencyMapping(
proficiencyMappingId int primary key AUTO_INCREMENT,
technicalId int,
foreign key (technicalId) references technical(technicalId),
proficiencyId int,
foreign key (proficiencyId) references proficiency(proficiencyId),
is_active boolean default true,
created_by int  not null default 1,
created_at  datetime not null default now(),
changed_by int,
changed_at datetime on update current_timestamp,
deleted_by int,
deleted_at datetime,
uniqueIdentifier varchar(36) not null unique default (UUID()),
version datetime default current_timestamp on update current_timestamp
);

create table technical(
technicalId int primary key AUTO_INCREMENT,
skillId int,
foreign key (skillId) references skill(skillId),
category varchar(255) Not Null,
is_active boolean default true,
created_by int  not null default 1,
created_at  datetime not null default now(),
changed_by int,
changed_at datetime  on update current_timestamp,
deleted_by int,
deleted_at datetime,
uniqueIdentifier varchar(36) not null unique default (UUID()),
version datetime default current_timestamp on update current_timestamp
);

create table soft(
softId int primary key AUTO_INCREMENT,
skillId int,
foreign key (skillId) references skill(skillId),
skill varchar(255) Not Null,
skillLevel varchar(255) Not Null,
experience varchar(255) Not Null,
is_active boolean default true,
created_by int  not null default 1,
created_at  datetime not null default now(),
changed_by int,
changed_at datetime  on update current_timestamp,
deleted_by int,
deleted_at datetime,
uniqueIdentifier varchar(36) not null unique default (UUID()),
version datetime default current_timestamp on update current_timestamp
);  

create table skill(
skillId int primary key AUTO_INCREMENT,
workExperienceId int Not Null Unique,
foreign key (workExperienceId) references workExperience(workExperienceId),
is_active boolean default true,
created_by int  not null default 1,
created_at  datetime not null default now(),
changed_by int,
changed_at datetime  on update current_timestamp,
deleted_by int,
deleted_at datetime,
uniqueIdentifier varchar(36) not null unique default (UUID()),
version datetime default current_timestamp on update current_timestamp
);


create table workExperience(
workExperienceId int primary key AUTO_INCREMENT,
personalInfoId int Not Null Unique,
foreign key (personalInfoId) references personalInfo(personalInfoId),
currentEmployer varchar(255) Not Null,
totalYears int Not Null,
is_active boolean default true,
created_by int  not null default 1,
created_at  datetime not null default now(),
changed_by int,
changed_at datetime  on update current_timestamp,
deleted_by int,
deleted_at datetime,
uniqueIdentifier varchar(36) not null unique default (UUID()),
version datetime default current_timestamp on update current_timestamp
);

create table personalInfo(
personalInfoId int primary key  AUTO_INCREMENT,
userId int Not Null Unique,
foreign key (userId) references user(userId),
professionalTitle varchar(255) Not Null,
company varchar(255) Not Null,
department varchar(255) Not Null,
is_active boolean default true,
created_by int  not null default 1,
created_at  datetime not null default now(),
changed_by int,
changed_at datetime  on update current_timestamp,
deleted_by int,
deleted_at datetime,
uniqueIdentifier varchar(36) not null unique default (UUID()),
version datetime default current_timestamp on update current_timestamp
);


create table user(
userId int primary key AUTO_INCREMENT,
firstname varchar(255) Not Null,
lastname varchar(255) Not Null,
phoneNumber varchar(255) Not Null,
age int not null check(age>18),
is_active boolean default true,
created_by int  not null default 1,
created_at  datetime not null default now(),
changed_by int,
changed_at datetime on update current_timestamp,
deleted_by int,
deleted_at datetime,
uniqueIdentifier varchar(36) not null unique  default (UUID()),
version datetime default current_timestamp on update current_timestamp
);







