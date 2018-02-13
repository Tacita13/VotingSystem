import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',
                              host='localhost', port='3306', database='upr-2fast4u-voting')
cursor = cnx.cursor(dictionary=True)

# SQL commands
drop_table = "drop table if exists User_Confirmation;"
           #"drop table if exists User_Confirmation; " \
           # "drop table if exists Voting;" \
            #"drop table if exists Results;" \
            #"drop table if exists Question;" \
            #"drop table if exists Group_Permission;" \
            #"drop table if exists Create_Group;"

createGroup = "CREATE TABLE `Create_Group` (" \
              "`group_id` varchar(10) NOT NULL," \
              "`user_id` varchar(10) NOT NULL," \
              "`group_creator` varchar(20) NOT NULL," \
              "`group_name` varchar(50) NOT NULL," \
              "`date_created` datetime DEFAULT NULL" \
              ") ENGINE=InnoDB DEFAULT CHARSET=latin1;"

createPermission = "CREATE TABLE `Group_Permission` (" \
              "`permission_id` varchar(10) NOT NULL," \
              "`group_id` varchar(10) NOT NULL," \
              "`username` varchar(20) NOT NULL," \
              "`permission_creator` varchar(50) NOT NULL," \
              "`group_name` varchar(50) NOT NULL" \
              ") ENGINE=InnoDB DEFAULT CHARSET=latin1;"

createQuestion = "CREATE TABLE `Question` (" \
                   "`question_id` varchar(15) NOT NULL," \
                   "`user_id` varchar(10) NOT NULL," \
                   "`group_name` varchar(50) NOT NULL," \
                   "`question_creator` varchar(20) NOT NULL," \
                   "`question_type` varchar(20) NOT NULL," \
                 "`question_title` varchar(50) NOT NULL," \
                 "`question_description` varchar(500) NOT NULL," \
                 "`voting_status` varchar(20) DEFAULT NULL," \
                 "`question_author` varchar(20) DEFAULT NULL," \
                 "`date_created` datetime DEFAULT NULL" \
                 ") ENGINE=InnoDB DEFAULT CHARSET=latin1;"


createResults = "CREATE TABLE `Results` (" \
                 "`result_id` varchar(10) NOT NULL," \
                 "`question_title` varchar(50) NOT NULL," \
                 "`question_type` varchar(20) NOT NULL," \
                 "`group_name` varchar(50) NOT NULL," \
                 "`count_yes` int(3) DEFAULT NULL," \
                 "`count_no` int(3) DEFAULT NULL," \
                "`count_abstain` int(3) DEFAULT NULL," \
                "`total_voters` int(3) DEFAULT NULL" \
                ") ENGINE=InnoDB DEFAULT CHARSET=latin1;"

createUser = "CREATE TABLE `User` (" \
                 "`user_id` varchar(10) NOT NULL," \
                 "`username` varchar(20) NOT NULL," \
                 "`name` varchar(20) NOT NULL," \
                 "`last_name` varchar(20) NOT NULL," \
                 "`user_type` varchar(20) NOT NULL," \
                 "`password` varchar(30) NOT NULL," \
                 "`email` varchar(30) NOT NULL," \
                 "`student_number` varchar(15) NOT NULL," \
                 "`date_created` datetime DEFAULT NULL" \
                 ") ENGINE=InnoDB DEFAULT CHARSET=latin1;"

createConfirmation = "CREATE TABLE `User_Confirmation` (" \
                 "`user_confirmationID` varchar(10) NOT NULL," \
                 "`username` varchar(20) NOT NULL," \
                 "`email` varchar(30) NOT NULL," \
                 "`Email_key` varchar(20) NOT NULL" \
                 ") ENGINE=InnoDB DEFAULT CHARSET=latin1;"


createVoting = "CREATE TABLE `Voting` (" \
                 "`voting_id` varchar(20) NOT NULL," \
                 "`question_id` varchar(10) NOT NULL," \
                 "`group_name` varchar(50) NOT NULL," \
                 "`question_title` varchar(50) NOT NULL," \
                 "`question_type` varchar(20) NOT NULL," \
                 "`voting_choice` varchar(9) NOT NULL" \
                 ") ENGINE=InnoDB DEFAULT CHARSET=latin1;"

insert_table = "INSERT INTO `User` VALUES ('512f0f02-0', 'TheDoctor', 'NoOne', 'Knows', 'Staff', 'SaraJane', 'testsubject1@gmail.com', '801-44-7821', '2018-01-28 12:00:10')"
getUser = 'SELECT * FROM User WHERE username="TheDoctor"'

try:
    cursor.execute(drop_table)
except mysql.connector.Error as err:
    print("Failed to drop Table: {}".format(err))
    exit(1)

try:
   print cursor.execute(createConfirmation)
except mysql.connector.Error as err:
    print("Failed creating Table: {}".format(err))
    exit(1)

"""
try:
    cursor.execute(insert_table)

except mysql.connector.Error as err:
    print("Failed inserting Table: {}".format(err))
    exit(1)

"""
cnx.commit()  # Very important. Without commit() the data will not be stored in the database.
cursor.close()
cnx.close()