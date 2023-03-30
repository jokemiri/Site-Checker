import tkinter as tk
import urllib.request

class SiteCheckerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Site Checker")
        master.geometry("335x250") #dimensions
        master.resizable(0, 0) #resizability
        master.configure(bg='#326273') #background    
        master.iconbitmap('icon.ico')# Set window icon
# #window icon
#         icon_image = tk.PhotoImage(file='icon.png')
#         master.iconphoto(False, icon_image)
        # Create labels and entry fields for URLs
        self.url_labels = []
        self.url_entries = []
        for i in range(4):
            label = tk.Label(master, text="Site " + str(i+1) + ":",fg='white', bg='#326273')
            label.grid(row=i, column=0, padx=5, pady=5)
            self.url_labels.append(label)

            entry = tk.Entry(master)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.url_entries.append(entry)

        # Create button to check sites
        self.check_button = tk.Button(master, text="Check Sites", command=self.check_sites)
        self.check_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

        # Create text area to display results
        self.result_text = tk.Text(master, height=4, width=40)
        self.result_text.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

    def check_sites(self):
        results = []
        for i in range(4):
            url = self.url_entries[i].get()
            if url == '':
                results.append("Site " + str(i+1) + ": No URL entered")
            else:
                try:
                    urllib.request.urlopen(url)
                    results.append("Site " + str(i+1) + ": OK")
                except:
                    results.append("Site " + str(i+1) + ": Error")

        # Display results in text area
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "\n".join(results))

# Create GUI
root = tk.Tk()
site_checker = SiteCheckerGUI(root)
root.mainloop()
