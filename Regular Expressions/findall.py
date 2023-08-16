import re

text=f"""
Email me at user123@example.com if you have any questions, 
Don't forget to check the weather forecast at www.weatherforecast.com.
"""
#use of \w+ and \S+
print(re.findall("\w+",text))
#output
#['Email', 'me', 'at', 'user123', 'example', 'com', 'if', 'you', 'have', 'any', 'questions', 
#'Don', 't', 'forget', 'to', 'check', 'the', 'weather', 'forecast', 'at', 'www', 'weatherforecast', 'com']

print(re.findall("\S+",text))
#output
#['Email', 'me', 'at', 'user123@example.com', 'if', 'you', 'have', 'any', 'questions,', "Don't", 'forget',
# 'to', 'check', 'the', 'weather', 'forecast', 'at', 'www.weatherforecast.com.']

#use of \b
pattern=r"\b\w+\b"
print(re.findall(pattern,text))
#output
#['Email', 'me', 'at', 'user123', 'example', 'com', 'if', 'you', 'have', 'any', 'questions', 'Don', 't', 
# 'forget', 'to', 'check', 'the', 'weather', 'forecast', 'at', 'www', 'weatherforecast', 'com']

pattern1=r"\b\S+\b"
print(re.findall(pattern1,text))
#output
#['Email', 'me', 'at', 'user123@example.com', 'if', 'you', 'have', 'any', 'questions', "Don't", '
# forget', 'to', 'check', 'the', 'weather', 'forecast', 'at', 'www.weatherforecast.com']

pattern2=r"\b\S+\.+\w+\b" #exact use of \b 
print(re.findall(pattern2,text))
#output
# ['user123@example.com', 'www.weatherforecast.com']

#------------------------------------------------------------------------------------
text1="banana pancake is my favorite"
pattern3=r"\Ban\B"
print(re.findall(pattern3,text1))
#output 
#['an', 'an', 'an']
pattern4=r"\w+\Ban\B\w+"
print(re.findall(pattern4,text1))
#output
#['banana', 'pancake']

#----------------------------------------------------------------------------------

                #################### use of $ and ? #######################

text2 = """
sample@gmail.com
dev.solutions@gmail.com
prod.sample@gmail.com
site1.production@hotmail.com.au
"""

pattern5 = r'@\w+\.(com|com\.au)$'
print(re.findall(pattern5, text2))

#-----------------------------------------------------------------------------
############################ use of {n} #############

text3=f"""hello, kerberos is running at 172.167.23.54 and FreeIPA is running on 192.168.17.4 
and nginx is runnig on 10.10.1.4
"""

pattern6=r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
print(re.findall(pattern6,text3))
#output
# ['172.167.23.54', '192.168.17.4', '10.10.1.4']

#--------------------------------------------------------

            ################################ use of IGNORECASE #############################

text4="""Hello, 
Today we will learn python2 and Python3. after this we will learn python selenium
Thanks,
"""
pattern7=r"python\d"
print(re.findall(pattern7,text4))
print(re.findall(pattern7,text4,re.IGNORECASE))

#-------------------------------------------------------------------
          ############################### use of ^ symbol ##############################
 
text5=f"""My nginx server ip= 192.168.10.23
My nagios server ip is 172.168.23.7
my kerberos server ip is 192.168.3.17
my FreeIPA server ip is 192.168.1.5
"""
pattern8=r"^My"
print(re.findall(pattern8,text5,re.MULTILINE|re.IGNORECASE))
#output
#['My', 'My', 'my', 'my']

#------------------------------------------------------------------------

        ########################## use of re.compile() function ########################

print(type(pattern8))
pattern9=re.compile("^My",re.MULTILINE|re.IGNORECASE)
print(type(pattern9))
print(pattern9.findall(text5))
#output
#<class 'str'>
#<class 're.Pattern'>
#['My', 'My', 'my', 'my']

#-------------------------------------------------------------------------------

############################ use of re.search() function ##########################

pattern10=re.compile(r"\d{1,3}\.\d{1,3}\.\d{1,3}")
print(pattern10.findall(text5))
print(pattern10.search(text5))
print(pattern10.search(text5).group()) #filter out the content from match section in the 
#object created by search function

#output
#['192.168.10', '172.168.23', '192.168.3', '192.168.1']
#<re.Match object; span=(20, 30), match='192.168.10'>
#192.168.10

#------------------------------------------------------------------------

################################### use of re.match() ##########################
#   text5="""My nginx server ip= 192.168.10.23
#   My nagios server ip is 172.168.23.7
#   my kerberos server ip is 192.168.3.17
#   my FreeIPA server ip is 192.168.1.5
#   """

text6=f"""172.168.12.212 is the main server
My nginx server ip= 192.168.10.23
My nagios server ip is 172.168.23.7
my kerberos server ip is 192.168.3.17
my FreeIPA server ip is 192.168.1.5
"""
pattern11=r"\d{3}\.\d{3}\.\d{1,3}\.\d{1,3}"
print(re.findall(pattern11,text5))
print(re.search(pattern11,text5).group())
print(re.match(pattern11,text5))
print(re.match(pattern11,text6).group())
#output
#['192.168.10.23', '172.168.23.7', '192.168.3.17', '192.168.1.5']
#192.168.10.23
#None
#172.168.12.212


#---------------------------------------------------------------------

##################################### use of re.split() ################################

#   text5="""My nginx server ip= 192.168.10.23
#   My nagios server ip is 172.168.23.7
#   my kerberos server ip is 192.168.3.17
#   my FreeIPA server ip is 192.168.1.5
#   """

#pattern11=r"\d{3}\.\d{3}\.\d{1,3}\.\d{1,3}"
print(re.split(pattern11,text6))
#output
#['', ' is the main server\nMy nginx server ip= ', '\nMy nagios server ip is ', '\nmy kerberos server ip is ', '\nmy FreeIPA server ip is ', '\n']

##############################################################################################

                ######################## use of re.sub() #######################

#   text5="""My nginx server ip= 192.168.10.23
#   My nagios server ip is 172.168.23.7
#   my kerberos server ip is 192.168.3.17
#   my FreeIPA server ip is 192.168.1.5
#   """
#pattern11=r"\d{3}\.\d{3}\.\d{1,3}\.\d{1,3}"

print(re.sub(pattern11,"confidential",text5))

###########################################################################################3

                        ############################# task #########################
task=f"""
We have example of email address finder
abdealidodia242@gmail.com
abdeali@gmail.com
xyz.co
ABDEALi@gmail.com
ABd@yahoo.com
support@hotmail.com.au
"""
email_pattern=r"\w+\@\w+\.\w+\.?\w\w"
print(re.findall(email_pattern,task))