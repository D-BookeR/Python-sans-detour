import docx

document = docx.Document()
document.add_paragraph("Ce document word a été créé avec python.")
document.save('my_test.docx')
