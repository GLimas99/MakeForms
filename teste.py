import sys
from novo.menu import *
from novo.obra import *
from novo.client import *
from novo.make_doc import *
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import QtWidgets
import sqlite3
from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from datetime import date
from num2words import num2words
from pathlib import Path
# create document
document = Document()

sections = document.sections
for section in sections:
    section.top_margin = Cm(1)
    section.bottom_margin = Cm(1)
    section.left_margin = Cm(3)
    section.right_margin = Cm(1)

section = document.sections[0]


header = document.sections[0].header
logo = header.paragraphs[0]
logo_run = logo.add_run()
logo_run.add_picture("images/logo.png", width=Cm(1.48), height=Cm(1.48))

paragraph = document.add_paragraph('Ao'
                                   '\nExcelentíssimo Senhor Prefeito Municipal,')
paragraph.style = document.styles.add_style('style', WD_STYLE_TYPE.PARAGRAPH)
font = paragraph.style.font
font.size = Pt(10)
font.name = 'Arial'
paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY

paragraph = document.add_paragraph('                    Venho respeitosamente à presença de Vossa Excelência requerer, por meio do representante legal que em conjunto este subscreve, que se digne em providenciar por meio do órgão competente o que segue:')
font = paragraph.style.font
font.size = Pt(10)
font.name = 'Arial'
paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY

paragraph = document.add_paragraph('(   ) PRED - Desdobro de lote 	(   ) PRED - Regularização de edificação')
font = paragraph.style.font
font.size = Pt(10)
font.name = 'Arial'
paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY

# add grid table

table = document.add_table(rows=3, cols=1, style='Table Grid')
table.left_margin = Cm(30.4)
row = table.rows[0]



tabela = 'Dados do requerente (titular do lote ou da edificação)'
tabela_formatada = row.cells[0].paragraphs[0].add_run(tabela)
tabela_formatada.font.name = 'Arial'
tabela_formatada.font.size = Pt(10)
tabela_formatada.bold = True

tabela = '\nRazão social/nome: ______________________________________________' \
             '\nCNPJ/CPF nº: ___________________________________________________' \
             '\nE-mail*: ________________________________________________________' \
             '\nTelefone para contato: ____________________________________________'
tabela_formatada = row.cells[0].paragraphs[0].add_run(tabela)
tabela_formatada.font.name = 'Arial'
tabela_formatada.font.size = Pt(10)

tabela = '\n*as notificações sobre este processo serão enviadas por e-mail. Favor atentar-se a isso no momento do preenchimento.'
tabela_formatada = row.cells[0].paragraphs[0].add_run(tabela)
tabela_formatada.font.name = 'Arial'
tabela_formatada.font.size = Pt(10)
tabela_formatada.bold = True

row = table.rows[1]

tabela = 'Dados do imóvel:'
tabela_formatada = row.cells[0].paragraphs[0].add_run(tabela)
tabela_formatada.font.name = 'Arial'
tabela_formatada.font.size = Pt(10)
tabela_formatada.bold = True

tabela = '\nLote/Gleba/Quinhão nº: ___________________________________' \
         '\nQuadra: ________________________________________________' \
         '\nLoteamento: ____________________________________________' \
         '\nInscrição Imobiliária: _______________________________________' \
         '\nEndereço:  ______________________________________________' \
         '\nCEP: _______________ - _______'
tabela_formatada = row.cells[0].paragraphs[0].add_run(tabela)
tabela_formatada.font.name = 'Arial'
tabela_formatada.font.size = Pt(10)

row = table.rows[2]

tabela = 'Dados do Responsável Técnico pelo projeto'
tabela_formatada = row.cells[0].paragraphs[0].add_run(tabela)
tabela_formatada.font.name = 'Arial'
tabela_formatada.font.size = Pt(10)
tabela_formatada.bold = True

tabela = '\nNome completo: ___________________________________________' \
         '\nRegistro profissional: _______________ Órgão:__________________' \
         '\nEstá registrado no CPHO¹?  (   ) sim     (   ) não' \
         '\nNº da Inscrição Mobiliária: ___________________________________' \
         '\nE-mail²: __________________________________________________' \
         '\nTelefone para contato: ______________________________________' \
         '\n¹CPHO - Cadastro de Profissionais Habilitados junto aos órgãos da Prefeitura Municipal de Hortolândia.'
tabela_formatada = row.cells[0].paragraphs[0].add_run(tabela)
tabela_formatada.font.name = 'Arial'
tabela_formatada.font.size = Pt(10)

tabela = '\n²as notificações sobre este processo serão enviadas por e-mail. Favor atentar-se a isso no momento do preenchimento.'
tabela_formatada = row.cells[0].paragraphs[0].add_run(tabela)
tabela_formatada.font.name = 'Arial'
tabela_formatada.font.size = Pt(10)
tabela_formatada.bold = True

paragraph = document.add_paragraph('\n(  ) Declaro que os documentos, declarações e demais elementos submetidos na instrução deste requerimento são verdadeiros e que tenho ciência de que a falsidade de qualquer informação prestada acarreta automaticamente em crime de falsidade ideológica na forma do art. 299 do Código Penal Brasileiro.')
font = paragraph.style.font
font.size = Pt(10)
font.name = 'Arial'
paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
paragraph.paragraph_format.line_spacing = Cm(0)
paragraph.paragraph_format.space_after = Cm(0)

paragraph = document.add_paragraph('(  ) Declaro ter ciência de que, caso meu pedido não seja instruído nos termos que determina a legislação vigente, deverei regularizá-lo no prazo de 30 (trinta) dias corridos, sob pena de arquivamento e indeferimento deste processo.')
font = paragraph.style.font
font.size = Pt(10)
font.name = 'Arial'
paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
paragraph.paragraph_format.line_spacing = Cm(0)
paragraph.paragraph_format.space_after = Cm(0)

paragraph = document.add_paragraph('(  ) Declaro ter ciência do prazo de 180 (cento e oitenta) dias corridos, contados da entrega da planta aprovada, para o registro dos desdobros e das edificações junto ao Cartório de Registro de Imóveis competente.')
font = paragraph.style.font
font.size = Pt(10)
font.name = 'Arial'
paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY

paragraph = document.add_paragraph('        	Nestes termos,')
font = paragraph.style.font
font.size = Pt(10)
font.name = 'Arial'
paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY
paragraph.paragraph_format.space_after = Cm(0)

paragraph = document.add_paragraph('        	Peço Deferimento.')
font = paragraph.style.font
font.size = Pt(10)
font.name = 'Arial'
paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.JUSTIFY

paragraph = document.add_paragraph('Hortolândia, _____ de _________________ de ________ . ')
font = paragraph.style.font
font.size = Pt(10)
font.name = 'Arial'
paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT

paragraph = document.add_paragraph('\n\n____________________________________________ '
                                   '\nProprietário'
                                   '\n\n\n____________________________________________'
                                   '\nResponsável técnico')
font = paragraph.style.font
font.size = Pt(10)
font.name = 'Arial'
paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT

document.save("aa.docx")