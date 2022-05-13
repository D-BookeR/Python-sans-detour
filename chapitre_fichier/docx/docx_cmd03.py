import docx

document = docx.Document()
tableau = document.add_table(rows=4, cols=3, style=None)
for idx_lig, lig in enumerate(tableau.rows):
    for c,cellule in enumerate(lig.cells):
        p = cellule.add_paragraph('ligne ')
        p_run = p.add_run(str(idx_lig))
        p_run.bold = True
        p_run.font.size = docx.shared.Pt(20)
        p_run = p.add_run(' colonne ')
        p_run = p.add_run(str(c))
        p_run.font.size = docx.shared.Pt(20)
        p_run.bold = True

document.save('mon_test_tableau.docx')