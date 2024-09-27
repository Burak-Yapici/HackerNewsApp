import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter import PhotoImage, filedialog
import webbrowser


window=Tk()
window.minsize(width=450,height=600)
window.title("Hacker News")


background_image = PhotoImage(file="matrix2.png")

# Label oluştur ve resmi yerleştir
background_label = Label(window, image=background_image)
background_label.config(width=450,height=600)
background_label.place(relwidth=1, relheight=1)  # Label'ı pencerenin tamamını kaplayacak şekilde yerleştir

my_label = Label(text="Hacker News Here Top 30 List")
my_label.config(bg="black",fg="green",font=("Times", "24", "bold italic"))
my_label.config(padx=800,pady=20)
my_label.pack()


target_url = "https://news.ycombinator.com/news"
foundLinks=[]
new_found_link=[]
link_sonuc=[]

response = requests.get(target_url)
soup = BeautifulSoup(response.text, features="html.parser")

for link in soup.find_all('a'):
        found_link = link.get('href')
        if found_link not in foundLinks:
            foundLinks.append(found_link)
            #if "http" and "https" in found_link:
            if "http" in found_link or "https" in found_link:
                new_found_link.append(found_link)

link_sonuc=[]
link_sonuc.append(new_found_link[1:31])
print(link_sonuc)


my_listbox=Listbox()
my_listbox.config(width=100,height=300)
my_listbox.config(bg="black",fg="green",font=("Times", "11", "bold italic"))
link_sonuc = new_found_link[1:31]
for link in link_sonuc:
    my_listbox.insert(END, link)

my_listbox.pack()



def open_link(event):
    selected_index = my_listbox.curselection()  # Seçili öğenin indeksini al
    if selected_index:  # Eğer bir öğe seçildiyse
        link = my_listbox.get(selected_index)  # Seçili öğeyi al
        webbrowser.open(link)  # Bağlantıyı tarayıcıda aç



my_listbox.bind("<Double-Button-1>", open_link)




window.mainloop()



