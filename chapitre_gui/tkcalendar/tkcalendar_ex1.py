import tkinter
import tkcalendar

def changement_date(event):
    date_choisie = event.widget.get_date()
    print(date_choisie)

if __name__ == '__main__':
    fen_principale = tkinter.Tk(className="Usage tkcalendar")
    calendrier = tkcalendar.Calendar(fen_principale,
                                     font="Arial 14",
                                     borderwidth=20,
                                     showweeknumbers=False,
                                     locale='fr_FR')
    calendrier.bind("<<CalendarSelected>>", changement_date)
    calendrier.pack()
    fen_principale.mainloop()
