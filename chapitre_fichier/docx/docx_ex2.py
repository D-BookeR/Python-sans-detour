import docx


def ajouter_paragraphe(doc, m_style=None):
    para = doc.add_paragraph('Ce document Word a été créé avec python.')
    p_run = para.add_run(' On peut mettre le texte en italique et gras')
    p_run.italic = True
    p_run.bold = True
    para.add_run(' et celui-ci en gras uniquement').bold = True
    texte = ' et la fin de la phrase en style de caractères emphasis, '
    para.add_run(texte).style = 'Emphasis'
    para.add_run('style accentuation en français.')
    if m_style:
        para.style = m_style


def creer_style(nom_style, nom_police, taille_police):
    m_style = document.styles.\
                    add_style(nom_style,
                              docx.enum.style.WD_STYLE_TYPE.PARAGRAPH)
    m_style.font.name = nom_police
    m_style.font.size = docx.shared.Pt(taille_police)
    m_style.paragraph_format.alignment =\
        docx.enum.text.WD_ALIGN_PARAGRAPH.JUSTIFY
    m_style.paragraph_format.first_line_indent = docx.shared.Mm(10)
    m_style.paragraph_format.left_indent = docx.shared.Mm(20)
    return m_style


if __name__ == '__main__':
    document = docx.Document()
    document.add_paragraph("Python c'est facile", "Title")
    section = document.sections[0]
    section.different_first_page_header_footer = True
    section.orientation = docx.enum.section.WD_ORIENT.LANDSCAPE
    hauteur_a4 = docx.shared.Twips(docx.shared.Mm(297).twips)
    largeur_a4 = docx.shared.Twips(docx.shared.Mm(210).twips)
    section.page_height, section.page_width = largeur_a4, hauteur_a4
    document.add_section(docx.enum.section.WD_SECTION.NEW_PAGE)
    section = document.sections[1]
    section.orientation = docx.enum.section.WD_ORIENT.PORTRAIT
    section.page_height, section.page_width =\
        section.page_width, section.page_height
    section.different_first_page_header_footer = False
    section.header.is_linked_to_previous = False
    section.footer.is_linked_to_previous = False
    section.header.paragraphs[0].text = \
        "Création de document Word avec Python-docx"
    section.header.paragraphs[0].style.paragraph_format.alignment = \
        docx.enum.text.WD_ALIGN_PARAGRAPH.CENTER
    section.footer.paragraphs[0].text = "Python-docx c'est pratique\t 2021\t"
    style = creer_style('mon_style1', 'Courier New', 20)
    ajouter_paragraphe(document, style)
    document.add_page_break()
    style = creer_style('mon_style2', 'MS Gothic', 8)
    ajouter_paragraphe(document, style)
    document.save('mon_test_page_anglais.docx')
