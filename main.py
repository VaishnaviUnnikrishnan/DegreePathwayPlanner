import tkinter as tk
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class DegreePlanner:
    def __init__(self, root):
        self.root = root
        self.root.title("Degree Pathway Planner")
        self.selected_degree = tk.StringVar()
        self.page1 = ttk.Frame(root)
        self.page1.pack()
        ttk.Label(self.page1, text="Choose Your Degree:").grid(row=0, column=0, pady=10)
        degrees = ["Computer Science", "Fine Arts", "Business Administration", "Literature", "Medicine", "Law",
                   "Fashion Designing", "Architecture", "Aerospace Engineering", "Data Scientist"]
        self.degree_combobox = ttk.Combobox(self.page1, values=degrees, textvariable=self.selected_degree)
        self.degree_combobox.grid(row=0, column=1, pady=10)
        ttk.Button(self.page1, text="Next", command=self.show_pathway).grid(row=1, column=0, columnspan=2, pady=10)
        self.page2 = ttk.Frame(root)
        self.current_page = 1

    def show_pathway(self):
        G = nx.DiGraph()
        if self.selected_degree.get() == "Computer Science":
            G.add_edges_from([
                ("Bachelor's Degree", "Introduction to Programming"),
                ("Introduction to Programming", "Data Structures"),
                ("Introduction to Programming", "Algorithms"),
                ("Data Structures", "Database Systems"),
                ("Algorithms", "Advanced Algorithms"),
                ("Advanced Algorithms", "Machine Learning"),
                ("Database Systems", "Software Engineering"),
                ("Machine Learning", "Artificial Intelligence"),
                ("Software Engineering", "Capstone Project")
            ])
        elif self.selected_degree.get() == "Fine Arts":
            G.add_edges_from([
                ("Bachelor's Degree", "Art History"),
                ("Art History", "Drawing 101"),
                ("Drawing 101", "Painting Techniques"),
                ("Drawing 101", "Sculpture Fundamentals"),
                ("Painting Techniques", "Advanced Painting"),
                ("Sculpture Fundamentals", "Advanced Sculpture"),
                ("Advanced Painting", "Senior Exhibition"),
                ("Advanced Sculpture", "Senior Exhibition")
            ])
        elif self.selected_degree.get() == "Business Administration":
            G.add_edges_from([
                ("Bachelor's Degree", "Principles of Marketing"),
                ("Principles of Marketing", "Financial Accounting"),
                ("Principles of Marketing", "Organizational Behavior"),
                ("Financial Accounting", "Managerial Accounting"),
                ("Organizational Behavior", "Human Resource Management"),
                ("Human Resource Management", "Strategic Management"),
                ("Managerial Accounting", "Financial Management"),
                ("Strategic Management", "Business Ethics"),
                ("Business Ethics", "Capstone Project")
            ])
        elif self.selected_degree.get() == "Literature":
            G.add_edges_from([
                ("Bachelor's Degree", "Introduction to Literature"),
                ("Introduction to Literature", "World Literature"),
                ("Introduction to Literature", "Creative Writing"),
                ("Creative Writing", "Advanced Writing Workshop"),
                ("Creative Writing", "Literary Criticism"),
                ("World Literature", "Comparative Literature"),
                ("Comparative Literature", "Capstone Project")
            ])
        elif self.selected_degree.get() == "Medicine":
            G.add_edges_from([
                ("Bachelor's Degree", "Pre-Medical Studies"),
                ("Pre-Medical Studies", "Anatomy and Physiology"),
                ("Anatomy and Physiology", "Medical Biochemistry"),
                ("Medical Biochemistry", "Cell Biology"),
                ("Cell Biology", "Medical Ethics"),
                ("Cell Biology", "Genetics"),
                ("Genetics", "Medical Microbiology"),
                ("Medical Microbiology", "Clinical Medicine"),
                ("Clinical Medicine", "Residency"),
                ("Residency", "Board Certification")
            ])
        elif self.selected_degree.get() == "Law":
            G.add_edges_from([
                ("Bachelor's Degree", "Introduction to Law"),
                ("Introduction to Law", "Constitutional Law"),
                ("Constitutional Law", "Criminal Law"),
                ("Constitutional Law", "Civil Procedure"),
                ("Criminal Law", "Legal Research and Writing"),
                ("Civil Procedure", "Contracts"),
                ("Contracts", "Torts"),
                ("Torts", "Family Law"),
                ("Legal Research and Writing", "Appellate Advocacy"),
                ("Family Law", "Business Law"),
                ("Business Law", "Capstone Project")
            ])
        elif self.selected_degree.get() == "Fashion Designing":
            G.add_edges_from([
                ("Bachelor's Degree", "Introduction to Fashion Design"),
                ("Introduction to Fashion Design", "Fashion Illustration"),
                ("Fashion Illustration", "Textile Design"),
                ("Textile Design", "Pattern Making"),
                ("Pattern Making", "Garment Construction"),
                ("Textile Design", "Fashion Marketing"),
                ("Fashion Marketing", "Fashion Styling"),
                ("Fashion Styling", "Advanced Fashion Design"),
                ("Garment Construction", "Fashion Merchandising"),
                ("Fashion Merchandising", "Capstone Project")
            ])
        elif self.selected_degree.get() == "Architecture":
            G.add_edges_from([
                ("Bachelor's Degree", "Architectural History"),
                ("Architectural History", "Architectural Design Fundamentals"),
                ("Architectural Design Fundamentals", "Building Materials and Construction"),
                ("Building Materials and Construction", "Architectural Structures"),
                ("Architectural Design Fundamentals", "Architectural Drawing"),
                ("Architectural Drawing", "Advanced Architectural Design"),
                ("Architectural Structures", "Sustainable Architecture"),
                ("Sustainable Architecture", "Urban Planning"),
                ("Urban Planning", "Capstone Project")
            ])
        elif self.selected_degree.get() == "Aerospace Engineering":
            G.add_edges_from([
                ("Bachelor's Degree", "Introduction to Aerospace Engineering"),
                ("Introduction to Aerospace Engineering", "Aerodynamics"),
                ("Introduction to Aerospace Engineering", "Flight Mechanics"),
                ("Aerodynamics", "Aircraft Design"),
                ("Flight Mechanics", "Spacecraft Systems"),
                ("Aircraft Design", "Propulsion Systems"),
                ("Spacecraft Systems", "Aerospace Materials"),
                ("Aerospace Materials", "Capstone Project")
            ])
        elif self.selected_degree.get() == "Data Scientist":
            G.add_edges_from([
                ("Bachelor's Degree", "Introduction to Statistics"),
                ("Introduction to Statistics", "Data Analysis"),
                ("Introduction to Statistics", "Programming Fundamentals"),
                ("Data Analysis", "Machine Learning Basics"),
                ("Programming Fundamentals", "Data Visualization"),
                ("Machine Learning Basics", "Advanced Machine Learning"),
                ("Data Visualization", "Big Data Technologies"),
                ("Advanced Machine Learning", "Deep Learning"),
                ("Big Data Technologies", "Data Science Project"),
                ("Deep Learning", "Capstone Project")
            ])

        self.page2.pack_forget()
        self.page2 = ttk.Frame(self.root)
        self.page2.pack()
        fig, ax = plt.subplots(figsize=(10, 8))
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, arrows=True, node_size=2000, node_color="skyblue", font_size=10,
                font_color="black", font_weight="bold", connectionstyle="arc3,rad=0.1", ax=ax)
        canvas = FigureCanvasTkAgg(fig, master=self.page2)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        ttk.Button(self.page2, text="Quit", command=self.root.destroy).pack()
        self.current_page = 2


if __name__ == "__main__":
    root = tk.Tk()
    app = DegreePlanner(root)
    root.mainloop()
