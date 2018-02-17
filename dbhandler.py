import mysql.connector
from passwordhelper import PasswordHelper
PH = PasswordHelper()


class DBHandler:
    def __init__(self, user, password, host, database, port):
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.database = database
        self.cnx = None
        self.cursor = None

    def connect(self):
        self.cnx = mysql.connector.connect(user=self.user, password=self.password,
                              host=self.host, database=self.database, port=self.port)
        self.cursor = self.cnx.cursor(dictionary=True)

    def getUser(self,username, password=""):
        query = 'SELECT * FROM User WHERE username="%s"' % username
        return self.executeGetQuery(query)
    def getUserType(self,username, password=""):
        query = 'SELECT * FROM User WHERE username="%s"' % username
        return self.executeGetQuery(query)
    def get_user_id(self):
        query = 'SELECT user_id FROM User'
        return self.executeGetQuery(query)
    def get_question_id(self):
        query = 'SELECT question_id FROM Question'
        return self.executeGetQuery(query)

    def setUser(self,user):
        query ="INSERT INTO `User` VALUES " \
                 "('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % \
                 (user.get('user_id'), user.get('username'),user.get('name'),
                  user.get('last_name'),user.get('user_type'), user.get('password'),
                  user.get('email'), user.get('student_number'), user.get('date_created'))
        return self.executeSetQuery(query)

    def setCode(self,confirmation):
        query = "INSERT INTO `User_Confirmation` VALUES " \
                "('%s', '%s', '%s', '%s')" % \
                (confirmation.get('user_confirmationID'), confirmation.get('username'), confirmation.get('email'),
                 confirmation.get('Email_key'))
        return self.executeSetQuery(query)

    def setGroup(self, group):
        query = "INSERT INTO `Create_Group` VALUES " \
                "('%s', '%s', '%s', '%s','%s')" % \
                (group.get('group_id'), group.get('user_id'), group.get('group_creator'),
                 group.get('group_name'), group.get('date_created'))
        return self.executeSetQuery(query)

    def getGroup(self,group_name):
        query = "SELECT * FROM Create_Group WHERE group_name = '%s'" % group_name
        return self.executeGetQuery(query)

    def setQuestion(self, question):
        query = "INSERT INTO `Question` VALUES " \
                "('%s', '%s', '%s', '%s','%s','%s', '%s', '%s', '%s','%s')" % \
                (question.get('question_id'), question.get('user_id'), question.get('group_name'),
                 question.get('question_creator'), question.get('question_type'), question.get('question_title'),
                 question.get('question_description'),question.get('voting_status'),question.get('question_author'),
                 question.get('date_created'))
        return self.executeSetQuery(query)

    def getInProgressQuestion(self, group_name):
        status ="In-Progress"
        query = "SELECT * FROM Question  WHERE voting_status='%s' AND group_name='%s'" % (status, group_name)
        return self.executeGetQuery(query)

    def getCompletedQuestions(self, group_name):
        status = "Completed"
        query = "SELECT * FROM Question WHERE voting_status='%s' AND group_name='%s'" % (status, group_name)
        return self.executeGetQuery(query)

    def getQuestion(self, question_title, group_name):
        query = "SELECT * FROM question WHERE question_title='%s' AND group_name='%s'" % (question_title, group_name)
        return self.executeGetQuery(query)

    def setResult(self,result):
        query = "INSERT INTO `Results` VALUES " \
                "('%s', '%s', '%s', '%s','%s','%s', '%s', %s)" % \
                (result.get('result_id'), result.get('question_title'), result.get('question_type'),
                 result.get('group_name'), result.get('count_yes'), result.get('count_no'),
                 result.get('count_abstain'), result.get('total_voters'))
        return self.executeSetQuery(query)

    def getResult(self,question_title):
        query = "SELECT * FROM Results WHERE question_title= %s" % question_title
        return self.executeGetQuery(query)

    def setVoting(self,voting):
        query = "INSERT INTO `Voting` VALUES " \
                "('%s', '%s', '%s', '%s', '%s', '%s')" % \
                (voting.get('voting_id'), voting.get('question_id'), voting.get('group_name'),
                 voting.get('question_title'), voting.get('question_type'), voting.get('voting_choice'))
        return self.executeSetQuery(query)

    def getVote(self, question_title):
        query = "SELECT * FROM Voting WHERE question_title= %s" % question_title
        return self.executeGetQuery(query)

    def set_Table(self, query):
        return self.executeSetQuery(query)

    def executeSetQuery(self, query):
        try:
            ans = self.cursor.execute(query)
        except mysql.connector.Error as err:
            print("Failed to get user: {}".format(err))
            return False
        else:
            if ans is None:
                output = True
            else:
                output = False
            return output

    def executeGetQuery(self, query):
        try:
            self.cursor.execute(query)
        except mysql.connector.Error as err:
            print("Failed to get user: {}".format(err))
            return None
        else:
            return self.cursor

    def disconnect_get(self):
        self.cursor.close()
        self.cnx.close()

    def disconnect_set(self):
        self.cnx.commit()  # Very important. Without commit() the data will not be stored in the database.
        self.cursor.close()
        self.cnx.close()

def get_user(username, user='root', password='root', host='localhost', database='upr-2fast4u-voting', port='3306'):
    DB = DBHandler(user=user, password=password, host=host, database=database, port= port)
    DB.connect()
    user = DB.getUser(username)
    output = []
    if user:
        for i in user:
            output.append(i)
    DB.disconnect_get()
    return output
def get_user_type(username, user='root', password='root', host='localhost', database='upr-2fast4u-voting', port='3306'):
    DB = DBHandler(user=user, password=password, host=host, database=database, port= port)
    DB.connect()
    user = DB.getUserType(username)
    output = None
    for i in user:
        output = i
    DB.disconnect_get()
    return output


def set_user(user):
    DB = DBHandler(user='root', password='root', host='localhost', database='upr-2fast4u-voting', port='3306')
    DB.connect()
    # Return True if successful or False otherwise.
    output = DB.setUser(user)
    DB.disconnect_set()
    return output

def set_confirmation(confirmation):
    DB = DBHandler(user='root', password='root', host='localhost', database='upr-2fast4u-voting', port='3306')
    DB.connect()
    # Return True if successful or False otherwise.
    output = DB.setUser(confirmation)
    DB.disconnect_set()
    return output

def set_question(question):
    DB = DBHandler(user='root', password='root', host='localhost', database='upr-2fast4u-voting', port='3306')
    DB.connect()
    # Return True if successful or False otherwise.
    output = DB.setQuestion(question)
    DB.disconnect_set()
    return output

def set_userTable(query, user, password, host, database, port):
    DB = DBHandler(user=user, password=password, host=host, database=database, port=port)
    DB.connect()
    # Return True if successful or False otherwise.
    output = DB.set_Table(query)
    DB.disconnect_set()
    return output

def get_CompletedQuestion(group_name):
    DB = DBHandler(user='root', password='root', host='localhost', database='upr-2fast4u-voting', port='3306')
    DB.connect()
    user = DB.getCompletedQuestions(group_name)
    output = []
    for i in user:
        output.append(i)
    DB.disconnect_get()
    return output

def get_Question(question_title, group_name):
    DB = DBHandler(user='root', password='root', host='localhost', database='upr-2fast4u-voting', port='3306')
    DB.connect()
    user = DB.getQuestion(question_title, group_name)
    output = None
    for i in user:
        output = i
    DB.disconnect_get()
    return output

def get_user_idx():
    DB = DBHandler(user='root', password='root', host='localhost', database='upr-2fast4u-voting', port='3306')
    DB.connect()
    id = DB.get_user_id()
    output = []
    for i in id:
        output.append(i)
    DB.disconnect_get()
    return output
def get_question_idx():
    DB = DBHandler(user='root', password='root', host='localhost', database='upr-2fast4u-voting', port='3306')
    DB.connect()
    id = DB.get_question_id()

    output = []
    for i in id:
        output.append(i)
    DB.disconnect_get()
    return output


def get_in_progress_question(group_name):
    DB = DBHandler(user='root', password='root', host='localhost', database='upr-2fast4u-voting', port='3306')
    DB.connect()
    quesiton = DB.getInProgressQuestion(group_name)
    output = None
    for i in quesiton:
        output = i
    DB.disconnect_get()
    return output
