import mysql.connector
from passwordhelper import PasswordHelper
import os
import re

PH = PasswordHelper()

# Comment this part for testing
cred = os.environ["CLEARDB_DATABASE_URL"]
creds = re.split('[/:@?]+', cred)

# Add Credentials for testing
userDB = creds[1][:14]
passwordDB = creds[2]
hostDB = creds[3]
databaseDB = creds[4]
portDB = "3306"

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

    def setTable(self, table):
        return self.executeSetQuery(table)

    def getUser(self,username, password=""):
        query = 'SELECT * FROM User WHERE username="%s"' % username
        return self.executeGetQuery(query)

    def getUserType(self,username, password=""):
        query = 'SELECT user_type FROM User WHERE username="%s"' % username
        return self.executeGetQuery(query)

    def get_user_id(self):
        query = 'SELECT user_id FROM User'
        return self.executeGetQuery(query)
    def get_question_id(self):
        query = 'SELECT question_id FROM Question'
        return self.executeGetQuery(query)

    def getAllUserStudent(self, user_type="Student"):
        query = 'SELECT * FROM User WHERE user_type="%s"' % user_type
        return self.executeGetQuery(query)

    def setUser(self,user):
        query ="INSERT INTO `User` VALUES " \
                 "('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', %s)" % \
                 (user.get('user_id'), user.get('username'),user.get('name'),
                  user.get('last_name'),user.get('user_type'), user.get('password'),
                  user.get('email'), user.get('student_number'), 'CURRENT_DATE()')
        return self.executeSetQuery(query)

    def setCode(self,confirmation):
        query = "INSERT INTO `User_Confirmation` VALUES " \
                "('%s', '%s', '%s', '%s')" % \
                (confirmation.get('user_confirmationID'), confirmation.get('username'), confirmation.get('email'),
                 confirmation.get('Email_key'))
        return self.executeSetQuery(query)

    def setGroup(self, group):
        query = "INSERT INTO `Create_Group` VALUES " \
                "('%s', '%s', '%s', '%s',%s)" % \
                (group.get('group_id'), group.get('user_id'), group.get('group_creator'),
                 group.get('group_name'), 'CURRENT_DATE()')
        return self.executeSetQuery(query)

    def getGroup(self,group_name):
        query = "SELECT * FROM Create_Group WHERE group_name = '%s'" % group_name
        return self.executeGetQuery(query)

    def getAddPermission(self,group_name):
        query = 'SELECT username, student_number FROM user WHERE user_type="Student"' \
                ' and username not in (SELECT username FROM group_permission WHERE group_name = "%s")' % group_name
        return self.executeGetQuery(query)

    def getDeletePermission(self, group_name):
        query = 'SELECT user.username, student_number FROM user join group_permission ' \
                'WHERE user.username = group_permission.username and group_permission.group_name ="%s"' % group_name
        return self.executeGetQuery(query)

    def getUserFromPermission(self,username, group_name):
        query = 'Select * FROM group_permission WHERE username = "%s" and group_name = "%s"' % (username, group_name)
        return self.executeGetQuery(query)

    def deletePermission(self, username, group_name):
        query = 'DELETE FROM group_permission WHERE username = "%s" and group_name = "%s"' % (username, group_name)
        return self.executeSetQuery(query)

    def setGroupPermission(self, permission):
        query = "INSERT INTO `Group_Permission` VALUES " \
                "('%s', '%s', '%s', '%s', '%s')" % \
                (permission['permission_id'], permission['group_id'], permission['username'],
                 permission['permission_creator'], permission['group_name'])
        return self.executeSetQuery(query)

    def setQuestion(self, question):
        query = "INSERT INTO `Question` VALUES " \
                "('%s', '%s', '%s', '%s','%s','%s', '%s', '%s', '%s',%s)" % \
                (question.get('question_id'), question.get('user_id'), question.get('group_name'),
                 question.get('question_creator'), question.get('question_type'), question.get('question_title'),
                 question.get('question_description'),question.get('voting_status'),question.get('question_author'),
                 'CURRENT_DATE()')
        return self.executeSetQuery(query)

    def updateQuestion(self, question_id, group_name):
        query = 'UPDATE question SET voting_status = "Completed" ' \
                'WHERE question_id = "%s" and group_name="%s"' % (question_id, group_name)
        return self.executeSetQuery(query)

    def getInProgressQuestion(self, group_name):
        status ="In-Progress"
        query = "SELECT * FROM Question  WHERE voting_status='%s' AND group_name='%s'" % (status, group_name)
        return self.executeGetQuery(query)
    def getInProgressQuestion1(self, group_name,titulo):
        status ="In-Progress"
        query = "SELECT * FROM Question  WHERE voting_status='%s' AND group_name='%s' AND question_title='%s'" % (status, group_name,titulo)
        return self.executeGetQuery(query)

    def getCompletedQuestions(self, group_name):
        status = "Completed"
        query = "SELECT * FROM Question WHERE voting_status='%s' AND group_name='%s'" % (status, group_name)
        return self.executeGetQuery(query)

    def getQuestion(self, question_title, group_name):
        query = "SELECT * FROM question WHERE question_title='%s' AND group_name='%s'" % (question_title, group_name)
        return self.executeGetQuery(query)

    def getQuestionByID(self, question_id, group_name):
        query = "SELECT * FROM question WHERE question_id='%s' AND group_name='%s'" % (question_id, group_name)
        return self.executeGetQuery(query)

    def setResult(self,result):
        query = "INSERT INTO `Results` VALUES " \
                "('%s', %s,'%s', '%s', '%s','%s','%s', '%s', %s)" % \
                (result.get('result_id'),result.get('question_id'), result.get('question_title'), result.get('question_type'),
                 result.get('group_name'), result.get('count_yes'), result.get('count_no'),
                 result.get('count_abstain'), result.get('total_voters'))
        return self.executeSetQuery(query)

    def getResult(self,question_id):
        query = 'Select Question.group_name, Question.question_creator, Question.question_type, Question.question_title,' \
                ' Question.question_description, Question.voting_status, Question.question_author, Question.date_created, ' \
                'Results.count_yes, Results.count_no, Results.count_abstain, Results.total_voters From Question JOIN Results ' \
                'Where Question.question_id = Results.question_id AND results.question_id= "%s"' % question_id
        return self.executeGetQuery(query)

    def setVoting(self,voting):
        query = "INSERT INTO `Voting` VALUES " \
                "('%s', '%s', '%s', '%s', '%s', '%s')" % \
                (voting.get('voting_id'), voting.get('question_id'), voting.get('group_name'),
                 voting.get('question_title'), voting.get('question_type'), voting.get('voting_choice'))
        return self.executeSetQuery(query)

    def getVote(self, question_title):
        query = "SELECT * FROM Voting WHERE question_title= '%s'" % question_title
        return self.executeGetQuery(query)
    def getUserHasVote(self, vote_id, qeustion):
        query = "SELECT * FROM Voting WHERE voting_id= '%s' AND question_title= '%s'" % (vote_id, qeustion)
        return self.executeGetQuery(query)


    def getVoteCount(self, group_name, question_id, voting_choice):
        query = 'SELECT COUNT(voting_choice) as vote_count FROM Voting ' \
                'WHERE group_name="%s" AND question_id="%s" AND voting_choice="%s"' % (group_name, question_id, voting_choice)
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


def get_user(username, user=userDB , password=passwordDB, host=hostDB, database=databaseDB, port=portDB):
    DB = DBHandler(user=user, password=password, host=host, database=database, port= port)
    DB.connect()
    user = DB.getUser(username)
    output = []
    if user:
        for i in user:
            output.append(i)
    DB.disconnect_get()
    return output

def get_AllUserStudent( user=userDB , password=passwordDB, host=hostDB, database=databaseDB, port=portDB):
    DB = DBHandler(user=user, password=password, host=host, database=database, port= port)
    DB.connect()
    user = DB.getAllUserStudent()
    output = []
    if user:
        for i in user:
            output.append(i)
    DB.disconnect_get()
    return output


def get_user_type(username, user=userDB , password=passwordDB, host=hostDB, database=databaseDB, port=portDB):
    DB = DBHandler(user=user, password=password, host=host, database=database, port= port)
    DB.connect()
    user = DB.getUserType(username)
    output = None
    for i in user:
        output = i
    DB.disconnect_get()
    return output


def set_user(user_query, user=userDB , password=passwordDB, host=hostDB, database=databaseDB, port=portDB):
    DB = DBHandler(user=user, password=password, host=host, database=database, port=port)
    DB.connect()
    # Return True if successful or False otherwise.
    output = DB.setUser(user_query)
    DB.disconnect_set()
    return output

def set_confirmation(confirmation, user=userDB , password=passwordDB, host=hostDB, database=databaseDB, port=portDB):
    DB = DBHandler(user=user, password=password, host=host, database=database, port=port)
    DB.connect()
    # Return True if successful or False otherwise.
    output = DB.setUser(confirmation)
    DB.disconnect_set()
    return output

def set_question(question, user=userDB , password=passwordDB, host=hostDB, database=databaseDB, port=portDB):
    DB = DBHandler(user=user, password=password, host=host, database=database, port=port)
    DB.connect()
    # Return True if successful or False otherwise.
    output = DB.setQuestion(question)
    DB.disconnect_set()
    return output

def set_userTable(query, user=userDB , password=passwordDB, host=hostDB, database=databaseDB, port=portDB):
    DB = DBHandler(user=user, password=password, host=host, database=database, port=port)
    DB.connect()
    # Return True if successful or False otherwise.
    output = DB.set_Table(query)
    DB.disconnect_set()
    return output

def get_CompletedQuestion(group_name, user=userDB , password=passwordDB, host=hostDB, database=databaseDB, port=portDB):
    DB = DBHandler(user=user, password=password, host=host, database=database, port=port)
    DB.connect()
    user = DB.getCompletedQuestions(group_name)
    output = []
    for i in user:
        output.append(i)
    DB.disconnect_get()
    return output

def get_Question(question_title, group_name, user=userDB , password=passwordDB, host=hostDB, database=databaseDB, port=portDB):
    DB = DBHandler(user=user, password=password, host=host, database=database, port=port)
    DB.connect()
    user = DB.getQuestion(question_title, group_name)
    output = None
    for i in user:
        output = i
    DB.disconnect_get()
    return output

def get_QuestionByID(question_id, group_name, user=userDB , password=passwordDB, host=hostDB, database=databaseDB, port=portDB):
    DB = DBHandler(user=user, password=password, host=host, database=database, port=port)
    DB.connect()
    user = DB.getQuestionByID(question_id, group_name)
    output = None
    for i in user:
        output = i
    DB.disconnect_get()
    return output

def get_Result(question_id, user=userDB , password=passwordDB, host=hostDB, database=databaseDB, port=portDB):
    DB = DBHandler(user=user, password=password, host=host, database=database, port=port)
    DB.connect()
    user = DB.getResult(question_id)
    output = None
    for i in user:
        output = i
    DB.disconnect_get()
    return output

def get_user_idx(user=userDB , password=passwordDB, host=hostDB, database=databaseDB, port=portDB):
    DB = DBHandler(user=user, password=password, host=host, database=database, port=port)
    DB.connect()
    id = DB.get_user_id()
    output = []
    for i in id:
        output.append(i)
    DB.disconnect_get()
    return output

def get_question_idx(user=userDB , password=passwordDB, host=hostDB, database=databaseDB, port=portDB):
    DB = DBHandler(user=user, password=password, host=host, database=database, port=port)
    DB.connect()
    id = DB.get_question_id()

    output = []
    for i in id:
        output.append(i)
    DB.disconnect_get()
    return output


def get_in_progress_question(group_name, user=userDB , password=passwordDB, host=hostDB, database=databaseDB, port=portDB):
    DB = DBHandler(user=user, password=password, host=host, database=database, port=port)
    DB.connect()
    quesiton = DB.getInProgressQuestion(group_name)
    output = []
    for i in quesiton:
        output.append(i)
    DB.disconnect_get()
    return output
def get_in_progress_question1(group_name,titulo, user=userDB , password=passwordDB, host=hostDB, database=databaseDB, port=portDB):
    DB = DBHandler(user=user, password=password, host=host, database=database, port=port)
    DB.connect()
    quesiton = DB.getInProgressQuestion1(group_name,titulo)
    output = None
    for i in quesiton:
        output = i
    DB.disconnect_get()
    return output

def set_groupPermission(permission, user=userDB , password=passwordDB, host=hostDB, database=databaseDB, port=portDB):
    DB = DBHandler(user=user, password=password, host=host, database=database, port=port)
    DB.connect()
    # Return True if successful or False otherwise.
    output = DB.setGroupPermission(permission)
    DB.disconnect_set()
    return output

def get_addPermission(group_name, user=userDB , password=passwordDB, host=hostDB, database=databaseDB, port=portDB):
    DB = DBHandler(user=user, password=password, host=host, database=database, port=port)
    DB.connect()
    users = DB.getAddPermission(group_name)
    output = []
    for user in users:
        output.append(user)
    DB.disconnect_get()
    return output

def get_deletePermission(group_name, user=userDB , password=passwordDB, host=hostDB, database=databaseDB, port=portDB):
    DB = DBHandler(user=user, password=password, host=host, database=database, port=port)
    DB.connect()
    users = DB.getDeletePermission(group_name)
    output = []
    for user in users:
        output.append(user)
    DB.disconnect_get()
    return output

def delete_Permission(username, group_name, user=userDB , password=passwordDB, host=hostDB, database=databaseDB, port=portDB):
    DB = DBHandler(user=user, password=password, host=host, database=database, port=port)
    DB.connect()
    # Return True if successful or False otherwise.
    output = DB.deletePermission(username, group_name)
    DB.disconnect_set()
    return output

def has_permission(username, group_name, user=userDB , password=passwordDB, host=hostDB, database=databaseDB, port=portDB):
    DB = DBHandler(user=user, password=password, host=host, database=database, port=port)
    DB.connect()
    users = DB.getUserFromPermission(username,group_name)
    output = []
    for user in users:
        output.append(user)
    DB.disconnect_get()
    return output

def update_question(question_id, group_name, user=userDB , password=passwordDB, host=hostDB, database=databaseDB, port=portDB):
    DB = DBHandler(user=user, password=password, host=host, database=database, port=port)
    DB.connect()
    # Return True if successful or False otherwise.
    output = DB.updateQuestion(question_id, group_name)
    DB.disconnect_set()
    return output

def get_voteCount(group_name, question_id, voting_choice, user=userDB , password=passwordDB, host=hostDB, database=databaseDB, port=portDB):
    DB = DBHandler(user=user, password=password, host=host, database=database, port=port)
    DB.connect()
    quesiton = DB.getVoteCount(group_name, question_id, voting_choice)
    output = None
    for i in quesiton:
        output = i
    DB.disconnect_get()
    return output

def set_result(result, user=userDB , password=passwordDB, host=hostDB, database=databaseDB, port=portDB):
    DB = DBHandler(user=user, password=password, host=host, database=database, port=port)
    DB.connect()
    # Return True if successful or False otherwise.
    output = DB.setResult(result)
    DB.disconnect_set()
    return output

def set_vote(vote, user=userDB , password=passwordDB, host=hostDB, database=databaseDB, port=portDB):
    DB = DBHandler(user=user, password=password, host=host, database=database, port=port)
    DB.connect()
    output = DB.setVoting(vote)
    DB.disconnect_set()
    return output

def get_user_has_vote(vote_id, question, user=userDB , password=passwordDB, host=hostDB, database=databaseDB, port=portDB):
    DB = DBHandler(user=user, password=password, host=host, database=database, port=port)
    DB.connect()
    quesiton = DB.getUserHasVote(vote_id, question)
    output = None
    for i in quesiton:
        output = i
    DB.disconnect_get()
    return output

def set_Table(table, user=userDB , password=passwordDB, host=hostDB, database=databaseDB, port=portDB):
    DB = DBHandler(user=user, password=password, host=host, database=database, port=port)
    DB.connect()
    output = DB.setTable(table)
    DB.disconnect_set()
    return output