import pandas

feuille1 = pandas.DataFrame([[1,'=sum(A1:A2)'],[3,'=average(A1:A2)']])
feuille2 = pandas.DataFrame([[1,'=sum(C5:C6)','=D5*D6'],[3,'=average(C5:C6)']])

with pandas.ExcelWriter('classeur_multiple.xlsx') as classeur_cible:  
    feuille1.to_excel(classeur_cible, 
                      sheet_name="Feuille1",
                      index=False,
                      header=False)
    feuille2.to_excel(classeur_cible,
                      sheet_name="Feuille2",
                      index=False,
                      header=False,
                      startrow=4,
                      startcol=2)


