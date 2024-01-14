import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    selected_task = listbox.curselection()
    if selected_task:
        listbox.delete(selected_task)

# Tạo cửa sổ
app = tk.Tk()
app.title("To-Do App")

# Tạo và thiết lập các thành phần
entry = tk.Entry(app, width=40)
entry.pack(pady=10)

add_button = tk.Button(app, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(app, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

listbox = tk.Listbox(app, selectmode=tk.SINGLE)
listbox.pack(pady=10)

# Khởi chạy ứng dụng
app.mainloop()
