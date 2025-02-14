from Tkinter import * 
import tkFileDialog ,os
from PIL import Image, ImageTk, ImageDraw, ImageOps, ImageEnhance
import pytesseract, re, itertools
import PIL     #star import not used due to namespace conflict of Image function(present in both Tkinter and PIL)
from os.path import join
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'
def GUI():
    counter=itertools.count()
    class ImageButcher(Tk):
        def __init__(self):
            Tk.__init__(self)
            '''To give the user the option of browsing for an image'''        
            root = Toplevel()
            root.withdraw() #use to hide tkinter window   
            currdir = os.getcwd()
            self.path = tkFileDialog.askopenfilename(parent=root, initialdir=currdir, title='Select an image')
            
            #path here ^ is the path of the image file chosen by the user
            #------------------------------------------------------------
                    
            
            #setting a title and a blank icon:-
            self.title("Image Editor v1")
            #self.wm_iconbitmap(r"C:\Users\Rohan\Pictures\Icons\blank.ico")
            
            #create ui
            f = Frame(self, bd=2)
            self.export = StringVar(self)
            self.exportMenu = OptionMenu(f, self.export,
                                         *('jpeg','png','ico','bmp'))
            self.exportMenu.config(width=7)
            self.export.set('Export As..')
            self.exportMenu.pack(side='left')
            
            #making some Tkinter Buttons:-
            
            self.saveButton = Button(f, text='Save',
                                        command=self.save_image)
            self.saveButton.pack(side='left')
            
            self.brightenButton = Button(f, text='Brighten',
                                        command=self.on_brighten)
            self.brightenButton.pack(side='left')
            
            self.darkenButton = Button(f, text='Darken',
                                        command=self.on_darken)
            self.darkenButton.pack(side='left')
    
            self.mirrorButton = Button(f, text='Mirror',
                                        command=self.on_mirror)
            self.mirrorButton.pack(side='left')
            
            self.grayButton = Button(f, text='Gray',
                                        command=self.on_gray)
            self.grayButton.pack(side='left')
            
            self.get_textButton = Button(f, text='Get Text',
                                        command=self.on_get_text)
            self.get_textButton.pack(side='left')
            
            self.resetButton = Button(f, text='RESET',
                                        command=self.on_reset)
            self.resetButton.pack(side='left')
            f.pack(fill='x')
    
            self.c = Canvas(self, bd=0, highlightthickness=0,
                            width=100, height=100)
            self.c.pack(fill='both', expand=1)
    
            #load image    
            im = Image.open(self.path)
            
            #scaling the image down to a smaller size that can be displayed on the window;
            im.thumbnail((600,600))
            
            #a Tkphoto object being created so that the Image object can be displayed on the window;
            self.tkphoto = ImageTk.PhotoImage(im)
            self.canvasItem = self.c.create_image(0,0,anchor='nw',image=self.tkphoto)
            self.c.config(width=im.size[0], height=im.size[1])
            self.imgoriginal=im
            self.img = im
            self.temp = im.copy() # 'working' image
            
            
            
        #functions that are called when the buttons are pressed;
        def display_image(self, aImage):
            self.tkphoto = pic = ImageTk.PhotoImage(aImage)
            self.c.itemconfigure(self.canvasItem, image=pic)
        def on_mirror(self):
            im = ImageOps.mirror(self.temp)
            self.display_image(im)
            self.temp = im
        def on_brighten(self):
            brightener = ImageEnhance.Brightness(self.temp)
            self.temp = brightener.enhance(1.1) # +10%
            self.display_image(self.temp)
        def on_darken(self):
            brightener = ImageEnhance.Brightness(self.temp)
            self.temp = brightener.enhance(0.9) # -10%
            self.display_image(self.temp)        
        def on_gray(self):
            im = (self.temp).convert("L");
            self.display_image(im)
            self.temp = im
        def on_get_text(self):
            im = (self.temp)
            text=pytesseract.image_to_string(im,lang='eng')
            self.display_image(im)
            if text:
                print text
                textpath=re.sub('\w+\.\w+','',self.path)+r'image_text.txt'
                with open(textpath,'w+') as fo:
                    fo.write(text)
                print 'Image text saved in the current directory as "image_text.txt"'
            else:
                print 'Image font not recognised / Image does not contain text!'
        def on_reset(self):
            im = self.imgoriginal
            self.display_image(im)
            self.temp = im
        def save_image(self):
            try:
                im=self.temp
                imgtype=self.export.get()
                ctext=r'({})'.format(counter.next())
                path=re.sub(r'\.',r'{}.'.format(ctext),self.path)
                path=re.sub(r'\..*$','.'+imgtype,path)
                im.save(path)
                print '\n\nImage saved in Current Directory!!'
            except:
                print 'Unable to save...make sure you change "Export As.." to a file extension of your choice!!'
                
            
            
            
    #initializing app;
    app = ImageButcher()
    #running the app. Runs infinitey until we close the window.
    app.mainloop()

def BATCH_PROCESSING():
    root = Tk()
    root.withdraw()
    # Make it almost invisible - no decorations, 0 size, top left corner.
    root.overrideredirect(True)
    root.geometry('0x0+0+0')
    # Show window again and lift it to top so it can get focus,
    # otherwise dialogs will end up behind the terminal.
    root.deiconify()
    root.lift()
    root.focus_force()
    path = tkFileDialog.askdirectory(parent=root) # Or some other dialog
    root.destroy()
    
     
    FILES=[]
    for dir, subdir, files in os.walk(path):
        for file in files:
            FILES.append(join(dir, file))
    
    def gettype(s):return s[s.index('.')+1:]
    images=[]
    for f in FILES:
        if gettype(f) in ['png','jpg','jpeg','bmp']:
            images.append(f)
    print 'You have chosen the directory:',path
    print 'The images in this directory are:\n','\n'.join(images)
    #--------------OPERATIONS ON THE IMAGES------------------------
    
    print '\n\n'
    #the menu:
    print 'WELCOME TO THE TEXT BASED MODE!This mode is used for batch processing of images.'
    print '''The options are:
             1) Making the images gray.
             2) Resizing all the images to a specified value.
             3) Converting all the images to png.
             4) Converting all images to jpg
             5) Blurring the image
             6) Rotating the image clockwise by 90 degrees
            Press "q" to quit! '''
    
    def make_gray(imageobject):
        return imageobject.convert("L")
    def make_png(imagepath):
        return imagepath[:imagepath.index('.')]+'.png'
    def make_jpg(imagepath):
        return imagepath[:imagepath.index('.')]+'.jpg'
    def resize_image(imageobject,x,y):
        return imageobject.resize((x,y))
    def blur_image(imageobject,radius=2):
        return imageobject.filter(PIL.ImageFilter.BLUR)
    def rotate_image(imageobject):
        return imageobject.rotate(-90)
    while True:
        option=raw_input('Enter the desired option(1-6): ')
        if option=='q':break
        try:
            option=int(option)
            if option>6: raise ZeroDivisionError
        except:
            print 'Enter a valid option!'
            continue
        if option==2:size=map(int,(raw_input('Enter a,b where (a x b) is the desired size of image:')).split(','))
        for imagepath in images:
            im=PIL.Image.open(imagepath)
            location=imagepath
            if option==1:im=make_gray(im)
            elif option==2:im=resize_image(im,*size) #unpacking  the size list and passing it to resize function
            elif option==3:location=make_png(imagepath)
            elif option==4:location=make_jpg(imagepath)
            elif option==5:im=blur_image(im)
            elif option==6: im=rotate_image(im)
            im.save(location)
        control=raw_input('The desired option has been carried out successfully. Do you want to continue?(y/n): ')
        if control=='n':break


print '''WELCOME TO THE IMAGE EDITING APPLICATION!!
        What do you want to do?
            1) Edit a single image (GUI)
            2) Edit a batch of images (text based)'''
while True:
    option=raw_input('Enter the desired option(1/2): ')
    if option=='1': GUI()
    elif option=='2': BATCH_PROCESSING()
    elif option=='q':break
    else:
        print 'Enter the correct option or press "q" to quit'
