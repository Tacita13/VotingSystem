from passwordhelper import PasswordHelper
from register import validateRegister
from login import validateLogin
from dbhandler import DBHandler, set_user, set_groupPermission, set_question, set_result, delete_Permission, get_user_type, get_in_progress_question1, get_in_progress_question, get_CompletedQuestion
from random import randint

import hashlib


PH = PasswordHelper()
passw =[ "1test01", "2test01", "3test01", "4test01", "5test01"]
users  =["1test01", "2test01", "3test01", "4test01", "5test01"]
ids = [ "2", "2", "3", "4", "5", "6"]
questions  =["Question1_test01","Question1_test01", "Question2_test01", "Question3test01", "Question4_test01", "Question5test01"]
group_name = "prueba01"

print("Identifier: Level1_Item02")
print("Type: Unit Test (Black Box)")
print("set_user")
for i in range(len(users)):
    user = {'user_id': ids[i], 'username': users[i], 'name': users[i],
            'last_name': users[i], 'user_type': 'Student', 'password': PH.get_hash(passw[i]),
            'email': users[i], 'student_number': '801-15-8943', 'date_created': 'CURRENT_DATE()'}

    output = set_user(user)

    if i < 2:
        print("Input: %s" % user)
        print("Output: %s" % output)
    if i == 1:
        assert output == False
    else:
        # assert output == True
        pass

print("Identifier: Level1_Item03")
print("Type: Unit Test (Black Box)")
print("set_groupPermission")
for i in range(len(users)):
    permission = {'permission_id': ids[i], 'group_id': 1, 'username': users[i],
                  'permission_creator': "admin", 'group_name': group_name}

    output = set_groupPermission(permission)
    if i < 2:
        print("Input: %s" % permission)
        print("Output: %s" % output)
    if i == 1:
        assert output == False
    else:
        assert output == True

print("Identifier: Level1_Item04")
print("Type: Unit Test (Black Box)")
print("set_question")
for i in range(len(users)):
    current_question = {'question_id': ids[i], 'user_id': ids[i], 'group_name': group_name,
                        'question_creator': "admin", 'question_type': "Enmienda",
                        'question_title': questions[i],
                        'question_description': questions[i], 'voting_status': "In-progress",
                        'question_author': "admin", "date_created": ""}

    output = set_question(current_question)
    if i < 2:
        print("Input: %s" % current_question)
        print("Output: %s" % output)
    if i == 1:
        assert output == False
    else:
        assert output == True

print("Identifier: Level1_Item05")
print("Type: Unit Test (Black Box)")
print("set_result")
for i in range(3):
    result = {'result_id': ids[i], 'question_id': ids[i], 'question_title': questions[i],
              'question_type': "Enmienda", 'group_name': group_name, 'count_yes': 3,
              'count_no': 1, 'count_abstain': 0, 'total_voters': 4}
    output = set_result(result)
    if i < 2:
        print("Input: %s" % result)
        print("Output: %s" % output)
    if i == 1:
        assert output == False
    else:
        assert output == True

print("Identifier: Level1_Item06")
print("Type: Unit Test (Black Box)")
print("delete_Permission")
usersPerms =["1test01", "Test" "2test01", "3test01", "4test01"]
for i in range(3):
    output = delete_Permission(usersPerms[i], group_name)
    if i < 2:
        print("Input: %s, %s" % (usersPerms[i], group_name))
        print("Output: %s" % output)

    assert output == True

for i in range(len(users)):
    type = get_user_type(users[i])
    print("Type of user %s: %s" ) % (i,type)

get_in_progress_question = get_in_progress_question(group_name)
print ("That are all of question in progress: $s") % get_in_progress_question

get_in_progress_question = get_in_progress_question("prueba02")
print ("That give an error: $s") % get_in_progress_question

get_CompletedQuestion = get_CompletedQuestion(group_name)
print ("That are all of question completed: $s") % get_CompletedQuestion

get_CompletedQuestion = get_CompletedQuestion("prueba02")
print ("That give an error: $s") % get_CompletedQuestion

