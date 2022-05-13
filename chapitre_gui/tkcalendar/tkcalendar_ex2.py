import tkinter
import datetime
import tkcalendar

def changement_date(event, l_date):
    date_choisie = event.widget.get_date()
    date_python = datetime.datetime.strptime(date_choisie,"%d/%m/%Y")
    if date_python not in l_date:
        event.widget.calevent_create(date_python, "","")
        l_date.append(date_python)      
    else:
        l_date.remove(date_python)
        event.widget.calevent_remove(date=date_python)

if __name__ == '__main__':
    fen_principale = tkinter.Tk(className="Usage tkcalendar")
    liste_dates = []
    calendrier = tkcalendar.Calendar(fen_principale,
                                        width=12,
                                        background='darkblue',
                                        foreground='white',
                                        borderwidth=2,
                                        year=2022,
                                        locale='fr_FR')
    calendrier.bind("<<CalendarSelected>>",
                     lambda event: changement_date(event, liste_dates))
    calendrier.pack()
    fen_principale.mainloop()
    for date_selec in liste_dates:
        print(date_selec)
