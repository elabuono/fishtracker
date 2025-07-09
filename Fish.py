import tkinter as tk
from PIL import Image, ImageTk

import tkinter as tk
from PIL import Image, ImageTk

class GridApp:
    def __init__(self, root, rows=5, cols=8, image_path="fishies/fish.png"):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.image_path = image_path
        self.cells = {}
        self.highlight_splits = [
            [(0, 6), (0, 7), (2, 0), (2, 3), (3, 6)], # July
            [(0, 0)] # Test
        ]

        self.current_step = 0
        self.image_refs = []
        self.load_image()
        self.create_grid()
        self.create_button()

    def load_image(self):
        img = Image.open(self.image_path)
        img = img.resize((90, 60))
        self.photo = ImageTk.PhotoImage(img)

    def create_grid(self):
        for r in range(self.rows):
            for c in range(self.cols):
                frame = tk.Frame(self.root, borderwidth=1, relief="solid", width=70, height=90, bg="white")
                frame.grid(row=r, column=c, padx=1, pady=1)

                label_text = tk.Label(frame, text=f"R{r+1}C{c+1}", bg="white")
                label_text.pack()

                label_img = tk.Label(frame, image=self.photo, bg="white")
                label_img.pack()

                self.cells[(r, c)] = (frame, label_text, label_img)

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


