import mysql.connector
from passwordhelper import PasswordHelper
PH = PasswordHelper()


class DBHandler:
    def __init__(self, user, password, host, port, database):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.cnx = None
        self.cursor = None

    def connect(self):
        self.cnx = mysql.connector.connect(user=self.user, password=self.password,
                              host=self.host, port= self.port, database=self.database)
        self.cursor = self.cnx.cursor(dictionary=True)

    def getUser(self,username, password=""):
        query = 'SELECT * FROM User WHERE username="%s"' % username

        try:
            self.cursor.execute(query)

        except mysql.connector.Error as err:
            print("Failed to get user: {}".format(err))
            exit(1)
        else:
            return self.cursor

    def setUser(self,user):
        query ="INSERT INTO `User` VALUES " \
                 "('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
                 (user.get('user_id'), user.get('username'),user.get('name'),
                  user.get('last_name'),user.get('user_type'), user.get('password'),
                  user.get('email'), user.get('student_number'), user.get('date_created'))
        try:
            self.cursor.execute(query)
        except mysql.connector.Error as err:
            print("Failed to get user: {}".format(err))
            exit(1)
        else:
            return True

    def setCode(self,confirmation):
        query = "INSERT INTO `User_Confirmation` VALUES " \
                "('%s', '%s', '%s', '%s')" % \
                (confirmation.get('user_confirmationID'), confirmation.get('username'), confirmation.get('email'),
                 confirmation.get('Email_key'))
        try:
            self.cursor.execute(query)
        except mysql.connector.Error as err:
            print("Failed to get user: {}".format(err))
            exit(1)
        else:
            return True

    def disconnect_get(self):
        self.cursor.close()
        self.cnx.close()

    def disconnect_set(self):
        self.cnx.commit()  # Very important. Without commit() the data will not be stored in the database.
        self.cursor.close()
        self.cnx.close()

def get_user(username):
    DB_TEST_1 = DBHandler(user='root', password='root', host='localhost', port='3306', database='upr-2fast4u-voting')
    DB_TEST_1.connect()
    user = DB_TEST_1.getUser(username)
    output = None
    for i in user:
        output = i
    DB_TEST_1.disconnect_get()
    return output



def set_user(user):
    DB_TEST_2 = DBHandler(user='root', password='root', host='localhost', port='3306', database='upr-2fast4u-voting')
    DB_TEST_2.connect()
    # Return True if successful or False otherwise.
    DB_TEST_2.setUser(user)
    DB_TEST_2.disconnect_set()

def set_confirmation(confirmation):
    DB_TEST_2 = DBHandler(user='root', password='root', host='localhost', port='3306', database='upr-2fast4u-voting')
    DB_TEST_2.connect()
    # Return True if successful or False otherwise.
    DB_TEST_2.setUser(confirmation)
    DB_TEST_2.disconnect_set()
