# ---------------------CHECK LIST REG.---------------------------------------------------------------------------------------------
if self.cbox_reg.isChecked() == True:
document = Document()

sections = document.sections
for section in sections:
    section.top_margin = Cm(0)
    section.bottom_margin = Cm(0)
    section.left_margin = Cm(1.27)
    section.right_margin = Cm(0)

section = document.sections[0]

header = document.sections[0].header
logo = header.paragraphs[0]
document.sections[0].header_distance = Cm(0.5)
document.sections[0].footer_distance = Cm(0)
logo.header_distance = Cm(10.0)
logo_run = logo.add_run()
logo_run.add_picture("images/logo.png", width=Cm(1.4), height=Cm(1.4))

paragraph = document.add_paragraph(''+nomecli1+'')
paragraph.style = document.styles.add_style('style', WD_STYLE_TYPE.PARAGRAPH)
font = paragraph.style.font
font.bold = True
font.name = 'Arial'
font.size = Pt(12)
paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

paragraph = document.add_paragraph('Cód. Cliente: '+idcli1+' \nCód. Obra: '+idobra+'')
paragraph.style = document.styles.add_style('style2', WD_STYLE_TYPE.PARAGRAPH)
font = paragraph.style.font
# font.bold = True
font.name = 'Arial'
font.size = Pt(10)

paragraph = document.add_paragraph('╔══════════════════════════════════════════════════════╗   \n'
           '║                                   DOCUMENTOS PARA REGULARIZAÇÃO                                 ║\n'
           '╚══════════════════════════════════════════════════════╝')
paragraph.style = document.styles.add_style('style3', WD_STYLE_TYPE.PARAGRAPH)
font = paragraph.style.font
font.name = 'Arial'
font.bold = True
paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
font.size = Pt(13)

paragraph = document.add_paragraph('☐ Certidão negativa de débitos,\n'
           '☐ Requerimento assinado pelo proprietario, \n'
           '☐ Cópia autenticada da escritura ou contrato de compra e venda, (se caso a escritura não for registrada), \n'
           '☐ 2 Projeto em A2,\n'
           '☐ Matrícula atualizada (vale por 30 dias),\n'
           '☐ Duas vias de ART (vale por 10 dias), \n'
           '☐ Ficha informativa.')
paragraph.style = document.styles.add_style('style4', WD_STYLE_TYPE.PARAGRAPH)
font = paragraph.style.font
font.name = 'Arial'
# paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
font.size = Pt(12)

paragraph = document.add_paragraph('╔══════════════════════════════════════════════════════╗ \n'
           '║                                   DADOS NECESSÁRIOS PARA CADASTRO                              ║\n'
           '╚══════════════════════════════════════════════════════╝')
paragraph.style = document.styles.add_style('style5', WD_STYLE_TYPE.PARAGRAPH)
font = paragraph.style.font
font.name = 'Arial'
font.bold = True
paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
font.size = Pt(13)

paragraph = document.add_paragraph('CLIENTE')
paragraph.style = document.styles.add_style('style6', WD_STYLE_TYPE.PARAGRAPH)
font = paragraph.style.font
font.bold = True
font.name = 'Arial'
font.size = Pt(13)
paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

paragraph = document.add_paragraph('☐CPF\n'
           '☐RG\n'
           '☐Profissão\n'
           '☐Comprovante de endereço\n'
           '☐Estado Civil\n'
           '☐Email\n'
           '☐Celular\n\n')
paragraph.style = document.styles.add_style('style7', WD_STYLE_TYPE.PARAGRAPH)
font = paragraph.style.font
font.name = 'Arial'
# paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT
font.size = Pt(12)

paragraph = document.add_paragraph('OBRA')
paragraph.style = document.styles.add_style('style8', WD_STYLE_TYPE.PARAGRAPH)
font = paragraph.style.font
font.bold = True
font.name = 'Arial'
font.size = Pt(12)
paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER

paragraph = document.add_paragraph('☐Matricula / Escritura\n'
           '☐Espelho do IPTU / Certidão de Área Construída\n'
           '☐Valor da Parcela________________________________\n'
           '☐Quantidade de Parcela___________________________\n'
           '☐ Valor da visita__________________________________\n'
           '☐Data do contrato_________/__________/_____________\n')
paragraph.style = document.styles.add_style('style9', WD_STYLE_TYPE.PARAGRAPH)
font = paragraph.style.font
font.name = 'Arial'
# paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.RIGHT
font.size = Pt(12)

document.save('//ROGER2/Users/ROCHA/Documents/PROCESSO DE CLIENTES/' + cidadeobra + '/' + nomecli1 + '/' + tipoobra + '/' + ano + '/Documentos/Check List Regularização ' + nomecli1 + '.docx')

# ---------------------CHECK LIST SUB/REG.---------------------------------------------------------------------------------------------
if self.cbox_subreg.isChecked() == True:
document = Document()

sections = document.sections
for section in sections:
    section.top_margin = Cm(0)
    section.bottom_margin = Cm(0)
    section.left_margin = Cm(1.27)
    section.right_margin = Cm(0)

section = document.sections[0]

header = document.sections[0].header
logo = header.paragraphs[0]
document.sections[0].header_distance = Cm(0.5)
document.sections[0].footer_distance = Cm(0)
logo.header_distance = Cm(10.0)
logo_run = logo.add_run()
logo_run.add_picture("images/logo.png", width=Cm(1.4), height=Cm(1.4))

paragraph = document.add_paragraph(''+nomecli1+'')
paragraph.style = document.styles.add_style('style', WD_STYLE_TYPE.PARAGRAPH)
font = paragraph.style.font
font.bold = True
font.name = 'Arial'
font.size = Pt(12)
paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
paragraph.paragraph_format.line_spacing = Cm(0)
paragraph.paragraph_format.space_after = Cm(0)

paragraph = document.add_paragraph('Cód. Cliente: '+idcli1+' \nCód. Obra: '+idobra+'')
paragraph.style = document.styles.add_style('style2', WD_STYLE_TYPE.PARAGRAPH)
font = paragraph.style.font
# font.bold = True
font.name = 'Arial'
font.size = Pt(10)
paragraph.paragraph_format.line_spacing = Cm(0)
paragraph.paragraph_format.space_after = Cm(0)

paragraph = document.add_paragraph('╔══════════════════════════════════════════════════════╗   \n'
           '║                  DOCUMENTOS PARA SUBDIVISÃO COM REGULARIZAÇÃO                 ║\n'
           '╚══════════════════════════════════════════════════════╝\n')
paragraph.style = document.styles.add_style('style3', WD_STYLE_TYPE.PARAGRAPH)
font = paragraph.style.font
font.name = 'Arial'
font.bold = True
font.size = Pt(13)
paragraph.paragraph_format.line_spacing = Cm(0)
paragraph.paragraph_format.space_after = Cm(0)

paragraph = document.add_paragraph('Montar nesta sequência:')
paragraph.style = document.styles.add_style('style4', WD_STYLE_TYPE.PARAGRAPH)
font = paragraph.style.font
font.name = 'Arial'
font.size = Pt(10)
paragraph.paragraph_format.line_spacing = Cm(0)
paragraph.paragraph_format.space_after = Cm(0)

paragraph = document.add_paragraph('SUBDIVISÃO:')
paragraph.style = document.styles.add_style('style5', WD_STYLE_TYPE.PARAGRAPH)
font = paragraph.style.font
font.name = 'Arial'
font.bold = True
font.size = Pt(10)
paragraph.paragraph_format.line_spacing = Cm(0)
paragraph.paragraph_format.space_after = Cm(0)

paragraph = document.add_paragraph('    ☐ Requerimento para subdivisão assinado por todos os proprietários,\n'
           '    ☐ Matrícula atualizada vale por 30 dias para subdivisão (Original)\n'
           '    ☐ Cópia autenticada da escritura ou contrato de compra e venda para a subdivisão\n'
           '    ☐ ART vale por 10 dias para subdivisão\n'
           '    ☐ Certidão negativa de débitos,\n'
           '    ☐ Foto faixada dos dois lotes (casas) para subdivisão\n'
           '    ☐ Memorial descritivo para subdivisão assinado por todos os proprietários,\n'
           '    ☐ Projeto em A2 só do terreno situação atual e pretendida para subdivisão.\n')
paragraph.style = document.styles.add_style('style6', WD_STYLE_TYPE.PARAGRAPH)
font = paragraph.style.font
font.name = 'Arial'
font.size = Pt(10)
paragraph.paragraph_format.line_spacing = Cm(0)
paragraph.paragraph_format.space_after = Cm(0)

paragraph = document.add_paragraph('REGULARIZAÇÃO LOTE A:')
paragraph.style = document.styles.add_style('style7', WD_STYLE_TYPE.PARAGRAPH)
font = paragraph.style.font
font.name = 'Arial'
font.bold = True
font.size = Pt(10)
paragraph.paragraph_format.line_spacing = Cm(0)
paragraph.paragraph_format.space_after = Cm(0)

paragraph = document.add_paragraph(
'    ☐ Requerimentos para regularização lote A assinado por todos os proprietários desta parte,\n'
'    ☐ Matrícula atualizada vale por 30 dias para regularização lote A (Cópia)\n'
'    ☐ Cópia autenticada da escritura ou contrato de compra e venda para a regularização lote \n'
'    ☐ ART vale por 10 dias para regularização lote A\n'
'    ☐ Foto faixada do lote A (casa) para regularização\n'
'    ☐ Projeto em A2 de regularização para o lote A\n'
'    ☐ Ficha informativa, após dar entrada no processo no protocolo.\n')
paragraph.style = document.styles.add_style('style8', WD_STYLE_TYPE.PARAGRAPH)
font = paragraph.style.font
font.name = 'Arial'
font.size = Pt(10)
paragraph.paragraph_format.line_spacing = Cm(0)
paragraph.paragraph_format.space_after = Cm(0)

paragraph = document.add_paragraph('REGULARIZAÇÃO LOTE B:')
paragraph.style = document.styles.add_style('style9', WD_STYLE_TYPE.PARAGRAPH)
font = paragraph.style.font
font.name = 'Arial'
font.bold = True
font.size = Pt(10)
paragraph.paragraph_format.line_spacing = Cm(0)
paragraph.paragraph_format.space_after = Cm(0)

paragraph = document.add_paragraph(
'    ☐ Requerimentos para regularização lote B assinado por todos os proprietários desta parte,\n'
'    ☐ Matrícula atualizada vale por 30 dias para regularização lote B (Cópia)\n'
'    ☐ Cópia autenticada da escritura ou contrato de compra e venda para a regularização lote B\n'
'    ☐ ART vale por 10 dias para regularização lote B\n'
'    ☐ Foto faixada do lote B (casa) para regularização\n'
'    ☐ Projeto em A2 de regularização para o lote B\n'
'    ☐ Ficha informativa, após dar entrada no processo no protocolo.\n')
paragraph.style = document.styles.add_style('style10', WD_STYLE_TYPE.PARAGRAPH)
font = paragraph.style.font
font.name = 'Arial'
font.size = Pt(10)
paragraph.paragraph_format.line_spacing = Cm(0)
paragraph.paragraph_format.space_after = Cm(0)

paragraph = document.add_paragraph(
'Obs: A matrícula e as copias autenticadas, se tiver com os dois processos, subdivisão e regularização, neste caso, as originais no processo de subdivisão e as cópias comum  de ambos (matrícula e as copias autenticadas) para cada meio lote.')
paragraph.style = document.styles.add_style('style11', WD_STYLE_TYPE.PARAGRAPH)
font = paragraph.style.font
font.name = 'Arial'
font.size = Pt(7)
paragraph.paragraph_format.line_spacing = Cm(0)
paragraph.paragraph_format.space_after = Cm(0)

paragraph = document.add_paragraph('╔══════════════════════════════════════════════════════╗ \n'
           '║                                   DADOS NECESSÁRIOS PARA CADASTRO                              ║\n'
           '╚══════════════════════════════════════════════════════╝')
paragraph.style = document.styles.add_style('style12', WD_STYLE_TYPE.PARAGRAPH)
font = paragraph.style.font
font.name = 'Arial'
font.bold = True
font.size = Pt(13)
paragraph.paragraph_format.line_spacing = Cm(0)
paragraph.paragraph_format.space_after = Cm(0)

paragraph = document.add_paragraph('CLIENTE')
paragraph.style = document.styles.add_style('style13', WD_STYLE_TYPE.PARAGRAPH)
font = paragraph.style.font
font.bold = True
font.name = 'Arial'
font.size = Pt(12)
paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
paragraph.paragraph_format.line_spacing = Cm(0)
paragraph.paragraph_format.space_after = Cm(0)

paragraph = document.add_paragraph('    ☐CPF						☐RG\n'
           '    ☐Profissão					             ☐Comprovante de endereço\n'
           '    ☐Estado Civil					☐Email\n'
           '    ☐Celular')
paragraph.style = document.styles.add_style('style14', WD_STYLE_TYPE.PARAGRAPH)
font = paragraph.style.font
font.name = 'Arial'
font.size = Pt(10)
paragraph.paragraph_format.line_spacing = Cm(0)
paragraph.paragraph_format.space_after = Cm(0)

paragraph = document.add_paragraph('OBRA')
paragraph.style = document.styles.add_style('style15', WD_STYLE_TYPE.PARAGRAPH)
font = paragraph.style.font
font.bold = True
font.name = 'Arial'
font.size = Pt(12)
paragraph.alignment = WD_PARAGRAPH_ALIGNMENT.CENTER
paragraph.paragraph_format.line_spacing = Cm(0)
paragraph.paragraph_format.space_after = Cm(0)

paragraph = document.add_paragraph(
'    ☐Matricula / Escritura		☐Espelho do IPTU / Certidão de Área Construída\n'
'    ☐Valor da Parcela________________________________\n'
'    ☐Quantidade de Parcela___________________________\n'
'    ☐ Valor da visita__________________________________\n'
'    ☐Data do contrato_________/__________/_____________\n')
paragraph.style = document.styles.add_style('style16', WD_STYLE_TYPE.PARAGRAPH)
font = paragraph.style.font
font.name = 'Arial'
font.size = Pt(10)
paragraph.paragraph_format.line_spacing = Cm(0)
paragraph.paragraph_format.space_after = Cm(0)

document.save('//ROGER2/Users/ROCHA/Documents/PROCESSO DE CLIENTES/' + cidadeobra + '/' + nomecli1 + '/' + tipoobra + '/' + ano + '/Documentos/Check List Subdivizão com Regularização ' + nomecli1 + '.docx')
