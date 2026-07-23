import tkinter as tk

root = tk.Tk()
root.attributes('-fullscreen', True, '-topmost', True)
root.config(bg='#abcdef')
root.attributes('-transparentcolor', '#abcdef')

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

canvas = tk.Canvas(root, width=screen_width, height=screen_height, bg='#abcdef', highlightthickness=0)
canvas.pack()

center_x = screen_width // 2
center_y = screen_height // 2

# رسم الخطوط باللون الأحمر وسماكة 2 بكسل
canvas.create_line(center_x, 0, center_x, screen_height, fill="red", width=2)
canvas.create_line(0, center_y, screen_width, center_y, fill="red", width=2)

# إغلاق البرنامج عند الضغط على زر Esc في لوحة المفاتيح
root.bind('<Escape>', lambda e: root.destroy())

root.mainloop()
