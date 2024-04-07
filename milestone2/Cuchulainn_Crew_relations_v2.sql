-- Cuchulainn Crew 
-- Nick Sturgeon

-- Template to copy data from JSON files
-- WARNING CHECK PATH BEFORE UPDATING INFO!!!!!
\copy business  FROM 'c://Users//Nick//Desktop//451_Project//Yelp-CptS451//Yelp-CptS451//yelp_business.json' (FORMAT JSON)

--Done
CREATE TABLE Business (
    business_id CHAR(22) PRIMARY KEY,
    name VARCHAR(75) NOT NULL,
    address VARCHAR(100) NOT NULL,
    city VARCHAR(20) NOT NULL,
    state_code CHAR(2) NOT NULL,
    postal_code CHAR(5) NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL,
    stars FLOAT CHECK (stars <= 5 AND stars >= 0) NOT NULL,
    reviewcount INTEGER NOT NULL,
    is_open INTEGER CHECK (is_open = 0 OR is_open = 1) NOT NULL,
    numCheckins INTEGER NOT NULL,
    reviewrating FLOAT NOT NULL
    );

--Done
CREATE TABLE Users (
    user_id			CHAR(22) PRIMARY KEY,
    yelping_since	DATE NOT NULL,
    name			VARCHAR(50) NOT NULL,
    review_count	INTEGER,
    useful			INTEGER,
    funny			INTEGER,
    fans			INTEGER,
    cool			INTEGER,
    average_stars	FLOAT CHECK (average_stars <= 5.0 AND average_stars >= 0.0)
    );

--Done
CREATE TABLE reviews (
    review_id    VARCHAR(25) PRIMARY KEY,
    user_id      VARCHAR(25) NOT NULL,
    business_id  VARCHAR(25) NOT NULL,
    stars        INT CHECK( stars >= 0 AND stars <= 5),
    date DATE,
    text         VARCHAR(3000),
    useful INT CHECK(useful >= 0),
    funny  INT CHECK(funny >=0),
    cool   INT CHECK(cool >= 0),
    FOREIGN KEY(user_id) REFERENCES Users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (business_id ) REFERENCES Business(business_id) ON DELETE CASCADE
    );

--Done
CREATE TABLE Checkins (
    business_id VARCHAR(25),
    day     VARCHAR(10),
    time     VARCHAR(6),
    count    INT CHECK(count >= 0),
    PRIMARY KEY( business_id,day,time),
    FOREIGN KEY(business_id) REFERENCES Business(business_id) ON DELETE CASCADE
    );

--Done
CREATE TABLE categories (
    business_id VARCHAR(25),
    cat_name VARCHAR(50),
    PRIMARY KEY(business_id, cat_name),
    FOREIGN KEY(business_id) REFERENCES Business(business_id) ON DELETE CASCADE
);

CREATE TABLE business_attribute (
business_id VARCHAR(25) PRIMARY KEY,
attr_name VARCHAR(50) NOT NULL,
value VARCHAR(100)
);

-- RELATIONS
CREATE TABLE has (
date_created VARCHAR(20),
business_ID  INT,
PRIMARY KEY(date_created, business_ID),
FOREIGN KEY (business_ID) REFERENCES business On DELETE CASCADE
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