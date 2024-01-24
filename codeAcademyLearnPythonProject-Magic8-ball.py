name= "Vanitas"
question= "Are you a member of the blue moon clan?"
answer=""
import random
call= random.randint(1,12)
#print(call)
if call==1:
  answer="Yes - definitely"
elif call==2:
  answer="It is decidedly so"
elif call==3:
  answer="Without a doubt"
elif call==4:
  answer="Reply hazy, try again"
elif call==5:
  answer="Ask again later"
elif call==6:
  answer="Better not tell you now"
elif call==7:
  answer="My sources say no"
elif call==8:
  answer="Outlook not so good"
elif call==9:
  answer="Very doubtful"
elif call==10:
  answer="Are you serious?"
elif call==11:
  answer="That is highly confidential"
elif call==12:
  answer="Fifth amendment"
else:
  answer="Error"
if question=="":
  print("Bro what is your question.")
elif name=="":
  print("Question:"+question)
  print("Magic 8-Ball's answer: "+answer)
else:
  print(name+" asks: "+question)
  print("Magic 8-Ball's answer: "+answer)