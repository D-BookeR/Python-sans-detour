ma_variable = 10
def ma_fonction():
    global ma_variable
    ma_variable = 17
    print("Valeur de ma_variable dans ma_fonction : ", ma_variable)

print("Valeur de ma_variable dans le script : ", ma_variable)
ma_fonction()
print("Valeur de ma_variable dans le script après l'appel : ", ma_variable)