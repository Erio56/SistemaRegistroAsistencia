import datetime 


def str_to_time(input:str)->datetime:
   horas = 0
   minutos = 0
   if input != "":
      horas = int(input[0:2])
      minutos = int(input[3:5])
      return datetime.time(horas,minutos, 0)
   else:
      return datetime.time(0,0,0)