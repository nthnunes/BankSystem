from tkinter import *
ui = Tk()

ui.title("Bank System")

mainText = Label(ui, text="Menu:")
mainText.grid(column=0, row=0)

buttonRegister = Button(ui, text="Cadastrar cliente/conta")
buttonRegister.grid(column=0, row=1)


ui.mainloop()