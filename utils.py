import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.messagebox import showinfo
import webbrowser
import time 
import pickle as pkl
from tqdm.tk import tqdm

x, y, filepath1 = '', '', ''

class NidlemanVunshAlgo():
    
    @staticmethod
    def my_range(*args):
        assert len(args) > 0 and len(args) <= 3, "Неверный формат аргументов"
        
        if len(args) == 1:
            start = 0
            stop = args[0]
            step = 1
        elif len(args) == 2:
            start = args[0]
            stop = args[1]
            step = 1
        elif len(args) == 3:
            start = args[0]
            stop = args[1]
            step = args[2]

        i = start
        while i < stop:
            yield i
            i += step
    
    @staticmethod
    def s(a, b, match_penalty, mismatсh_penalty):
        if a == b:
            return match_penalty
        return mismatсh_penalty
    

    def count_matrix(self, x, y, gap_penalty, match_penalty, mismatсh_penalty, pbar):
        #if pbar != None:
        pbar._tk_window.deiconify()
        iter_num = len(x)*len(y)
        pbar.reset(total=iter_num)
            
        F = [[((i + j) * gap_penalty if i*j == 0 else 0) for j in range(len(y) + 1)] for i in range(len(x) + 1)]
        
        for i in self.my_range(1, len(x) + 1):
            for j in self.my_range(1, len(y)+ 1):
                F[i][j] = min(F[i-1][j-1] + self.s(x[i-1], y[j-1], match_penalty, mismatсh_penalty), 
                              F[i][j-1] + gap_penalty, F[i-1][j] + gap_penalty)
                #if pbar != None:
                pbar.update(1)
                if iter_num < 500:
                    time.sleep(2 / iter_num)
                
                    
        #if pbar != None:
        pbar._tk_window.withdraw()
            
        return F

    
    
    def Nidleman_Vunsh(self, x, y, mismatсh_penalty = 2, match_penalty = -1, pbar=None):
        gap_penalty = 0.5 * mismatch_penalty 
        F = self.count_matrix(x,y, gap_penalty, match_penalty, mismatсh_penalty, pbar)
        self.F = F
        aligment_x = ''
        aligment_y = ''
        i = len(x)
        j = len(y)
        while (i > 0 or j > 0):

            if (F[i][j]== (F[i - 1][j - 1] + self.s(x[i - 1], y[j - 1],  match_penalty, mismatсh_penalty)) and i > 0 and j > 0):
                aligment_x = x[i - 1] + aligment_x
                aligment_y = y[j - 1] + aligment_y
                i -= 1
                j -= 1

            elif (F[i][j] == (F[i - 1][j]+ gap_penalty) and i > 0 ):
                aligment_x = x[i - 1] + aligment_x
                aligment_y = "_" + aligment_y
                i -= 1


            elif (F[i][j] == (F[i][j - 1] + gap_penalty) and j > 0):
                aligment_y = y[j - 1] + aligment_y
                aligment_x = "_" + aligment_x
                j -= 1

            else:
                messagebox.showinfo('Информационное окно', 'Ошибка!')
                break

        return aligment_y, aligment_x
    
    def __repr__(self):
        return "Class of Nidleman Vunsh algorithm"
    


    
class App(tk.Tk):
    def __init__(self):
        super().__init__()
    
        self.color = 'lavenderblush'
        self.font = ("Helvetica Bold", 14)
        self.max_len_to_show = 30

        # configure the root window
        self.title('Наш супер код Нильдмана-Вунша')
        self.geometry('800x400')

        # label
        self.label = ttk.Label(self, text='Щас будем красиво делать выравнивание строк', font=("Arial", 17))
        self.label.pack()

        # buttons
        
        self.button3 = ttk.Button(self, text='Нажмите сюда')
        self.button3['command'] = self.destroy
        self.button3.pack()
        
        self.nv = NidlemanVunshAlgo()
        
        
    def config_labels(self):
        self.lbl1  = Label(self.window, bg = self.color, text="Последовательность 1:", font=self.font)
        self.lbl2  = Label(self.window, bg = self.color, text="Последовательность 2:", font=self.font)
        self.lbl3  = Label(self.window, bg = self.color, text=" ", font=self.font)
        self.lbl4  = Label(self.window, bg = self.color, text=" ", font=self.font)
        self.lbl5  = Label(self.window, bg = self.color, text="Введите последовательность 1:") 
        self.lbl6  = Label(self.window, bg = self.color, text="Введите последовательность 2:")
        self.lbl7  = Label(self.window, bg = self.color, text="или", font=self.font)
        self.lbl8  = Label(self.window, bg = self.color, text="или", font=self.font)
        self.lbl9  = Label(self.window, bg = self.color, text=" ", font=self.font)
        self.lbl10 = Label(self.window, bg = self.color, text=" ", font=self.font)
        self.lbl11 = Label(self.window, bg = self.color, text=" ", font=self.font)
        self.lbl12 = Label(self.window, bg = self.color, text=" ", font=self.font)
        self.lbl13 = Label(self.window, bg = self.color, text=" ", font=self.font)
        self.lbl14 = Label(self.window, bg = self.color, text=" ", font=self.font)  
       
        self.lbl1.grid(column=0, row=15) 
        self.lbl2.grid(column=0, row=16)
        self.lbl3.grid(column=0, row=4)
        self.lbl4.grid(column=0, row=5)
        self.lbl5.grid(column=0, row=3)
        self.lbl6.grid(column=0, row=12)
        self.lbl7.grid(column=0, row=2)
        self.lbl8.grid(column=0, row=11)
        self.lbl9.grid(column=0, row=13)
        self.lbl10.grid(column=0, row=14)
        self.lbl11.grid(column=0, row=19)
        self.lbl12.grid(column=0, row=20)
        self.lbl13.grid(column=0, row=17)
        self.lbl14.grid(column=0, row=18)
        
      
    def config_buttons(self):
        btn1 = Button(self.window, bg = 'lemonchiffon', text="Загрузить последовательность 1", command=self.clicked1)
        btn2 = Button(self.window, bg = 'lemonchiffon', text="Загрузить последовательность 2", command=self.clicked2)
        btn3 = Button(self.window, bg = 'palegreen', text="Выровнять", command=self.clicked3)
        btn4 = Button(self.window, bg = 'paleturquoise', text="Загрузить ввод 1", command=self.clicked4)
        btn5 = Button(self.window, bg = 'paleturquoise', text="Загрузить ввод 2", command=self.clicked5)

        btn1.grid(column=0, row=0)
        btn2.grid(column=0, row=10)
        btn3.grid(column=1, row=16)
        btn4.grid(column=2, row=3)
        btn5.grid(column=2, row=12)
        
        
    def config_txt(self):
        self.txt1 = Entry(self.window, width=40)
        self.txt2 = Entry(self.window, width=40)       

        self.txt1.grid(column=1, row=3)  
        self.txt2.grid(column=1, row=12)
        
        
    @staticmethod
    def reader(file_path):
        with open(file_path) as file:
            for line in file:
                if all(char in 'AGTCN\n' for char in sorted(set(line))):
                    yield line.strip()
        
          
#     def bar(self, progress): 
#         progress['value'] = 0
#         self.window.update_idletasks() 
#         time.sleep(0.5) 
        
#         progress['value'] = 20
#         self.window.update_idletasks() 
#         time.sleep(0.7) 

#         progress['value'] = 40
#         self.window.update_idletasks() 
#         time.sleep(0.2) 

#         progress['value'] = 50
#         self.window.update_idletasks() 
#         time.sleep(1) 

#         progress['value'] = 60
#         self.window.update_idletasks() 
#         time.sleep(0.4) 

#         progress['value'] = 80
#         self.window.update_idletasks() 
#         time.sleep(1)
        
#         progress['value'] = 100
#         time.sleep(0.5)
#         progress.destroy()
        
     
    def clicked1(self):  
        global x, filepath1
        filepath1 = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*"),("fasta","*.fa*")))
        r1 = self.reader(filepath1)
        for i in r1:
            x += i
        if len(x) < self.max_len_to_show:
            self.lbl1.configure(text= ("Первая последовательность: "+x))
        else:
            self.lbl1.configure(text= ("Первая последовательность слишком велика для отображения"))
    
    
    def clicked2(self):  
        filepath2 = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*"),("fasta","*.fa*")))
        global y
        r2 = self.reader(filepath2)
        for i in r2:
            y += i
        if len(x) < self.max_len_to_show:
            self.lbl2.configure(text= ("Вторая последовательность: "+y))
        else:
            self.lbl2.configure(text= ("Вторая последовательность слишком велика для отображения"))
        
        
    def clicked3(self):
             
#         progress = ttk.Progressbar(self.window, orient = HORIZONTAL, 
#               length = 500, mode = 'indeterminate')
        
#         progress.grid(column=0, row=19)
        #self.bar(progress)
        
        if x != 0 and y != 0:
          #  progress.start()
            y_done, x_done = self.nv.Nidleman_Vunsh(x, y, pbar=self.pbar)
          #  progress.stop()
          #  progress.destroy()
            if len(x_done) < self.max_len_to_show:
                self.lbl12.configure(text = (' '+f'{x_done} \n{y_done}'))
                self.lbl11.configure(text = "Выравнивание:")
                draw_button = ttk.Button(self.window, text='Показать матрицу', command=self.draw_matrix)
                draw_button.grid(column=1, row=20)
                
            else:
                self.lbl11.configure(text = "Последовательность слишком велика для отображения.\n")   
                
            global filepath1
            if filepath1 != '':
                end = filepath1.rfind('.')               
            else:
                end = min(10, len(x))
                filepath1 = x[:end]
                
            save_filepath = filepath1[:end] + '_alligned.txt'
            
            with open(save_filepath, 'w') as file:
                file.write(f'ALLIGNED_SEQ\n{x_done}\n{y_done}')
                
            matrix_path = f'{filepath1[:end]}_matrix.pkl'
            
            with open(matrix_path, 'wb+') as file:
                pkl.dump([self.nv.F, x, y], file)
                
            self.save_filepath = save_filepath
            self.matrix_path = matrix_path
             
        else:
            messagebox.showinfo('Информационное окно', 'Ошибка!')
            print(x,y)
        
        
    def clicked4(self):  
        global x
        x = self.txt1.get()
        if len(x) < self.max_len_to_show:
            self.lbl1.configure(text= (" Последовательность 1: "+str(x)))
        else:
            self.lbl1.configure(text= ("Последовательность слишком велика для отображения"))


    def clicked5(self):  
        global y
        y = self.txt2.get()
        if len(y) < self.max_len_to_show:
            self.lbl2.configure(text= (" Последовательность 2: "+str(y)))
        else:
            self.lbl2.configure(text= ("Последовательность слишком велика для отображения"))
            
        
    def draw_matrix(self):
        global x, y
        matrix_window = Tk() 
        matrix_window.title("Матрица расстояний")   
        matrix_window.configure(bg=self.color) 
        matrix = self.nv.F
        rows = len(matrix)
        cols = len(matrix[0])
        
        for i, item in enumerate(x):
            label = tk.Label(matrix_window, text=item, bg = self.color)
            label.grid(row=i+2, column=0)
        for i, item in enumerate(y):
            label = tk.Label(matrix_window, text=item, bg = self.color)
            label.grid(row=0, column=i+2)
        
        for i in range(rows):
            for j in range(cols):
                cell_value = matrix[i][j]
                label = tk.Label(matrix_window, text=str(cell_value), bg = self.color)
                label.grid(row=i+1, column=j+1)
                
        matrix_window.mainloop()
        
        
        
    @staticmethod    
    def button_clicked():
        pass
        
    @staticmethod    
    def callback(url):
        pass
        

    def button_clicked_meme(self):
        pass
        
    def main(self): 
        
        self.window = Tk() 
 
        self.window.title("Алгоритм Нидльмана-Вунша")  
        self.window.geometry('1000x600')  
        self.window.configure(bg=self.color)
        
        self.config_labels()
        self.config_buttons()
        self.config_txt()
        
        self.pbar = tqdm(tk_parent=self.window)
        self.pbar._tk_window.withdraw()
 
        self.window.mainloop()  
