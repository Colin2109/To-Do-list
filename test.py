import tkinter as tk
from tkinter import messagebox          #tkinter Bibliothek

class TodoApp:
    def __init__(self, root):           #Wird automatisch aufgerufen
        
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("500x400")           #Fenster-Einstellungen
        self.root.resizable(False, False)
        self.root.configure(bg="#f0f4f7")

        self.task = []                          #Liste der Aufgaben
        self.setup_ui()
    
    def setup_ui(self):                         #User-Interface

        title_label = tk.Label(
            self.root,
            text = "To-Do List",
            font = ("Helvetica", 22, "bold"),
            bg = "#f0f4f7",
            fg = "#333"
        )
        title_label.pack(pady=10)


        input_frame = tk.Frame(self.root, bg = "#f0f4f7")
        input_frame.pack(pady=10)

        self.task_entry = tk.Entry(
            input_frame,
            font = ("Helvetica", 12),
            width = 30
        )
        self.task_entry.pack(side="left", padx=(0, 10))

        add_button = tk.Label(
            input_frame,
            text = "Add Task",
            font = ("Helvetica", 11, "bold"),
            bg = "#27ae60",
            fg = "white",
            padx = 15,
            pady = 8
        )
        add_button.pack(side="left", padx=(0, 10))
        add_button.bind("<Button-1>", lambda e: self.add_task())

        list_frame = tk.Frame(self.root, bg="#f0f4f7")
        list_frame.pack(pady=10, fill = "both", expand=True)

        self.task_listbox = tk.Listbox(
            list_frame,
            font = ("Helvetica", 12),
            width = 45,
            height = 10,
            activestyle = "none"
        )
        self.task_listbox.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")

        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)

        self.info_label = tk.Label(
            self.root,
            text = "",
            font = ("Helvetica", 11),
            bg = "#f0f4f7",
            fg = "#007acc"
        )
        self.info_label.pack(pady=5)

        button_frame = tk.Frame(self.root, bg = "#f0f4f7")
        button_frame.pack(pady=10)

        mark_done = tk.Label(
            button_frame,
            text = "Mark as Done",
            font = ("Helvetica", 11, "bold"),
            bg = "#2980b9",
            fg = "white",
            padx = 15,
            pady = 8
        )
        mark_done.pack(side="left", padx = 5)
        mark_done.bind("<Button-1>", lambda e: self.mark_done())

        delete_button = tk.Label(
            button_frame,
            text = "Delete Task",
            font = ("Helvetica", 11, "bold"),
            bg = "#c0392b",
            fg = "white",
            padx = 15,
            pady = 8
        )
        delete_button.pack(side="right", padx=5)
        delete_button.bind("<Button-1>", lambda e: self.delete_task())

        clear_button = tk.Label(
            button_frame,
            text = "Clear All",
            font = ("Helvetica", 11, "bold"),
            bg = "#7f8c8d",
            fg = "white",
            padx = 15,
            pady = 8
        )
        clear_button.pack(side="left", padx = 5)
        clear_button.bind("<Button-1>", lambda e: self.clear_all())

    def refresh_listbox(self):                  #Anzeige aktualisieren
        self.task_listbox.delete(0, tk.END)
        for index, task in enumerate(self.task, start=1):
            status = "✔" if task["done"] else "X"
            display_text = f"{index}.{task['task']} [{status}]"
            self.task_listbox.insert(tk.END, display_text)

    def add_task(self):                                 #Aufgabe hinzufügen
        task_text = self.task_entry.get().strip()
        if not task_text:                               #Leere Eingabe?
            self.info_label.config(text = "Please enter a task first.")
            return
        
        self.task.append({"task" : task_text, "done" : False})  #Task speichern
        self.task_entry.delete(0, tk.END)
        self.info_label.config(text = f"Task '{task_text}' added!")
        self.refresh_listbox()

    def get_selected_index(self):                          #Auswahl überprüfen
        selection = self.task_listbox.curselection()
        if not selection:                                  #Nichts ausgewählt?
            messagebox.showinfo("No Selection", "Please select a task first.")
            return None
        return selection[0]

    def mark_done(self):                        #Aufgabe abhaken
        index = self.get_selected_index()
        if index is None:
            return
        
        self.task[index]["done"] = True
        self.info_label.config(text = "Task marked as done!")
        self.refresh_listbox()

    def delete_task(self):                      #Aufgabe löschen
        index = self.get_selected_index()
        if index is None:
            return

        removed = self.task.pop(index)
        self.info_label.config(text = f"Delete task: {removed['task']}")
        self.refresh_listbox()

    def clear_all(self):                        #Alles löschen
        if not self.task:
            self.info_label.config(text = "No tasks to clear.")
            return
        
        if messagebox.askyesno("Clear All", "Are you sure you want to clear all tasks?"):
            self.task.clear()
            self.refresh_listbox()
            self.info_label.config(text = "All tasks cleared!")

if __name__ == "__main__":      #Programmstart
    root = tk.Tk()              #Funktioniert nur wenn die Datei direkt gestartet wird
    app = TodoApp(root) 
    root.mainloop()