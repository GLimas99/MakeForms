from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Pt, RGBColor, Cm
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
# create document
doc = Document()

# add grid table
Nombre_text = 'Dados do requerente (titular do lote ou da edificação)'
table = doc.add_table(rows=1, cols=1, style='Table Grid')
row = table.rows[0]

Nombre_text_formatted = row.cells[0].paragraphs[0].add_run(Nombre_text)
Nombre_text_formatted.font.name = 'Arial'
Nombre_text_formatted.font.size = Pt(10)
Nombre_text_formatted.bold = True

other_text = '\nRazão social/nome: ______________________________________________' \
             '\nCNPJ/CPF nº: ___________________________________________________' \
             '\nE-mail*: ________________________________________________________' \
             '\nTelefone para contato: ____________________________________________'
other_text_formatted = row.cells[0].paragraphs[0].add_run(other_text)
other_text_formatted.font.name = 'Arial'
other_text_formatted.font.size = Pt(10)

other_text2 = '\n*as notificações sobre este processo serão enviadas por e-mail. Favor atentar-se a isso no momento do preenchimento.'
other_text2_formatted = row.cells[0].paragraphs[0].add_run(other_text2)
other_text2_formatted.font.name = 'Arial'
other_text2_formatted.font.size = Pt(10)
other_text2_formatted.bold = True



doc.save("aa.docx")