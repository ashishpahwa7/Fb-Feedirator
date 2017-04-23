from FbFeed import NewsFeed
import getpass

username = raw_input('Enter your email id registered with facebook : ')
password = getpass.getpass(prompt='Enter your Password : ',stream=None)
print('Creating new session on Firefox..')
fb = NewsFeed(username,password)
print('Logging into your facebook account')
fb.login()

#Add people to group
print('Add people to Feed Group')

count = int(raw_input('How many people would you like to add ?: '))
for i in range(count):
	name = raw_input()
	fb.add(name)

print('Leave me running on your system , I will notify you whenever these people perform any public activity')
fb.read()








