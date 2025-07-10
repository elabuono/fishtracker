import tkinter as tk
from PIL import Image, ImageTk

import tkinter as tk
from PIL import Image, ImageTk

class GridApp:
    def __init__(self, root, rows=5, cols=8):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.cells = {}
        self.highlight_splits = [
            [(4, 1), (4, 0), (3, 2), (3, 3), (1, 3), (1, 0), (0, 1), (1, 7)], # June 1st 9AM
            [(3, 4), (3, 5), (2, 0), (0, 6), (0, 7)], # June 1st 3AM
            [(4, 3), (4, 5), (4, 6), (4, 7), (3, 0)], # August 31st 11:58pm - September with Rain
            [(3, 1), (2, 3), (3, 6), (1, 6), (3, 7), (0, 7), (4, 2), (4, 4)], # July 1st 4AM
            [(4, 4), (2, 2), (1, 1), (0, 3), (2, 7), (1, 4), (0,0), (2, 1), (1, 5), (0, 5), (0, 4), (0, 2)], # February 1st 4AM
            [()] # March 1st 4AM

        ]
        self.fish_names = [
            "Crucian Carp", "Brook Trout", "Carp", "Koi", "Barbel Steed", "Dace", "Catfish", "Giant Catfish",
            "Pale Chub", "Bitterling", "Loach", "Bluegill", "Small Bass", "Bass", "Large Bass", "Giant Snakehead",
            "Eel", "Freshwater Goby", "Pond Smelt", "Sweetfish", "Cherry Salmon", "Rainbow Trout", "Large Char", "Stringfish",
            "Salmon", "Goldfish", "Popeyed Goldfish", "Guppy", "Angelfish", "Piranha", "Arowana", "Arapaima",
            "Crawfish", "Frog", "Killifish", "Jellyfish", "Sea Bass", "Red Snapper", "Barred Knifejaw", "Coelacanth"
        ]


        self.current_step = 0
        self.image_refs = []
        self.create_grid()
        self.create_button()

    def create_grid(self):
        current_fish = 0
        for r in range(self.rows):
            for c in range(self.cols):
                frame = tk.Frame(self.root, borderwidth=1, relief="solid", width=100, height=100, bg="white")
                frame.grid(row=r, column=c, padx=1, pady=1)
                frame.grid_propagate(False)

                img_path = "fishies/" + self.fish_names[current_fish].replace(" ", "") + ".png"
                img = Image.open(img_path).convert("RGBA")
                img = img.resize((75, 75), Image.Resampling.LANCZOS)
                photo = ImageTk.PhotoImage(img)
                self.image_refs.append(photo)

                label_img = tk.Label(frame, image=photo, bg="white")
                label_img.place(relx=0.5, rely=0.18, anchor="n")

                label_text = tk.Label(
                    frame,
                    text=self.fish_names[current_fish],
                    bg="white",
                    wraplength=90,
                    justify="center",
                    font=("Arial", 9)
                )
                label_text.place(relx=0.5, rely=0.05, anchor="n")

                self.cells[(r, c)] = (frame, label_text, label_img)
                current_fish += 1

    def create_button(self):
        button = tk.Button(self.root, text="Next", command=self.highlight_next)
        button.grid(row=self.rows, column=0, columnspan=self.cols, sticky="we")

    def highlight_next(self):
        # Clear all cells
        for (frame, label_text, label_img) in self.cells.values():
            frame.config(bg="white")
            label_text.config(bg="white")
            label_img.config(bg="white")

        # Get current step cells to highlight
        current_cells = self.highlight_splits[self.current_step]

        # Highlight selected cells
        for (r, c) in current_cells:
            frame, label_text, label_img = self.cells[(r, c)]
            frame.config(bg="yellow")
            label_text.config(bg="yellow")
            label_img.config(bg="yellow")

        # Move to next step
        self.current_step = (self.current_step + 1) % len(self.highlight_splits)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Fish Tracker")
    app = GridApp(root)
    root.mainloop()


