import tkinter as tk

app = tk.Tk()
app.title("Mediacut")
app.state('zoomed')
app.configure(bg="black")
app.font=("Arial", 24)


def close_app():
    app.destroy()

app.bind("<Control-q>", lambda event: close_app())

app.mainloop()