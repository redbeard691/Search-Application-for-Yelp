

--numCheckIns

update business
set numCheckins = a.sum
from(
select business_id, sum(count)
from checkins
group by business_id) a
where business.business_id = a.business_id;

select * from business;
