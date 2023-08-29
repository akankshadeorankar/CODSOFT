import tkinter 
import tkinter .messagebox 
import pickle


window=tkinter.Tk()
window.title("TO-DO-LIST")

def task_adding():
    todo = task_add.get()
    if todo !="":
        todo_box.insert(tkinter.END,todo)
        task_add.delete(0,tkinter.END)
    else:
        tkinter.messagebox.showwarning(title="ATTENTION !!",message="To add a task , plze enter some task")    
        
def task_removing():
    try:
        index_todo=list_frame.curselection()[0]  
        list_frame.delete(index_todo)
    except:
        tkinter.messagebox.showwarning(title="ATTENTION !!",message="TO delete a task, ypu must select a task")  

def task_load():
    try:
        todo_list = pickle.load(open("tasks.dat","rb"))
        list_frame.delete(0,tkinter.END)
        for todo in task_save:
            list_frame.insert(tkinter.END,todo)
    except:
        tkinter.messagebox.showwarning(title="ATTENSTION !!" , message="Connot find task.dat")
        
def task_save():
    todo_list = list_frame.get(0,list_frame.size())
    pickle.dump(todo_list,open("tasks.dat", "wb"))        
        

#the frame in which the whole to do list is coming
#frame function is basically use for making the frame 
#pack is for applying the things on the tkinter window
list_frame  = tkinter.Frame(window)
list_frame.pack()

#for making the box we use the func listbox
todo_box=tkinter.Listbox(list_frame, height =20 , width=50) 
todo_box.pack(side=tkinter.LEFT)

#for the scroller 
scroller = tkinter.Scrollbar(list_frame)
scroller.pack(side=tkinter.RIGHT , fill=tkinter.Y)

#config function is to right inside that
todo_box.config(yscrollcommand=scroller.set)
#scroller.config(command=list_frame.yview)


#function for enter out the task Entry() is the function to write in box
task_add= tkinter.Entry(window,width =70)
task_add.pack()

add_task_button =tkinter.Button(window , text="CLICK TO ADD TASK" , font=("arial",20,"bold"),background="yellow",width=40,command=task_adding)
add_task_button.pack()

remove_task_button =tkinter.Button(window,text="CLICK TO DELETE TASK" ,font=("arial",20,"bold"),background="red",width=40,command=task_removing)
remove_task_button.pack()
load_task_button=tkinter.Button(window,text="CLICK TO LOAD TASK",font=("arial",20,"bold"),background="pink",width=40,command=task_load)
load_task_button.pack()

save_task_button =tkinter.Button(window,text="Click to save",font=("arial",20,"bold"),background="grey",width=40,command=task_save)
save_task_button.pack()

window.mainloop()