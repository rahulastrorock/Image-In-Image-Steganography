from PIL import Image

from tkinter import *
from tkinter.filedialog import *
from PIL import ImageTk, Image
from tkinter import messagebox
from tkinter import ttk

MAX_COLOR_VALUE = 255
MAX_BIT_VALUE = 8

# This function takes two inputs the data which is a matrix and resolution of the image and converts it
# into a PIL image object.


def make_image(data, resolution):
    image = Image.new("RGB", resolution)  # makes a new Image object.
    image.putdata(data)  # puts the "data" matrix (pixels) onto the image.

    return image


def remove_n_least_significant_bits(value, n):
    value = value >> n
    return value << n


def get_n_least_significant_bits(value, n):
    value = value << MAX_BIT_VALUE - n
    value = value % MAX_COLOR_VALUE
    return value >> MAX_BIT_VALUE - n


def get_n_most_significant_bits(value, n):
    return value >> MAX_BIT_VALUE - n


def shit_n_bits_to_8(value, n):
    return value << MAX_BIT_VALUE - n


def encrypt():
    Response = messagebox.askyesno("PopUp", "Do you want to encode the image")
    if (Response == 1):
        n_bits = 2

        image_to_hide = Image.open(".\sly.jpg")
        image_to_hide_in = Image.open(".\quote.jpg")

        # now we need to create a copy of image to hide with resolution (width*height of the image to hide_in)
        image_to_hide = image_to_hide.resize(image_to_hide_in.size)

        width, height = image_to_hide_in.size

        # .load() returns the "pixel_access" object that has the data(matrix) of the pixels.
        hide_image = image_to_hide.load()
        hide_in_image = image_to_hide_in.load()

        # this will store the values of each individual pixel as a matrix.
        data = []

        # looping the hide_image object.

        for y in range(height):
            for x in range(width):

                # (107, 3, 10)
                # most sig bits
                # print(hide_image[x,y]) #you can uncomment this to see the pixel values in r,g,b form.
                try:
                    # the value of n can be 1 or 2 and you won't see much difference in the encoded image.
                    # gets n most significant bits of r,g,b values of image to hide.
                    r_hide, g_hide, b_hide = hide_image[x, y]
                    r_hide = get_n_most_significant_bits(r_hide, n_bits)
                    g_hide = get_n_most_significant_bits(g_hide, n_bits)
                    b_hide = get_n_most_significant_bits(b_hide, n_bits)

                    # remove least n significant bits of image to hide in so we can store
                    # the n most significant bits in that place.

                    r_hide_in, g_hide_in, b_hide_in = hide_in_image[x, y]
                    r_hide_in = remove_n_least_significant_bits(
                        r_hide_in, n_bits)
                    g_hide_in = remove_n_least_significant_bits(
                        g_hide_in, n_bits)
                    b_hide_in = remove_n_least_significant_bits(
                        b_hide_in, n_bits)

                    data.append((r_hide + r_hide_in,
                                g_hide + g_hide_in,
                                b_hide + b_hide_in))

                # incase of exception it will show the reason.
                except Exception as e:
                    print(e)

        # return an Image object from the above data.
        make_image(data, image_to_hide.size).save("./encrypted_img.png")
        messagebox.showinfo("Pop Up", "Successfully Encoded the image")
        win = Toplevel()
        win.geometry("750x270")
        win.title("ENCRYPTED IMAGE")
        win.iconbitmap('C:\\Users\\rahul\\Desktop\\OSS PROJECT\\icons\\Hopstarter-Soft-Scraps-Lock-Lock.ico')
        image1 = Image. open("C:\\Users\\rahul\\Desktop\\OSS PROJECT\\encrypted_img.png")
        resized_image= image1.resize((300,205), Image.ANTIALIAS)
        image2 = ImageTk. PhotoImage(resized_image)
        image_label = ttk. Label(win, image=image2)
        image_label.place(x=0, y=0)
        win.mainloop()
    else:
        messagebox.showwarning("Pop Up", "Unsuccessful,please try again")


def encode():

    Screen.destroy()
    EncScreen = Tk()
    EncScreen.title("ENCODING")
    EncScreen.iconbitmap('C:\\Users\\rahul\\Desktop\\OSS PROJECT\\icons\\Oxygen-Icons.org-Oxygen-Apps-preferences-desktop-cryptography.ico')
    EncScreen.geometry("500x500+300+300")
    EncScreen.config(bg="yellow")
    label = Label(text="Choose the first Image")
    label.place(relx=0.1, rely=0.2)
    entry = Entry()
    entry.place(relx=0.5, rely=0.2)
    label1 = Label(text="Choose the second Image")
    label1.place(relx=0.1, rely=0.3)
    SaveEntry = Entry()
    SaveEntry.place(relx=0.5, rely=0.3)

    def OpenFileA():
        global FileOpen
        FileOpen = StringVar()
        FileOpen = askopenfilename(initialdir="/Desktop", title="SelectFile",
                                   filetypes=(("jpeg files", "*jpg"), ("all files", "*.*")))

        label2 = Label(text=FileOpen)
        label2.place(relx=0.5, rely=0.2)
        win = Toplevel()
        win.geometry("750x270")
        win.title("IMAGE TO BE HIDDEN")
        win.iconbitmap('C:\\Users\\rahul\\Desktop\\OSS PROJECT\\icons\\Treetog-I-Image-File.ico')
        image1 = Image. open(
            "C:\\Users\\rahul\\Desktop\\OSS PROJECT\\sly.jpg")
        image2 = ImageTk. PhotoImage(image1)
        image_label = ttk. Label(win, image=image2)
        image_label.place(x=0, y=0)
        win.mainloop()

    def OpenFileB():
        global FileOpen
        FileOpen = StringVar()
        FileOpen = askopenfilename(initialdir="/Desktop", title="SelectFile",
                                   filetypes=(("jpeg files", "*jpg"), ("all files", "*.*")))

        label2 = Label(text=FileOpen)
        label2.place(relx=0.5, rely=0.3)
        win = Toplevel()
        win.geometry("750x270")
        win.iconbitmap('C:\\Users\\rahul\\Desktop\\OSS PROJECT\\icons\\Treetog-I-Image-File.ico')
        win.title("IMAGE TO BE HIDDEN IN")
        image1 = Image. open("C:\\Users\\rahul\\Desktop\\OSS PROJECT\\quote.jpg")
        resized_image= image1.resize((300,205), Image.ANTIALIAS)
        image2 = ImageTk. PhotoImage(resized_image)
        image_label = ttk. Label(win, image=image2)
        image_label.place(x=0, y=0)
        win.mainloop()

    SelectButtonA = Button(text="Select the Image1", command=OpenFileA)
    SelectButtonB = Button(text="Select the Image2", command=OpenFileB)

    SelectButtonA.place(relx=0.1, rely=0.4)
    SelectButtonB.place(relx=0.4, rely=0.4)
    EncodeButton = Button(text="Encode", command=encrypt)
    EncodeButton.place(relx=0.5, rely=0.5)

def decoded():
    n_bits = 2
    image_to_decode = Image.open("quote.jpg")
    width, height = image_to_decode.size
    encoded_image = image_to_decode.load()

    # matrix that will store the extracted pixel values from the encoded Image.
    data = []

    # looping through the encoded Image.
    for y in range(height):
        for x in range(width):

            # gets rgb values of encoded image.
            r_encoded, g_encoded, b_encoded = encoded_image[x, y]

            # get n least significant bits for each r,g,b value of the encoded image
            r_encoded = get_n_least_significant_bits(r_encoded, n_bits)
            g_encoded = get_n_least_significant_bits(g_encoded, n_bits)
            b_encoded = get_n_least_significant_bits(b_encoded, n_bits)

            # shifts the n bits to right so that they occupy a total of 8 bit spaces.
            # like if there 10 are the bits then shifting them would look like 10000000
            # this would ofcourse be converted to an int as per python's bit operations.

            r_encoded = shit_n_bits_to_8(r_encoded, n_bits)
            g_encoded = shit_n_bits_to_8(g_encoded, n_bits)
            b_encoded = shit_n_bits_to_8(b_encoded, n_bits)

            data.append((r_encoded, g_encoded, b_encoded))

    make_image(data, image_to_decode.size).save("./decrypted_img.png")
        
    
    win = Toplevel()
    win.geometry("750x270")
    #win.iconbitmap('C:\\Users\\rahul\\Desktop\\OSS PROJECT)\\icons\\Hopstarter-Soft-Scraps-Lock-Unlock.ico')
    win.title("DECRYPTED IMAGE")
    image1 = Image. open("C:\\Users\\rahul\\Desktop\\OSS PROJECT\\decrypted_img.png")
    #img= (Image.open("./decrypted_img.png"))
    resized_image= image1.resize((300,205), Image.ANTIALIAS)
    image2 = ImageTk. PhotoImage(resized_image)
    image_label = ttk. Label(win, image=image2)
    image_label.place(x=0, y=0)
    messagebox.showinfo("Pop Up", "Successfully Decoded the image")
    win.mainloop()
    

# takes image to decode and n_bits as parameters.

def decode():
    Response = messagebox.askyesno("PopUp", "Do you want to Decode the image")
    if(Response == 1):
        Screen.destroy()
        EncScreen = Tk()
        EncScreen.title("DECODING")
        #EncScreen.iconbitmap('C:\\Users\\rahul\\Desktop\\OSS PROJECT\\icons\\Hopstarter-Soft-Scraps-Lock-Unlock.ico')
        EncScreen.geometry("500x500+300+300")
        EncScreen.config(bg="blue")
        label = Label(text="Choose the Encrypted Image")
        label.place(relx=0.1, rely=0.2)
        entry = Entry()
        entry.place(relx=0.5, rely=0.2)
        
        def OpenFileA():
            global FileOpen
            FileOpen = StringVar()
            FileOpen = askopenfilename(initialdir="/Desktop", title="SelectFile",
                                   filetypes=(("jpeg files", "*jpg"),("image files", ".png"), ("all files", "*.*")))

            label2 = Label(text=FileOpen)
            label2.place(relx=0.5, rely=0.2)
            win = Toplevel()
            win.geometry("750x270")
            win.title("Encoded Image")
            win.iconbitmap('C:\\Users\\rahul\\Desktop\\OSS PROJECT\\icons\\Treetog-I-Image-File.ico')
            image1 = Image. open(
                "C:\\Users\\rahul\\Desktop\\OSS PROJECT\\quote.jpg")
            resized_image= image1.resize((300,205), Image.ANTIALIAS)
            image2 = ImageTk. PhotoImage(resized_image)
            image_label = ttk. Label(win, image=image2)
            image_label.place(x=0, y=0)
            win.mainloop()
        
        
        SelectButtonA = Button(text="Select the Image1", command=OpenFileA)
        SelectButtonA.place(relx=0.1, rely=0.4)
        EncodeButton = Button(text="Decode", command=decoded)
        EncodeButton.place(relx=0.5, rely=0.5)
    else:
        messagebox.showwarning("Pop Up", "Unsuccessful,please try again")

    
    


Screen = Tk()
Screen.title("Image Steganography by - astrorock ")
Screen.geometry("500x500+300+300")
Screen['bg'] = '#ADD8E6'
# creating buttons
EncodeButton = Button(text="Encode", command=encode)
EncodeButton.place(relx=0.3, rely=0.4)

DecodeButton = Button(text="Decode", command=decode)
DecodeButton.place(relx=0.6, rely=0.4)


"""""

if "__main__":
    n_bits = 2
    cmd=int(input("To encode input 1 to decode input 2:"))

    encoded_image_path = "./encoded.png"
    decoded_image_path = "./decoded.png"
    
    if cmd==1:
        image_to_hide_path = ".\sly.jpg"
        image_to_hide_in_path = ".\quote.jpg"
        image_to_hide = Image.open(image_to_hide_path)
        image_to_hide_in = Image.open(image_to_hide_in_path)
        #now we need to create a copy of image to hide with resolution (width*height of the image to hide_in)
        image_to_hide=image_to_hide.resize(image_to_hide_in.size)
        
        encode(image_to_hide, image_to_hide_in, n_bits).save(encoded_image_path)

    if cmd==2:
        image_to_decode = Image.open(encoded_image_path)
        decode(image_to_decode, n_bits).save(decoded_image_path)

"""
