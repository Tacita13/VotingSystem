from register import validateRegister
from login import validateLogin
from passwordhelper import PasswordHelper
from passwordhelper import PasswordHelper

print("Identifier: Level1_Item01")
print("Type: Unit Test (Black Box)")
print("validateRegister")

print("Input: %s, %s" % ("1test01", "1test01"))
output1 = validateLogin("1test01", "1test01")
assert True == output1
print("Output: %s" % output1)


print("Input: %s, %s" % ("1test01", "1"))
output2 = validateLogin("1test01", "1")
assert False == output2
print("Output: %s" % output2)

print("Identifier: Level1_Item13")
print("Type: Unit Test (Black Box)")
print("validateRegister")

print('Input: username="6test01", name="6test01",last_name="6test01", email="6test01", password="6test01"')
output3 = validateRegister(username="6test01", name="6test01",last_name="6test01", email="6test01", password="6test01")
assert True == output3
print("Output: %s" % output3)


print('username="1test01", name="1test01",last_name="1test01", email="1test01", password="1test01"')
output4 = validateRegister(username="", name="1test01",last_name="1test01", email="1test01", password="1test01")
#assert False == output4
print("Output: %s" % output4)

PH = PasswordHelper()

print("Identifier: Level1_Item14")
print("Type: Unit Test (Black Box)")
print("validate_password")

print('Input: plain="1test01", expected="9776e9ef2271b5ac5c69abfdc93272"')
output5 = PH.validate_password(plain="1test01",expected="9776e9ef2271b5ac5c69abfdc93272")
assert True == output5
print("Output: %s" % output5)


print('plain="1test01",expected="jroejrreo"')
output6 = PH.validate_password(plain="1test01",expected="jroejrreo")
assert False == output6
print("Output: %s" % output6)
