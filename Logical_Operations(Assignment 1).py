'''
In second year computer engineering class, group A students play cricket, group B students play badminton, 
and group C students play football. You are tasked with writing a Python program using functions to compute the following:

a) List of students who play both cricket and badminton
b) List of students who play either cricket or badminton but not both
c) Number of students who play neither cricket nor badminton
d) Number of students who play cricket and football but not badminton
(Note : While realizing the group duplicate entries should be avoided, Do not use SET built-in functions)
'''

cricket = []
badminton = []
football = []

cric = int(input("Enter the number of students who play cricket :"))
for i in range(cric):
  a = input("Enter who plays cricket :")
  cricket.append(a)

badm = int(input("Enter the number of students who play badminton :"))
for i in range(badm):
  a = input("Enter who plays badminton :")
  badminton.append(a)

foot = int(input("Enter the number of students who play football :"))
for i in range(foot):
  a = input("Enter who plays football :")
  football.append(a)

def cric_badm():
  Cric_Badm = []
  for i in cricket:
    if i in badminton:
      Cric_Badm.append(i)
  print("Player playing both cricket and badminton\n", Cric_Badm)

def cricorbadm():
 
  CricorBadm = []

  for i in cricket:
    if i not in badminton:
      CricorBadm.append(i)
  for i in badminton:
    if i not in cricket:
      CricorBadm.append(i)

  print("Player playing either cricket or badminton but not both are\n",CricorBadm)

def norCricorBadm():
  xyz = []
  for i in football:
    if i not in cricket and i not in badminton:
      xyz.append(i)
  print("Player who play only football\n", len(xyz))

def cric_foot():
  Cric_foot = []
  for i in cricket:
    if i not in badminton and i not in football:
      Cric_foot.append(i)
  for i in football:
    if i not in badminton and i not in cricket:
      Cric_foot.append(i)
  print("Player who play cricket or football but not badminton\n", len(Cric_foot))

cric_badm()
cricorbadm()
norCricorBadm()
cric_foot()
