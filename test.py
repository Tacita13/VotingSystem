from passwordhelper import PasswordHelper
from register import validateRegister
from login import validateLogin
from dbhandler import DBHandler, set_user, set_groupPermission, set_question, set_result, delete_Permission
from random import randint

import hashlib

PH = PasswordHelper()
passw =[ "1test01", "2test01", "3test01", "4test01", "5test01"]
users  =["1test01", "2test01", "3test01", "4test01", "5test01"]
ids = [ "2", "3", "4", "5", "6"]
questions  =["Question1_test01", "Question2_test01", "Question3test01", "Question4_test01", "Question5test01"]
group_name = "prueba01"

print("Identifier: Level1_Item02")
print("Type: Unit Test (Black Box)")
for i in range(len(users)):
    user = {'user_id': ids[i], 'username': i, 'name': users[i],
            'last_name': users[i], 'user_type': 'Student', 'password': PH.get_hash(passw[i]),
            'email': users[i], 'student_number': '801-15-8943', 'date_created': 'CURRENT_DATE()'}
    print("Input: %s" % user)
    output = set_user(user)
    print("Output: %s" % output)
    assert output == True

print("Identifier: Level1_Item03")
print("Type: Unit Test (Black Box)")
for i in range(len(users)):
    permission = {'permission_id': ids[i], 'group_id': 1, 'username': users[i],
                  'permission_creator': "admin", 'group_name': group_name}
    print("Input: %s" % user)
    set_groupPermission(permission)
    print("Output: %s" % output)
    assert output == True

print("Identifier: Level1_Item03")
print("Type: Unit Test (Black Box)")
for i in range(len(users)):
    current_question = {'question_id': ids[i], 'user_id': ids[i], 'group_name': group_name,
                        'question_creator': "admin", 'question_type': "Enmienda",
                        'question_title': questions[i],
                        'question_description': questions[i], 'voting_status': "In-progress",
                        'question_author': "admin", "date_created": ""}
    print("Input: %s" % user)
    set_question(current_question)
    print("Output: %s" % output)
    assert output == True

print("Identifier: Level1_Item04")
print("Type: Unit Test (Black Box)")
for i in range(3):
    result = {'result_id': ids[i], 'question_id': [i], 'question_title': questions[i],
              'question_type': "Enmienda", 'group_name': group_name, 'count_yes': 3,
              'count_no': 1, 'count_abstain': 0, 'total_voters': 4}
    print("Input: %s" % user)
    set_result(result)
    print("Output: %s" % output)
    assert output == True

print("Identifier: Level1_Item05")
print("Type: Unit Test (Black Box)")
for i in range(3):
    print("Input: %s, %s" % (users[i], group_name))
    output = delete_Permission(users[i], group_name)
    print("Output: %s" % output)
    assert output == True
