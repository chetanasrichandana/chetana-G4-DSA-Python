import tkinter
import random

class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.canvas = tkinter.Canvas(root, width = 600, height = 400) #creation of canvas animation 
        self.canvas.pack() #organizes vertical and horizontal boxes within a frame
        self.array = [random.randint(10, 400) for _ in range(50)]
        self.sorting_array()

    def sorting_array(self):
        self.canvas.delete("all")
        canvas_width = 600
        canvas_height = 400
        x_width = canvas_width / (len(self.array) + 1)
        offset = 4
        spacing = 2
        normalized_data = [i / max(self.array) for i in self.array] # organizes data
        for i, height in enumerate(normalized_data):
            x0 = i * x_width + offset + spacing
            y0 = canvas_height - height * 390
            x1 = (i + 1) * x_width + offset
            y1 = canvas_height
            self.canvas.create_rectangle(x0, y0, x1, y1, fill = "#78A7FF")
        self.root.update_idletasks()

    def bubble_sort(self):
        n = len(self.array)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.array[j] > self.array[j+1]:
                    self.array[j], self.array[j+1] = self.array[j+1], self.array[j]
                    self.draw_array()
                    self.root.update()
                    self.root.after(10)

    def quick_sort(self):
        self.quick_sort_helper(0, len(self.array) - 1)
        self.sorting_array()

    def quick_sort_helper(self, low, high):
        if low < high:
            pi = self.partition(low, high)
            self.quick_sort_helper(low, pi-1)
            self.quick_sort_helper(pi+1, high)
            self.sorting_array()
            self.root.update()
            self.root.after(10)

    def insertion_sort(self):
        for i in range(1, len(self.array)):
            key = self.array[i]
            j = i-1
            while j >= 0 and key < self.array[j]:
                self.array[j + 1] = self.array[j]
                j -= 1
            self.array[j + 1] = key
            self.draw_array()
            self.root.update()
            self.root.after(10)

    def merge_sort(self):
        self.merge_sort_helper(0, len(self.array) - 1)
        self.sorting_array()

    def merge_sort_helper(self, low, high):
        if low < high:
            mid = (low + high) // 2
            self.merge_sort_helper(low, mid)
            self.merge_sort_helper(mid + 1, high)
            self.merge(low, mid, high)
            self.sorting_array()
            self.root.update()
            self.root.after(10)

    def merge(self, low, mid, high):
        left = self.array[low:mid + 1]
        right = self.array[mid + 1:high + 1]
        i = j = 0
        k = low
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                self.array[k] = left[i]
                i += 1
            else:
                self.array[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            self.array[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            self.array[k] = right[j]
            j += 1
            k += 1


    def partition(self, low, high):
        pivot = self.array[high]
        i = low - 1
        for j in range(low, high):
            if self.array[j] < pivot:
                i += 1
                self.array[i], self.array[j] = self.array[j], self.array[i]
                self.sorting_array()
                self.root.update()
                self.root.after(10)
        self.array[i+1], self.array[high] = self.array[high], self.array[i+1]
        self.sorting_array()
        self.root.update()
        self.root.after(10)
        return i + 1

root = tkinter.Tk()
visualizer = SortingVisualizer(root)
button_frame = tkinter.Frame(root)
button_frame.pack()
bubble_sort_button = tkinter.Button(button_frame, text="Bubble Sort", command=visualizer.bubble_sort)
bubble_sort_button.pack(side= tkinter.LEFT)
quick_sort_button = tkinter.Button(button_frame, text="Quick Sort", command=visualizer.quick_sort)
quick_sort_button.pack(side=tkinter.LEFT)
insertion_sort_button = tkinter.Button(button_frame, text="Insertion Sort", command=visualizer.insertion_sort)
insertion_sort_button.pack(side=tkinter.LEFT)
merge_sort_button = tkinter.Button(button_frame, text="Merge Sort", command=visualizer.merge_sort)
merge_sort_button.pack(side=tkinter.LEFT)             
root.mainloop()
