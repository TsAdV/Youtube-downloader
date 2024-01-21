import cv2
from tkinter import *
from PIL import Image, ImageTk, ImageSequence
import os, sys
from pytube import YouTube
from tkinter import filedialog




def resource_path(relative_path):
    try:
        base_path = sys.MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def Gif(i):
    print("Gif section")
    if i == 1:
        count = 1
        while True:
            count += 1
            img = Image.open(resource_path("Text.gif"))
            lbl.update()
            #lbl = Label(root)
            lbl.place(x=90, y=20)
            for img in ImageSequence.Iterator(img):
                img = img.resize((500, 243))
                img = ImageTk.PhotoImage(img)
                lbl.config(image=img)
                root.update()
    elif i == 2:
        count = 1
        while True:
            count += 1
            img = Image.open(resource_path("7OS4.gif"))
            lbl.update()
            #lbl = Label(root)
            lbl.place(x=90, y=50)
            for img in ImageSequence.Iterator(img):
                img = img.resize((500, 243))
                img = ImageTk.PhotoImage(img)
                lbl.config(image=img)
                root.update()
            return



    elif i == 3:
        count = 1
        while True:
            count += 1
            img = Image.open(resource_path("giphy.gif"))
            lbl.update()
            #lbl = Label(root)
            lbl.place(x=90, y=50)
            for img in ImageSequence.Iterator(img):
                img = img.resize((500, 243))
                img = ImageTk.PhotoImage(img)
                lbl.config(image=img)
                root.update()



#download
def download_video(url,save_path):
    
    print("reached video downloading section")
    yt = YouTube(url)
    try:

        yt = YouTube(url)
        # Streams= yt.streams.filter(progressive=True,file_extension="mp4")

        Format = input("Please select "
                       "H for HQ"
                       "L for LQ"
                       "M for Mp3:")
        print(Format)
        if Format == "H":
            print("downloading High quality")
            Streams = yt.streams.filter(progressive=True, file_extension="mp4")
            highestResolution_stream = Streams.get_highest_resolution()
            highestResolution_stream.download(output_path=save_path)
            print("Video download is Successfull")

        elif Format == "L":
            print("downloading low quality")
            Streams = yt.streams.filter(progressive=True, file_extension="mp4")
            lowestResolution_stream = Streams.get_lowest_resolution()
            lowestResolution_stream.download(output_path=save_path)
            print("Video download is Successfull")

        elif Format == "M":
            print("downloading Medium quality")
            Streams = yt.streams.filter(only_audio=True)
            audioResolution_stream = Streams.get_audio_only(True, 'mp3')
            audioResolution_stream.download(output_path=save_path)
            print("Video download is Successfull")

        else:
            print("unsupported format")
    except Exception as e:
        print(e)





#save_directory
def open_file_dialogue():
    print("Button function")
    folder = filedialog.askdirectory()
    if folder:
        print(f"selected folder:{folder}")
        return folder
    else:
        print("Invalid save location")


def url_check():
    vid_url = link_entry.get()
    save_dir = open_file_dialogue()

    print("url checking reached")
    if save_dir:

        print("started downloading....")
        download_video(vid_url, save_dir)
        print("test")


    else:
        print("Invalid save location")



root=Tk()
root.geometry("700x600")
root.title("Youtube HQ video downloader")
global img
count= IntVar()
i= IntVar()
lbl = Label(root)
link_entry = StringVar()

entry_widget = Entry(root,textvariable=link_entry, width=60).place(x=100,y=380)

print(link_entry)

Button(text="Convert", command = url_check).place(x=100, y=350)
lbl.config(Gif(1))
















root.mainloop()