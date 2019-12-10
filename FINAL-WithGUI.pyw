import tkinter
import sys

##This class is used to capture the output that is outputed to the CLI. 

class StdRedirector():
    def __init__(self, text_widget):
        self.text_space = text_widget

    def write(self, string):
        self.text_space.config(state=tkinter.NORMAL)
        self.text_space.insert("end", string)
        self.text_space.see("end")
        self.text_space.config(state=tkinter.DISABLED)

##This class builds the GUI

class GUI:

    def __init__(self):

        ##Creates a window using tkinter
        
        self.main_window = tkinter.Tk()
        self.main_window.title("Encrypt - Decrypt")
        self.main_window.iconbitmap("__pycache__\\favicon.ico")
        self.main_window.config(background = 'black')


        ##Builds the frame for each of the elements that will be in the GUI
        
        self.frame_buttons = tkinter.Frame(self.main_window)
        
        self.frame_text = tkinter.Frame(self.main_window)
        
        self.options_text = tkinter.Frame(self.main_window)
        
        self.text_field = tkinter.Frame(self.main_window)

        ##Creates a scrollbar in text_field
        
        self.scroll = tkinter.Scrollbar(self.text_field)


        ##Places text in the corresponding field
        
        self.frame_text_label2 = tkinter.Label(self.frame_text, text = "Generating a new key will destroy the previous key.", bg="black", fg = "white")
        self.frame_text_label3 = tkinter.Label(self.frame_text, text = "USE WITH CAUTION", wraplength = '200', bg = 'black',fg = "red")
        self.frame_text_label2.pack(side = "top",expand='yes', fill='both')
        self.frame_text_label3.pack(side = "top",expand='yes', fill='both')

        ##Places text in the corresponding field
        
        self.options_text_label = tkinter.Label(self.options_text, text = "Enter the file's name or the text you would like to encrypt.", bg="black", fg = "white")
        self.options_text_entry = tkinter.Entry(self.options_text, width = 28, bg="white", fg = "black", bd = 5)
        self.options_text_label.pack(side = "top",expand='yes', fill='both')
        self.options_text_entry.pack(side = "top",expand='yes', fill='both')
        


        ##Creates the buttons that we will be using to call the respective functions
        
        self.frame_buttons_button1 = tkinter.Button(self.frame_buttons, text = 'Encrypt', command = self.encode_program, bg="black", fg = "white")
        self.frame_buttons_button2 = tkinter.Button(self.frame_buttons, text = 'Decrypt', command = self.decode_program, bg="black", fg = "white")
        self.frame_buttons_button3 = tkinter.Button(self.frame_buttons, text = 'Generate New Key', command = self.gen_new_key, bg="black", fg = "white")
        self.frame_buttons_button1.pack(side = "left",expand='yes', fill='both')
        self.frame_buttons_button2.pack(side = "right",expand='yes', fill='both')
        self.frame_buttons_button3.pack(side = 'right',expand='yes', fill='both')

        ##Creates a text box that will be used to output the captured CLI output

        self.text_field_text = tkinter.Text(self.text_field, width = 75, height = 20, bg="black", fg = "white")
        self.text_field_text.config(yscrollcommand=self.scroll.set)
        self.text_field_text.insert("end", "Welcome to Justins encrypting and decrypting program.\n\n\n", 'center')
        self.text_field_text.tag_configure("center", justify='center')
        self.scroll.config(command=self.text_field_text.yview)
        self.scroll.pack(side= 'right', fill= 'y')
        self.text_field_text.pack(side = "bottom", fill = 'both', expand=True)
        

        ##Calling the functions that will be capturing CLI output
        
        sys.stdout = StdRedirector(self.text_field_text)
        sys.stderr = StdRedirector(self.text_field_text)

        ##Packs the frames
        
        self.frame_text.pack()
        self.options_text.pack()
        self.frame_buttons.pack()
        self.text_field.pack()

        ##The usual
        
        tkinter.mainloop()

    def gen_new_key(self):

        from encode import generateKey
        print("\nNew key generated...\n")

        return generateKey()
                    
    def encode_program(self):
        from encode import encode
        self.text = self.options_text_entry.get()
        encode(self.text)

    def decode_program(self):

        import decode
        decode.decode()
    
if __name__ == "__main__":
    gui = GUI()
