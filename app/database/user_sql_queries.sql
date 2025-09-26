delete from skillnamemapping where skillnamemappingId >5;

rename table skills to skill;

delimiter $$
create trigger call_inc_id
before insert on user for each row 
begin
    set new.userId = inc_id();
end$$
delimiter ;

delimiter $$
create function inc_id() returns int deterministic
begin 
	declare newId int;
    select ifnull(max(userId),0)  into newId from user;
    return newId + 1  ;
end $$
delimiter ;

INSERT INTO user (firstname, phoneNumber,age) VALUES ('Yash', '9321533499',30);
select * from user;

alter table personalInfo 
modify column changed_at datetime  on update current_timestamp;

alter table user
add column age int not null after phoneNumber ;


alter table user
drop column age ;

select * from user;

delete from  user where userId = 9;

with  workX_pInfo_cte as (
select w.personalInfoId, w.totalYears 
from workexperience as w inner join personalInfo as p
on w.personalInfoId = p.personalInfoId),

user_pInfo_cte as (
select p.personalInfoId, u.firstname 
from  personalInfo as p right join user as u 
on  p.userId = u.userId )
-- select * from user_pInfo_cte;

select u.firstname , w.totalYears 
from user_pInfo_cte as u left join workX_pInfo_cte as w
on  u.personalInfoId = w.personalInfoId;

select count(age),max(age),min(age), sum(age) ,avg(age),round(avg(age),2) from user where age >0;
 
 alter table user
 add column lastname varchar(255) not null ;
 
 alter table user 
 modify column lastname varchar(255) not null after firstname;
 
update  user
set lastname ='Rathod' where userId =7;

select * from user;

select userId, concat(firstname,' ',lastname)  as fullname,age, concat(substring(firstname,1,1),'',substring(lastname,1,1)) as initials from user order by age desc; 

select softId,skillId,skill,skillLevel,trim(trailing 'years' from experience) as experience from soft;

alter table user
-- modify column age int not null after phoneNumber ;
 -- add constraint   chk_age check (age>18) ;
  drop constraint   chk_age;
 
 
 select * from user;
 SET SQL_SAFE_UPDATES = 0;
 update user set age = 16 where userId = 3;

update user
set age = case 
    when userId = 1 then 22
    when userId = 2 then 24
    when userId = 3 then 21
    when userId = 4 then 29
    when userId = 5 then 23
    when userId = 6 then 26
    when userId = 7 then 27
    else 28
end;

update user set age = 16 where userId = 8;

alter table proficiencymapping rename column skillNameId to proficiencyId;

with snm_sn_cte as (
select snm.skillNameMappingId, sn.name
from skillnamemapping as snm left join skillName as sn
on snm.skillNameId = sn.skillNameId),
-- union 
-- select snm.skillNameMappingId, sn.name
-- from skillnamemapping as snm right join skillName as sn
-- on snm.skillNameId = sn.skillNameId)
-- select * from snm_sn_cte;
-- select name as skill, count(name) as no_of_ids from snm_sn_cte group by name;

pnm_pn_cte as (
select pnm.proficiencymappingId, p.name
from proficiencymapping as pnm join proficiency as p 
on  pnm.proficiencyId = p.proficiencyId)
-- select * from pnm_pn_cte;
 select  name as proficiency,count(proficiencymappingId) as no_of_ids from pnm_pn_cte group by name;

select t.technicalId, t.category, sn.name
from skillName as sn join skillnamemapping as snm on sn.skillNameId = snm.skillNameId
join  technical as t on t.technicalId = snm.technicalId order by t.technicalId;

alter table user
-- modify column phoneNumber varchar(255) not null ,
modify column userId int ;
-- add constraint chk_phoneNumber_length check (char_length(phoneNumber) = 10);

alter table  skill
modify column workexperienceId int unique not null;


select u.firstname, w.totalYears from user as u 
join personalInfo as p on u.userId=p.userId
join workExperience as w on p.personalInfoId=w.personalInfoId
where totalYears > 3;

select u.firstname,p.professionalTitle,w.currentEmployer,w.totalYears,t.category,s.skill,s.skillLevel,sn.name as SkillName,pr.name as Proficiency
from  user as u left join personalinfo as p on u.userId = p.userId
left join workexperience as w on p.personalInfoId = w.personalInfoId
left join skill as sk on w.workexperienceId = sk.workexperienceId
left join technical as t on sk.skillId = t.skillId
left join soft as s on  sk.skillId = s.skillId
left join skillnamemapping as snm on snm.technicalId = t.technicalId
left join skillname as sn on sn.skillNameId = snm.skillNameId
left join proficiencymapping as pm on  pm.technicalId = t.technicalId
left join proficiency as pr on pr.proficiencyId = pm.proficiencyId;

-- SQL querries
-- 1
select  u.firstname,p.professionalTitle,w.currentEmployer,sn.name as SkillName
from  user as u  left join personalinfo as p on u.userId = p.userId
left join workexperience as w on p.personalInfoId = w.personalInfoId
left join skill as sk on w.workexperienceId = sk.workexperienceId
left join technical as t on sk.skillId = t.skillId
left join skillnamemapping as snm on snm.technicalId = t.technicalId
left join skillname as sn on sn.skillNameId = snm.skillNameId;


-- 2
select u.userId,s.skill,t.skillId from user as u 
left join personalinfo as p on u.userId = p.userId 
left join workexperience as w on p.personalInfoId = w.personalInfoId 
left join skill as sk on w.workexperienceId = sk.workexperienceId 
left join technical as t on sk.skillId = t.skillId 
left join soft as s on sk.skillId = s.skillId 
where s.skill is null and t.skillId is not null;


-- 3 
select u.userId,s.skill as soft_skill,sn.name as technical_skill,pr.name as Proficiency from user as u 
left join personalinfo as p on u.userId = p.userId 
left join workexperience as w on p.personalInfoId = w.personalInfoId 
left join skill as sk on w.workexperienceId = sk.workexperienceId 
left join technical as t on sk.skillId = t.skillId 
left join soft as s on sk.skillId = s.skillId 
left join skillnamemapping as snm on snm.technicalId = t.technicalId 
left join skillname as sn on sn.skillNameId = snm.skillNameId 
left join proficiencymapping as pm on pm.technicalId = t.technicalId 
left join proficiency as pr on pr.proficiencyId = pm.proficiencyId; 

-- 4
select u.userid, u.firstname,w.totalYears,count(snm.technicalId) as Count
from  user as u left join personalinfo as p on u.userId = p.userId
left join workexperience as w on p.personalInfoId = w.personalInfoId
left join skill as sk on w.workexperienceId = sk.workexperienceId
left join technical as t on sk.skillId = t.skillId
left join skillnamemapping as snm on snm.technicalId = t.technicalId
group by u.firstname,w.totalYears, u.userid;

-- 6
select u.firstname,count(s.softId )+count(t.technicalId) as total_skill
from  user as u left join personalinfo as p on u.userId = p.userId
 join workexperience as w on p.personalInfoId = w.personalInfoId
 join skill as sk on w.workexperienceId = sk.workexperienceId
 join technical as t on sk.skillId = t.skillId
 join soft as s on  sk.skillId = s.skillId
 left join skillnamemapping as snm on snm.technicalId = t.technicalId 
left join skillname as sn on sn.skillNameId = snm.skillNameId 
left join proficiencymapping as pm on pm.technicalId = t.technicalId 
left join proficiency as pr on pr.proficiencyId = pm.proficiencyId
group by firstname
order by count(s.softId )+count(t.technicalId) desc
 limit 5;


-- 5
select u.userId,u.firstname,sn.name as technical_skill,pr.name as Proficiency from user as u 
left join personalinfo as p on u.userId = p.userId 
left join workexperience as w on p.personalInfoId = w.personalInfoId 
left join skill as sk on w.workexperienceId = sk.workexperienceId 
left join technical as t on sk.skillId = t.skillId 
left join soft as s on sk.skillId = s.skillId 
left join skillnamemapping as snm on snm.technicalId = t.technicalId 
left join skillname as sn on sn.skillNameId = snm.skillNameId 
left join proficiencymapping as pm on pm.technicalId = t.technicalId 
left join proficiency as pr on pr.proficiencyId = pm.proficiencyId; 


-- 7
select created_by as userId,name  from skillname where is_active = false;

-- 8
select u.userId,u.firstname,w.totalYears as work_exp,pr.name as Proficiency from user as u 
left join personalinfo as p on u.userId = p.userId 
left join workexperience as w on p.personalInfoId = w.personalInfoId 
left join skill as sk on w.workexperienceId = sk.workexperienceId 
left join technical as t on sk.skillId = t.skillId 
left join soft as s on sk.skillId = s.skillId 
left join skillnamemapping as snm on snm.technicalId = t.technicalId 
left join skillname as sn on sn.skillNameId = snm.skillNameId 
left join proficiencymapping as pm on pm.technicalId = t.technicalId 
left join proficiency as pr on pr.proficiencyId = pm.proficiencyId
where w.totalYears > 10 and pm.proficiencyMappingId is null; 

-- 9
select name as skills,changed_at from skillname 
where  changed_at >= date_sub('2024-09-24 00:00:00',interval 30 DAY)
union  select  skill as skills,changed_at from soft
where  changed_at >= date_sub('2024-09-24 00:00:00',interval 30 DAY);

-- 10
select name as skills,changed_at,deleted_by from skillname 
where  changed_by is null and deleted_by is not null
union  select  skill as skills,changed_at,deleted_by from soft
where  changed_by is null and deleted_by is not null;

-- 11 
select u.firstname,t.category, count(t.skillId) as no_of_skills
from  user as u left join personalinfo as p on u.userId = p.userId
 join workexperience as w on p.personalInfoId = w.personalInfoId
 join skill as sk on w.workexperienceId = sk.workexperienceId
 join technical as t on sk.skillId = t.skillId
 join skillnamemapping as snm on snm.technicalId = t.technicalId
 group by u.firstname,t.category;
 
 -- 13
 with user_skill_active_cte as (
 select u.firstname, count(snm.is_active) as active
 from  user as u left join personalinfo as p on u.userId = p.userId
 join workexperience as w on p.personalInfoId = w.personalInfoId
 join skill as sk on w.workexperienceId = sk.workexperienceId
 left join technical as t on sk.skillId = t.skillId 
left join soft as s on sk.skillId = s.skillId 
left join skillnamemapping as snm on snm.technicalId = t.technicalId 
left join skillname as sn on sn.skillNameId = snm.skillNameId 
left join proficiencymapping as pm on pm.technicalId = t.technicalId 
left join proficiency as pr on pr.proficiencyId = pm.proficiencyId
where  snm.is_active is true
group by u.firstname
 ),
user_skill_inactive_cte as (
 select u.firstname, count(snm.is_active) as inactive
 from  user as u left join personalinfo as p on u.userId = p.userId
 left join workexperience as w on p.personalInfoId = w.personalInfoId
 left join skill as sk on w.workexperienceId = sk.workexperienceId
 left join technical as t on sk.skillId = t.skillId 
left join soft as s on sk.skillId = s.skillId 
left join skillnamemapping as snm on snm.technicalId = t.technicalId 
left join skillname as sn on sn.skillNameId = snm.skillNameId 
left join proficiencymapping as pm on pm.technicalId = t.technicalId 
left join proficiency as pr on pr.proficiencyId = pm.proficiencyId
where  snm.is_active is false
group by u.firstname
 )
 
 select u.firstname,  ifnull(( (ifnull(usac.active,0) /(ifnull(usic.inactive,0)+ifnull(usac.active,0)) )* 100),0)  as active ,  ifnull(( (ifnull(usic.inactive,0) /(ifnull(usic.inactive,0)+ifnull(usac.active,0)) )* 100),0)  as Inactive 
from  user as u left join user_skill_active_cte as usac on  u.firstname =  usac.firstname
left join user_skill_inactive_cte as usic on u.firstname =  usic.firstname
group by firstname;



-- 12
select p.department,round(avg(w.totalYears),2) as avg_years
from  user as u left join personalinfo as p on u.userId = p.userId
 join workexperience as w on p.personalInfoId = w.personalInfoId
 group by p.department;

-- 14
select name,changed_at from skillname 
order by changed_at desc limit 1;

-- 15
with user_level_cte as (
select u.firstname, sn.name as skill_Name,pr.name as proficiency, pr.proficiency_rating,
dense_rank() over (partition by u.firstname,sn.name order by pr.proficiency_rating desc) as level
 from  user as u left join personalinfo as p on u.userId = p.userId
 left join workexperience as w on p.personalInfoId = w.personalInfoId
left join skill as sk on w.workexperienceId = sk.workexperienceId
 left join technical as t on sk.skillId = t.skillId 
left join skillnamemapping as snm on snm.technicalId = t.technicalId 
left join skillname as sn on sn.skillNameId = snm.skillNameId 
left join proficiencymapping as pm on pm.technicalId = t.technicalId 
left join proficiency as pr on pr.proficiencyId = pm.proficiencyId
)

select firstname,skill_Name,proficiency from user_level_cte where level = 1 and skill_Name is not null;

-- 16
 select u.firstname, sn.name as skill_Name,count(pr.name)
 from  user as u left join personalinfo as p on u.userId = p.userId
 left join workexperience as w on p.personalInfoId = w.personalInfoId
 left join skill as sk on w.workexperienceId = sk.workexperienceId
 left join technical as t on sk.skillId = t.skillId 
left join skillnamemapping as snm on snm.technicalId = t.technicalId 
left join skillname as sn on sn.skillNameId = snm.skillNameId 
left join proficiencymapping as pm on pm.technicalId = t.technicalId 
left join proficiency as pr on pr.proficiencyId = pm.proficiencyId
group by firstname,skill_Name
having count(pr.name)>1 and skill_Name is not null;

-- 17
select u.firstname,sk.skillId,snm.skillNameMappingId,pm.proficiencymappingId,pr.name,sn.name,t.technicalId
 from  user as u left join personalinfo as p on u.userId = p.userId
 left join workexperience as w on p.personalInfoId = w.personalInfoId
 left join skill as sk on w.workexperienceId = sk.workexperienceId
 left join technical as t on sk.skillId = t.skillId 
left join skillnamemapping as snm on snm.technicalId = t.technicalId 
left join skillname as sn on sn.skillNameId = snm.skillNameId 
left join proficiencymapping as pm on pm.technicalId = t.technicalId 
left join proficiency as pr on pr.proficiencyId = pm.proficiencyId
where proficiencymappingId is not null and skillnamemappingId is  null;




-- 18
with user_tech_cte as (
select u.userId,u.firstname,t.changed_at,t.created_by
 from  user as u left join personalinfo as p on u.userId = p.userId
 left join workexperience as w on p.personalInfoId = w.personalInfoId
 left join skill as sk on w.workexperienceId = sk.workexperienceId
 left join technical as t on sk.skillId = t.skillId 
 where t.changed_at is not null and t.created_by != u.userId
),
user_soft_cte as (
select u.userId,u.firstname,s.changed_at,s.created_by
 from  user as u left join personalinfo as p on u.userId = p.userId
 left join workexperience as w on p.personalInfoId = w.personalInfoId
 left join skill as sk on w.workexperienceId = sk.workexperienceId
 left join soft as s on sk.skillId = s.skillId
 where s.changed_at is not null and s.created_by != u.userId
)

 select * from user_soft_cte
union select * from user_tech_cte;



