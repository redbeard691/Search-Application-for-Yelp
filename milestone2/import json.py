
import json
import psycopg2
from datetime import datetime

def cleanStr4SQL(s):
    return s.replace("'","`").replace("\n"," ")

def int2BoolStr (value):
    if value == 0:
        return 'False'
    else:
        return 'True'
"""
def insert2BusinessTable():
    # Reading the JSON file
    with open('C://Users//Nick//Desktop//451_Project//Yelp-CptS451//Yelp-CptS451//yelp_business.JSON', 'r') as f:

        line = f.readline()
        count_line = 0
        # Connect to yelpdb database on postgres server using psycopg2
        # TODO: update the database name, username, and password
        try:
            conn = psycopg2.connect("dbname='milestone1db' user='postgres' host='localhost' password='admin'")
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()

        while line:
            data = json.loads(line)
            # Generate the INSERT statement for the current business

            sql_str = "INSERT INTO business (business_id, name, address,city, state_code, postal_code, latitude, longitude, stars, reviewcount, is_open, numcheckins, reviewrating) " \
                      "VALUES ('" + cleanStr4SQL(data['business_id']) + "','" + cleanStr4SQL(data["name"]) + "','" + cleanStr4SQL(data["address"]) + "','" + \
                      cleanStr4SQL(data["city"]) + "','" + cleanStr4SQL(data["state"]) + "','" + cleanStr4SQL(data["postal_code"]) + "'," + str(data["latitude"]) + "," + \
                      str(data["longitude"]) + "," + str(data["stars"]) + "," + str(data["review_count"]) + "," + str(data["is_open"]) + ",0 ,0" + ");"

            try:
                cur.execute(sql_str)
            except:
                print("Insert to businessTABLE failed!")
            conn.commit()
            # Optionally you might write the INSERT statement to a file.
            # outfile.write(sql_str)
            line = f.readline()
            count_line += 1
        cur.close()
        conn.close()
    print(count_line)
    # outfile.close() # uncomment this line if you are writing the INSERT statements to an output file.
    f.close()
"""

"""
def insert2UsersTable():
    #reading the JSON file
    with open('C://Users//Nick//Desktop//451_Project//Yelp-CptS451//Yelp-CptS451//yelp_user.JSON','r') as f:

        line = f.readline()
        count_line = 0

        #connect to yelpdb database on postgres server using psycopg2
        try:
            conn = psycopg2.connect("dbname='milestone1db' user='postgres' host='localhost' password='admin'")
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()

        while line:
            data = json.loads(line)
            #Generate the INSERT statement for the current user
            # include values for all userTable attributes

            sql_str = "INSERT INTO users (user_id, yelping_since, name, review_count, useful, funny, fans, cool, average_stars) " \
                      "VALUES ('" + cleanStr4SQL(data['user_id']) + "','" + cleanStr4SQL(data["yelping_since"]) + "','" + cleanStr4SQL(data["name"]) + "'," + \
                      str(data["review_count"]) + "," + str(data["useful"]) + "," + str(data["funny"]) + "," + str(data["fans"]) + "," + \
                      str(data["cool"]) + "," + str(data["average_stars"]) + ");"
            try:
                cur.execute(sql_str)
            except:
                print("Insert to userTABLE failed!")
            conn.commit()
            line = f.readline()
            count_line +=1

        cur.close()
        conn.close()

    print(count_line)
    f.close()
"""

"""
def insert2ReviewTable():
    #reading the JSON file
    with open('C://Users//Nick//Desktop//451_Project//Yelp-CptS451//Yelp-CptS451//yelp_review.JSON', 'r') as f:

        line = f.readline()
        count_line = 0

        #connect to yelpdb database on postgres server using psycopg2
        try:
            conn = psycopg2.connect("dbname='milestone1db' user='postgres' host='localhost' password='admin'")
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()

        while line:
            data = json.loads(line)
            #Generate the INSERT statement for the current user
            # include values for all userTable attributes

            sql_str = "INSERT INTO reviews (review_id, user_id, business_id, stars ,date, text, useful, funny, cool) " \
                      "VALUES ('" + cleanStr4SQL(data['review_id']) + "','" + cleanStr4SQL(data["user_id"]) + "','" + cleanStr4SQL(data["business_id"]) +  \
                      "'," + str(data["stars"]) + ",'" + cleanStr4SQL(data["date"]) + "','" + cleanStr4SQL(data["text"]) + "'," + str(data["useful"]) +  \
                      "," + str(data["funny"]) + "," + str(data["cool"]) + ");"
            try:
                cur.execute(sql_str)
            except:
                print("Insert to ReviewTABLE failed!")
            conn.commit()
            line = f.readline()
            count_line +=1

        cur.close()
        conn.close()

    print(count_line)
    f.close()
"""

"""
def insert2CheckinTable():
    #reading the JSON file
    with open('C://Users//Nick//Desktop//451_Project//Yelp-CptS451//Yelp-CptS451//yelp_checkin.JSON', 'r') as f:

        line = f.readline()
        count_line = 0

        #connect to yelpdb database on postgres server using psycopg2
        try:
            conn = psycopg2.connect("dbname='milestone1db' user='postgres' host='localhost' password='admin'")
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()

        while line:
            data = json.loads(line)


            for day, hours_dict in data["time"].items():
                for hour, count in hours_dict.items():
                    sql_str = "INSERT INTO Checkins (business_id, day , time, count) " \
                    "VALUES ('" + cleanStr4SQL(data['business_id']) + "','" + str(day) + "','" + str(hour) + \
                    "'," + str(count) + ");"
                    try:
                        cur.execute(sql_str)
                        print("...")
                    except:
                        print("Insert to CheckinTABLE failed!")
                    conn.commit()
                    line = f.readline()
                    count_line += 1

        cur.close()
        conn.close()

    print(count_line)
    f.close()
"""

""" Not Done Needs more work
def insert2AttributeTable():
    # reading the JSON file
    with open('C://Users//Nick//Desktop//451_Project//Yelp-CptS451//Yelp-CptS451//yelp_business.JSON', 'r') as f:

        line = f.readline()
        count_line = 0

        # connect to yelpdb database on postgres server using psycopg2
        try:
            conn = psycopg2.connect("dbname='milestone1db' user='postgres' host='localhost' password='admin'")
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()

        while line:
            data = json.loads(line)

            for key, val in data["attributes"].items():
                
                sql_str = "INSERT INTO business_attributes (business_id, attr_name, value) " \
                      "VALUES ('" + cleanStr4SQL(data['business_id']) + "','" + str(key) + "','" + str(val) + "');"
                try:
                    cur.execute(sql_str)
                    print("...")
                except:
                    print("Insert to ReviewTABLE failed!")
                conn.commit()
                line = f.readline()
                count_line += 1

        cur.close()
        conn.close()

    print(count_line)
    f.close()
"""


def insert2CategoryTable():
    # reading the JSON file
    with open('C://Users//Nick//Desktop//451_Project//Yelp-CptS451//Yelp-CptS451//yelp_business.JSON', 'r') as f:

        line = f.readline()
        count_line = 0

        # connect to yelpdb database on postgres server using psycopg2
        try:
            conn = psycopg2.connect("dbname='milestone1db' user='postgres' host='localhost' password='admin'")
        except:
            print('Unable to connect to the database!')
        cur = conn.cursor()

        while line:
            data = json.loads(line)

            for key in data["categories"]:

                sql_str = "INSERT INTO categories (business_id, cat_name) " \
                          "VALUES ('" + cleanStr4SQL(data['business_id']) + "','" + cleanStr4SQL(key) + "');"
                try:
                    cur.execute(sql_str)
                    print("...")
                except:
                    print("Insert to categoryTABLE failed!" + data['business_id'] + " " + key)
                conn.commit()
                line = f.readline()
                count_line += 1

        cur.close()
        conn.close()

    print(count_line)
    f.close()

insert2CategoryTable()
#insert2CheckinTable()
#insert2ReviewTable()
#insert2UsersTable()
#insert2BusinessTable()


