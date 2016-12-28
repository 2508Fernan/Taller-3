from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=800, height=800)
canvas.pack()
tk.title("Mi Foto")
my_image = PhotoImage (file="Fernan.png")
canvas.create_image(0,0,anchor=NW, image=my_image)

def movePhoto(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -3)
    elif event.keysym == 'Down':
        canvas.move(1, 0, 3)
    elif event.keysym == 'Left':
        canvas.move(1, -3, 0)
    else:
        canvas.move(1, 3, 0)
        
canvas.bind_all('<KeyPress-Up>', movePhoto)
canvas.bind_all('<KeyPress-Down>', movePhoto)
canvas.bind_all('<KeyPress-Left>', movePhoto)
canvas.bind_all('<KeyPress-Right>', movePhoto)

tk.mainloop()
