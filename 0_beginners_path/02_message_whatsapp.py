import pywhatkit
try:
  pywhatkit.sendwhatmsg("+595986305548", 
                        "Feliz cumpleaños señor X.", 
                        19, 31)
  print("Successfully Sent!")
  
except:
  print("An Unexpected Error!")
  
