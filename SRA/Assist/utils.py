import datetime 
from django.utils import timezone

def str_to_time(input:str)->datetime:
   horas = 0
   minutos = 0
   if input != "":
      horas = int(input[0:2])
      minutos = int(input[3:5])
      return datetime.time(horas,minutos, 0)
   else:
      return datetime.time(0,0,0)

      
def getDay(input):
   now = datetime.datetime.now()
   day = now.strftime("%A")
   match day:
      case 'Monday':
            return input.lunes
      case 'Tuesday':
            return input.martes
      case 'Wednesday':
            return input.miercoles
      case 'Thursday':
            return input.jueves
      case 'Friday':
            return input.viernes
      case 'Saturday':
            return input.sabado
      case 'Sunday':
            return input.domingo
      case _:
            return None
   
def needsToAssist(input:datetime, input2:datetime)->bool:
   now = timezone.now()
   if input == datetime.time(0,0,0) and input2 == datetime.time(0,0,0):
      return False
   else:
      if input >= now and input2 <= now:
         return True