import tkinter as tk
import requests
def fetchNews():
    api = "5c67c6acbe74409cb28ab12252cf910f"
    url = "https://newsapi.org/v2/top-headlines?country=us&apiKey="+api
    news = requests.get(url).json()
    articles = news["articles"]
    new_news = ""
    newscast = []
    for article in articles:
        newscast.append(article["title"])
    for i in range(18):
        new_news = new_news + str(i+1) + ". " + newscast[i] + "\n\n"
    label.config(text = new_news)
canvas = tk.Tk()
canvas.geometry("1400x1400")
canvas.title("News App In Python")
label = tk.Label(canvas, font = 28, justify = "left",relief="solid",wraplength="1800")
label.pack(pady = 5)
fetchNews()
canvas.mainloop()
