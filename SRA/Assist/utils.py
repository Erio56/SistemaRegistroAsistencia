import datetime 


def str_to_time(input:str)->datetime:
   horas = 0
   minutos = 0
   if input != "":
      if input[i][0:1] != "":
         horas = int(input[0:1])
      if input[i][3:4] != "":
            minutos = int(input[3:4])
      return datetime.time(horas,minutos, 0)
   else:
      return datetime.time(0,0,0)