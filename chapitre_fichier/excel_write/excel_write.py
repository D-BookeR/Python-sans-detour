import pandas

mes_donnees = [[1,'=sum(A1:A2)'],[3,'=average(A1:A2)']]
feuille = pandas.DataFrame([[1,'=sum(A1:A2)'],[3,'=average(A1:A2)']])

#feuille.to_excel("classeur.xlsx", sheet_name="Feuille", index=False, header=False)


feuille = pandas.DataFrame([[1,'=sum(C5:C6)','=D5*D6'],[3,'=average(C5:C6)']])

feuille.to_excel("classeur.xlsx", sheet_name="Feuille", index=False, header=False,startrow=4, startcol=2)
