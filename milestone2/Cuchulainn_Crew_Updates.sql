-- UPDATE Query

--reviewCount

update business
set reviewcount = a.count
from (select business_id, count(stars)
from review
group by business_id) a
where business.business_id = a.business_id;

--numCheckIns

update business
set numCheckins = a.sum
from(
select business_id, sum(count)
from checkins
group by business_id) a
where business.business_id = a.business_id;

--reviewRating

update business
set reviewrating = (a.sum / a.count)
from (select business_id, count(stars), sum(stars)
from review
group by business_id) a
where business.business_id = a.business_id;


-- FOR PAPER

--sample successful
SELECT
	b.name, 
	b.reviewrating,
	b.reviewcount,
	b.city, 
	b.postal_code,
	AVG(reviewcount) AS avgCount,
	AVG(reviewrating) AS myrate,
	c.cat_name
From 
	business AS b
INNER JOIN
	categories AS c ON b.business_id = c.business_id
WHERE
	postal_code = '85251' AND
	cat_name = 'Shopping' AND
	b.reviewcount >= (SELECT AVG(reviewcount) FROM business WHERE postal_code = '85251') AND
	b.reviewrating >= ((SELECT AVG(reviewrating) FROM business WHERE postal_code = '85251'))
GROUP BY
	b.name, b,reviewrating, b.city, b.postal_code, b.reviewcount,c.cat_name
ORDER BY	
	b.reviewrating DESC

--sample popular
SELECT
	b.name, 
	b.numcheckins,
	b.city,
	b.postal_code,
	c.cat_name
From 
	business AS b
INNER JOIN
    categories AS c ON b.business_id = c.business_id
WHERE
	postal_code = '85251' AND
	cat_name = 'Shopping' AND
	numcheckins >= (SELECT AVG(numcheckins) FROM business WHERE postal_code = '85251')
GROUP BY
	b.name,b.numcheckins,b.city,b.postal_code,c.cat_name
ORDER BY
	b.numcheckins DESC;





