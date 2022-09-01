print("""Welcome 

     The 4th Industrial Revolution 

     - Menu -
     ........
     
     pick one. 
     
     1)Question & Answer 1
     2)Question & Answer 2
     3)Question & Answer 3
     4)Question & Answer 4 
     5)Question & Answer 5 
     6)Question & Answer 6
     7)Question & Answer 7 
     """)
answer = "empty"
userchoice = input()

while(answer == "empty"):
  answer = "chosen"
  
  if(userchoice == "1"):
    print("""Who do you think went to school before that? 
    Before public school was really made a thing only wealthy people had the money and time to dedicate their attention towards any sort of education.
    """)
  elif(userchoice == "2"):
    print("""Why do you think the laws changed?
     
    I think they saw the benefit of teaching people authority and prepared kids to enter the workforce. They probably saw more skilled workers enter the workforce further driving the already growing economy.""")
  elif(userchoice == "3"):
    print("""What effects do you think have?
     
   it taught a great number of people important skills and subjects applicable in the real world. It most likely impacted the economy the greatest and it's probably one of the reasons innovation also exponentially grew.""")
  elif(userchoice == "4"):
    print("""What are your thoughts in response to the video? 
    
    I think some of the things that the video sjpwed are pretty cool. For example, its impact on th emedical field.It's great because it's less susceptible to human mistakes and it learns new things faster than humans.""")
  elif(userchoice == "5"):
    print("""How might these new technologies affect education? 
    
    I guess we're incorporating towards a more technological based style of educatoin, but I highly doubt that technology would ever go as far as replacing teachers, but I think they will assist teachers a lot more. I also see this making school even more challanging as we teach more complex material.""")
  elif(userchoice == "6"):
    print("""Society and culture helps shape the development of new technologies, and new technologies, in turn, help shape the development of our society and culture. Some of these only affects minor aspects, others may radically change nearly every part of our culture. Historicallly, you should be aware of the Industrial Revolution, but have you heard of the 4th industrial revolution?
    
    The 4th Revolution is defined by how ingrained technology is becoming to human life. One of the examples that were mentioned in the video was pretty interesting: it took 75 years to adapt the telegram into human life, it took 2 years to adapt instagram, and it took 1 month to adapt Pokemon Go into our lives. Also interesting point they boguht up that companies are turning into tech companies and are taking up more data from their customers than before.""")
  else:
      print("INVALID, pls try again")
      answer = "empty"
