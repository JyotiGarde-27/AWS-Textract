import profile
import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
import boto3

my_w=tk.Tk()
my_w.geometry("450x400")
my_w.title("Aws Textract")
my_font1=('times', 18, 'bold')
l1=tk.Label(my_w, text="Upload an Image", width=30, font=my_font1)
l1.pack()
b1=tk.Button(my_w, text='Upload file and See what it has!!!', width=30, command=lambda:upload_file())
b1.pack()
def upload_file():
    aws_mag_con=boto3.session.Session(profile_name='demo_user')
    boto3.client=aws_mag_con.client(service_name='textract', region_name='us-east-2')
    global img
    f_types=[('Jpg Files', "*.jpg")]
    # f_types=[('png Files',"*.png")]
    # f_types=[('pdf Files',"*.pdf")]

    filename=filedialog.askopenfilename(filetype=f_types)
    img=Image.open(filename)
    # resizing 
    img_resized=img.resize((400,200))
    img=ImageTk.PhotoImage(img_resized)
    imgbytes=get_image_byte(filename)

    b2=tk.Button(my_w, image=img)
    b2.pack()
    response=boto3.client.detect_document_text(Document={'Bytes':imgbytes})
    for item in response['Blocks']:
        if item['BlockType']=='LINE':
            print(item['Text'])
def get_image_byte(filename):
        with open(filename, 'rb') as imgfile:
            return imgfile.read()    

my_w.mainloop()