from num2words import num2words
a = "12/05/2022"
c = "52,5"
b = (a.replace(",","."))
num_ptbr = num2words(c.replace(",","."), lang='pt-br')
print(a[:2])

q = 2
c = 4



# endobra = dados_lidos[0][1]
#         bairroobra = dados_lidos[0][2]
#         numobra = dados_lidos[0][3]
#         cidadeobra = dados_lidos[0][4]
#         loteobra = dados_lidos[0][5]
#         quadraobra = dados_lidos[0][6]
#         quarteiraoobra = dados_lidos[0][7]
#         tipoobra = dados_lidos[0][8]
#         areaobra = dados_lidos[0][9]
#         artobra = dados_lidos[0][10]
#         valorparcobra = dados_lidos[0][11]
#         quantparcobra = dados_lidos[0][12]
#         datacontratoobra = dados_lidos[0][13]
#         valorvisitaobra = dados_lidos[0][14]