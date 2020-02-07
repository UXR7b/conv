import vk,random,math,os,time
tokenlink = input("TOKEN LINK:")
token1 = tokenlink.rsplit("access_token=")
token2 = token1[1].rsplit("&expires_in")
token = token2[0]
print(token)
sess=vk.Session(access_token=token)
api=vk.API(sess,v='5.92',lang='ru')
id = input("ID:")
memberslist = str(api.messages.getConversationMembers(peer_id=2000000000+int(id)))
members1=memberslist.rsplit("'profiles'")
members2=members1[0]
members3=members2.rsplit("'member_id': ")
memberslen=len(members3)
members=[]

for n in range(1,memberslen):
	members4=members3[n].rsplit(',')
	members.append(members4[0])
	

message = ''
ss=0
memberslen2=len(members)
for s in range(0,int(memberslen2/2)):
	members5=int(members[s])
	if members5 < 0:
		members.remove(str(members5))
		
		
memberslen2=len(members)
for n in range(ss,memberslen2):
	message += '[id'+members[n]+'| ] '

api.messages.send(random_id=int(time.time()),peer_id=2000000000+int(id),message=message)