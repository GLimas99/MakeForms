import datetime
import time
from playsound import playsound

def despertar(dia, mes, ano, hora, minuto, agora):
    if agora.day == dia and agora.month == mes and agora.year == ano and agora.hour == hora and agora.minute == minuto:
        return True
    return False

print("DESPERTADOR")

data = input("Quando vence o AVCB? (dd/mm/aaaa): ")

dora = input("Qual o horário para despertar? (hh:mm): ")

dia = int(data.split('/')[0])
mes = int(data.split('/')[1])
ano = int(data.split('/')[2])

hora = int(dora.split(':')[0])
minuto = int(dora.split(':')[1])

agora = datetime.datetime.now()

# resultado = despertar(dia, mes, ano, hora, minuto, agora)
#
# print("Está na hora? :" + str(resultado))

while True:
    agora = datetime.datetime.now()
    print(agora)

    if despertar(dia, mes, ano, hora, minuto, agora):
        playsound('./videoplayback.mp3')

    time.sleep(60)