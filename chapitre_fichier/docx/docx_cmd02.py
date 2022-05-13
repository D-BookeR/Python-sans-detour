import docx

document = docx.Document()

p = document.add_paragraph('Gérer les styles', "Heading 1")
p = document.add_paragraph('Ce document Word a été créé avec python.')
p_run = p.add_run(' On peut mettre le texte en italique et gras')
p_run.italic = True
p_run.bold = True
p.add_run(' et celui-ci en gras uniquement').bold = True
p.add_run(' et la fin de la phrase en style de caractères emphasis, ').style = 'Emphasis'
p.add_run('style accentuation en français.')
mon_style = document.styles.add_style('mon_style1', docx.enum.style.WD_STYLE_TYPE.PARAGRAPH)
mon_style.font.name = 'Consolas'
mon_style.font.size = docx.shared.Pt(20)
mon_style.paragraph_format.alignment = docx.enum.text.WD_ALIGN_PARAGRAPH.JUSTIFY
mon_style.paragraph_format.first_line_indent = docx.shared.Mm(10)
mon_style.paragraph_format.left_indent = docx.shared.Mm(20)
p.style = mon_style
document.save('mon_test_style.docx')
