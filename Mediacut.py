import tkinter as tk
import subprocess

app = tk.Tk()
app.title("Mediacut")
app.state('zoomed')
app.configure(bg="black")

def header():
    header = tk.Frame(app, bg="darkblue")
    header.pack(fill="x", side="top", ipadx=0, ipady=15)
    header_label = tk.Label(
        header,
        text="Mediacut",
        font=("Arial", 24, "bold"),
        fg="white",
        bg="darkblue"
    )
    header_label.pack(expand=True, pady=10)

header()

def clear_screen():
    for widget in app.winfo_children():
        widget.destroy()


application_screen = tk.Frame(app, bg="black")
application_screen.pack(expand=True)

def youtube_downloader():
    clear_screen()
    header()
    youtube_label = tk.Label(app, text="YouTube Downloader", font=("Arial", 24, "bold"), fg="white", bg="black")
    youtube_label.pack(pady=20)
    back_button = tk.Button(app, text="Back", font=("Arial", 14), fg="white", bg="grey", command=main_screen)
    back_button.pack(padx=10, pady=10)

youtube = tk.Button(
    application_screen,
    text="YouTube",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="red",
    width=20,
    height=5,
    command=lambda: youtube_downloader()
)
youtube.grid(row=0, column=0, padx=50, pady=50)

def facebook_downloader():
    clear_screen()
    header()
    facebook_label = tk.Label(app, text="Facebook Downloader", font=("Arial", 24, "bold"), fg="white", bg="black")
    facebook_label.pack(pady=20)
    back_button = tk.Button(app, text="Back", font=("Arial", 14), fg="white", bg="grey", command=main_screen)
    back_button.pack(pady=10)

facebook = tk.Button(
    application_screen,
    text="Facebook",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="blue",
    width=20,
    height=5,
    command=lambda: facebook_downloader()
)
facebook.grid(row=0, column=1, padx=50, pady=50)

def instagram_downloader():
    clear_screen()
    header()
    instagram_label = tk.Label(app, text="Instagram Downloader", font=("Arial", 24, "bold"), fg="white", bg="black")
    instagram_label.pack(pady=20)
    back_button = tk.Button(app, text="Back", font=("Arial", 14), fg="white", bg="grey", command=main_screen)
    back_button.pack(pady=10)

instagram = tk.Button(
    application_screen,
    text="Instagram",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="purple",
    width=20,
    height=5,
    command=lambda: instagram_downloader()
)
instagram.grid(row=0, column=2, padx=50, pady=50)

def spotify_downloader():
    clear_screen()
    header()
    spotify_label = tk.Label(app, text="Spotify Downloader", font=("Arial", 24, "bold"), fg="white", bg="black")
    spotify_label.pack(pady=20)
    back_button = tk.Button(app, text="Back", font=("Arial", 14), fg="white", bg="grey", command=main_screen)
    back_button.pack(pady=0)

spotify = tk.Button(
    application_screen,
    text="Spotify",
    font=("Arial", 18, "bold"),
    fg="white",
    bg="green",
    width=20,
    height=5,
    command=lambda: spotify_downloader()
)
spotify.grid(row=1, column=0, padx=50, pady=50)

def main_screen():
    clear_screen()
    header()

    global application_screen
    application_screen = tk.Frame(app, bg="black")
    application_screen.pack(expand=True)

    youtube = tk.Button(
        application_screen,
        text="YouTube",
        font=("Arial", 18, "bold"),
        fg="white",
        bg="red",
        width=20,
        height=5,
        command=youtube_downloader
    )
    youtube.grid(row=0, column=0, padx=50, pady=50)

    facebook = tk.Button(
        application_screen,
        text="Facebook",
        font=("Arial", 18, "bold"),
        fg="white",
        bg="blue",
        width=20,
        height=5,
        command=facebook_downloader
    )
    facebook.grid(row=0, column=1, padx=50, pady=50)

    instagram = tk.Button(
        application_screen,
        text="Instagram",
        font=("Arial", 18, "bold"),
        fg="white",
        bg="purple",
        width=20,
        height=5,
        command=instagram_downloader
    )
    instagram.grid(row=0, column=2, padx=50, pady=50)

    spotify = tk.Button(
        application_screen,
        text="Spotify",
        font=("Arial", 18, "bold"),
        fg="white",
        bg="green",
        width=20,
        height=5,
        command=spotify_downloader
    )
    spotify.grid(row=1, column=0, padx=50, pady=50)

def close_app():
    app.destroy()
app.bind("<Control-q>", lambda event: close_app())

app.mainloop()
