# Changes part of filenames in folder, E.g. searches every folder for specific text and replaces with what the user wants
# made by Adam Fox


import os
from tkinter.filedialog import askdirectory
import PySimpleGUI as sg

file_path = r'{}'.format(askdirectory(title="Choose Folder where images located"))

def User_inputs():

    layout = [
        [sg.Text('What string do you want to replace/remove?'), sg.InputText()],
        [sg.Text("What do you want to replace the string with?"), sg.InputText()],
        [sg.Button("OK"), sg.Button("Cancel")]  
    ]

    window=sg.Window("input Window", layout)

    while True:
        event, values= window.read()
        if event in (None,"Cancel"):
            break
        elif event == "OK":
                    
            orig_txt = values[0]
            replace_txt = values[1]
            print(f"replace substring {orig_txt} with {replace_txt}")
            window.close()
            break


    window.close()
    return orig_txt, replace_txt


orig_txt, replace_txt = User_inputs()

orig_txt=str(orig_txt)
replace_txt=str(replace_txt)

os.chdir(file_path)
#then you will use this 
for filename in os.listdir(file_path):
    os.rename(filename, filename.replace(orig_txt, replace_txt))