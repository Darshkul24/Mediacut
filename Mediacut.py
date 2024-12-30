import tkinter as tk
import subprocess

app = tk.Tk()
app.title("Mediacut")
app.state('zoomed')
app.configure(bg="black")

def clear_screen():
    for widget in app.winfo_children():
        widget.destroy()

def header(show_back_button=False, show_exit_button=True):
    clear_screen()
    header = tk.Frame(app, bg="black")
    header.pack(fill="x", side="top", ipadx=0, ipady=15)
    if show_back_button:
        back_button = tk.Button(
            header, 
            text="Back", 
            font=("Arial", 14), 
            fg="white", 
            bg="grey",
            width="8",
            command=main_screen
        )
        back_button.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    if show_exit_button:
        exit_button = tk.Button(
            header, 
            text="Exit", 
            font=("Arial", 14), 
            fg="white", 
            bg="brown", 
            width="8",
            command=lambda: close_app()
        )
        exit_button.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    header_label = tk.Label(
        header,
        text="Mediacut",
        font=("Arial", 24, "bold"),
        fg="white",
        bg="black"
    )
    header_label.grid(row=0, column=1, padx=20, pady=5)
    header.grid_columnconfigure(1, weight=1)

header()

application_screen = tk.Frame(app, bg="black")
application_screen.pack(expand=True)

def download_button(platform, platform_downloader, row, column, bg):
    button = tk.Button(
    application_screen,
    text=platform,
    font=("Arial", 18, "bold"),
    fg="white",
    bg=bg,
    width=20,
    height=5,
    command=platform_downloader
    )
    button.grid(row=row, column=column, padx=50, pady=50)

def youtube_downloader():
    clear_screen()
    header(show_back_button=True,show_exit_button=False)
    youtube_label = tk.Label(app, text="YouTube Downloader", font=("Arial", 24, "bold"), fg="white", bg="black")
    youtube_label.pack(pady=20)G:\Coding\Projects\Incomplete\Mediacut\test.py
    link_label = tk.Label(app, text="Enter Video URL:", font=("Arial", 14), fg="white", bg="black")
    link_label.pack(pady=5)

    link_entry = tk.Entry(app, font=("Arial", 14), width=40)
    link_entry.pack(pady=10)

def facebook_downloader():
    clear_screen()
    header(show_back_button=True,show_exit_button=False)
    facebook_label = tk.Label(app, text="Facebook Downloader", font=("Arial", 24, "bold"), fg="white", bg="black")
    facebook_label.pack(pady=20)

def instagram_downloader():
    clear_screen()
    header(show_back_button=True,show_exit_button=False)
    instagram_label = tk.Label(app, text="Instagram Downloader", font=("Arial", 24, "bold"), fg="white", bg="black")
    instagram_label.pack(pady=20)

def spotify_downloader():
    clear_screen()
    header(show_back_button=True,show_exit_button=False)
    spotify_label = tk.Label(app, text="Spotify Downloader", font=("Arial", 24, "bold"), fg="white", bg="black")
    spotify_label.pack(pady=20)

platforms = [
        ("YouTube", youtube_downloader, 0, 0, "red"),
        ("Facebook", facebook_downloader, 0, 1, "blue"),
        ("Instagram", instagram_downloader, 0, 2, "purple"),
        ("Spotify", spotify_downloader, 1, 0, "green")
    ]

application_screen.pack(expand=True)

for platform, downloader, row, column, bg in platforms:
    download_button(platform, downloader, row, column, bg)

def main_screen():
    clear_screen()
    header(show_back_button=False, show_exit_button=True)

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
app.bind("<Shift-Escape>", lambda event: close_app())

app.mainloop()
