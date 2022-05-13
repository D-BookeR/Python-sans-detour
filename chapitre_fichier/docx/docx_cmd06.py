import docx

document = docx.Document()
nb_lig = 4
nb_col = 3
tableau = document.add_table(rows=nb_lig, cols=nb_col)
for idx_lig, lig in enumerate(tableau.rows):
    for c, cellule in enumerate(lig.cells):
        p = cellule.add_paragraph('ligne ')
        p_run = p.add_run(str(idx_lig))
        p_run.bold = True
        p_run.font.size = docx.shared.Pt(20)
        p_run = p.add_run(' colonne ')
        p_run = p.add_run(str(c))
        p_run.font.size = docx.shared.Pt(20)
        p_run.bold = True
document.save('mon_test_tableau.docx')
tableau.alignment = docx.enum.table.WD_TABLE_ALIGNMENT.RIGHT
tableau.style = 'Light Shading'
alignement_vertical = (docx.enum.table.WD_ALIGN_VERTICAL.TOP,
                       docx.enum.table.WD_ALIGN_VERTICAL.CENTER,
                       docx.enum.table.WD_ALIGN_VERTICAL.BOTTOM)
for lig in tableau.rows:
    for idx_col, cellule in enumerate(lig.cells):
        cellule.vertical_alignment = alignement_vertical[idx_col % 3]
document.save('mon_test2_tableau.docx')
tableau.autofit = False
for idx_col, col in enumerate(tableau.columns):
    col.width = docx.shared.Mm(40 - idx_col * 5)
for idx_lig, lig in enumerate(tableau.rows):
    lig.height = docx.shared.Mm(20 + idx_lig*5)
document.save('mon_test3_tableau.docx')
document.add_picture("python_book_docx_image.png")
document.add_picture("python_book_docx_image.png",
                     width=docx.shared.Mm(30))
document.add_picture("python_book_docx_image.png",
                     height=docx.shared.Mm(30))
document.add_picture("python_book_docx_image.png",
                     width=docx.shared.Mm(30),
                     height=docx.shared.Mm(30))
document.save('mon_test4_tableau_img.docx')
