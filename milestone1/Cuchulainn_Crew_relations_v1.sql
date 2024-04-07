-- Cuchulainn Crew 
-- Nick Sturgeon

-- Template to copy data from JSON files
-- WARNING CHECK PATH BEFORE UPDATING INFO!!!!!
\copy business (zip) FROM 'c://Users//Nick//OneDrive//WSU//451//451_Project//Yelp-CptS451//Yelp-CptS451//milestone1DB.csv' DELIMITER ',' CSV

CREATE TABLE business (
business_ID     INT NOT NULL,
review_count    INT,
num_checkin     INT,
latitude        DECIMAL(10, 9),
longitude       DECIMAL(11, 8),
address         VARCHAR(100),
name            VARCHAR(100),
city            VARCHAR(100),
neighborhood    VARCHAR(100),
state           VARCHAR(10),
zip             VARCHAR(20),
stars           DECIMAL(2, 1),
PRIMARY KEY(business_ID)
);

CREATE TABLE business_attribute (
business_ID
details     VARCHAR(100),
val         INT,
PRIMARY KEY(details)
);

CREATE TABLES business_hours (
day_of_week     VARCHAR(10),
close_time      VARCHAR(5),
open_time       VARCHAR(5),
PRIMARY KEY(day_of_week)
);

CREATE TABLE reviews (
review_id    VARCHAR(10) NOT NULL,
stars        INT,
text         VARCHAR(300),
date_created VARCHAR(10),
votes_funny  INT,
votes_cool   INT,
votes_useful INT,
PRIMARY KEY(review_id)
);

CREATE TABLE users (
user_id     INT NOT NULL,
name        VARCHAR(20),
review_count INT,

);

CREATE TABLE checkin (
date_created VARCHAR(20),
PRIMARY KEY(date_created)
);

CREATE TABLE categories (
category_id INT NOT NULL,
name VARCHAR(30),
PRIMARY KEY(category_id)
);

-- RELATIONS
CREATE TABLE has (
date_created VARCHAR(20),
business_ID  INT,
PRIMARY KEY(date_created, business_ID),
FOREIGN KEY (business_ID) REFERENCES business On DELETE CASCADE
);

CREATE TABLE review (
business_ID     INT,
review_id       INT,
user_id         INT,
Primary KEY (business_ID, review_id,user_id),
FOREIGN KEY (business_ID) REFERENCES business,
FOREIGN KEY (review_id) REFERENCES reviews,
FOREIGN KEY (user_id) REFERENCES users
);

CREATE TABLE category (
category_id INT,
business_ID INT,
Primary KEY (category_id, business_ID),
FOREIGN KEY (category_id) REFERENCES categories,
FOREIGN KEY (business_ID) REFERENCES business
);

CREATE TABLE attributes (
details     VARCHAR(100),
business_ID INT,
PRIMARY KEY(details, business_ID),
FOREIGN KEY (business_ID) REFERENCES business On DELETE CASCADE
);

CREATE TABLE has_hours (
day_of_week     VARCHAR(20),
business_ID     INT,
PRIMARY KEY(day_of_week, business_ID),
FOREIGN KEY (business_ID) REFERENCES business On DELETE CASCADE
);