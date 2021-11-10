from tkinter import Tk, Canvas, Button, Frame, \
    BOTH, NORMAL, HIDDEN, YES, Menu, X, Y, Text, \
    Entry, END, Label
import re


class Interface:
    def __init__(self):
        self.button1 = None
        self.button2 = None
        self.button3 = None
        self.button4 = None
        self.button5 = None
        self.button_click = 0
        self.frame = None
        self.params_height = None
        self.params_width = None
        self.cell_params = None
        self.entry_height = ''
        self.entry_width = ''
        self.entry_class = ''
        self.solve = None
        self.field = None
        self.r = None
        self.root = None
        self.r_win = None
        self.canv = None
        self.interf_matrix = None
        self.matrix_field = None
        self.field_height = None
        self.field_width = None
        self.screen_height = 0
        self.screen_width = 0
        self.flag_in_or_tor = False
        self.flag = None
        self.r = None

    def make_params(self):
        self.r = Tk()
        self.screen_height = int(self.r.winfo_screenheight())
        self.screen_width = int(self.r.winfo_screenwidth())
        self.r.resizable(0, 0)
        text_enter = Label(self.r, text="Please,\
        select field options and press the button",
                           font="Arial 12")
        text_enter2 = Label(self.r,
                            text="Then close the window,field will be created then",
                            font="Arial 12")
        text_height = Label(self.r, text="Input height", font="Arial 12")
        text_wight = Label(self.r, text="Input width", font="Arial 12")
        text_class = Label(self.r, text="Input thor or inf", font="Arial 12")
        self.entry_height = Entry(self.r, text="test1", width=20)
        self.entry_width = Entry(self.r, text="test2", width=20)
        self.entry_class = Entry(self.r, text="entry_class", width=20)
        self.entry_height.insert(0, '300')
        self.entry_width.insert(0, '300')
        self.entry_class.insert(0, 'thor')
        text_enter.pack()
        text_enter2.pack()
        text_height.pack(side='left', expand=YES, fill=BOTH)
        self.entry_height.pack(side='left', expand=YES, fill=BOTH)
        text_wight.pack(side='left', expand=YES, fill=BOTH)
        self.entry_width.pack(side='left', expand=YES, fill=BOTH)
        text_class.pack(side='left', expand=YES, fill=BOTH)
        self.entry_class.pack(side='left', expand=YES, fill=BOTH)
        convert_button = Button(self.r, text="OK", command=self.convent)
        convert_button.pack(side='right', expand=YES, fill=BOTH)
        self.r.mainloop()

    # \D
    def convent(self):
        template = re.compile(r'\D')
        height_check = re.findall(template, self.entry_height.get())
        wight_check = re.findall(template, self.entry_width.get())
        self.flag = True
        if len(height_check) != 0 or self.entry_height.get() == '':
            self.entry_height.delete(0, END)
            self.flag = False
        if len(wight_check) != 0 or self.entry_width.get() == '':
            self.entry_width.delete(0, END)
            self.flag = False
        if self.entry_class.get() != 'thor' and self.entry_class.get() != 'inf':
            self.entry_class.delete(0, END)
            self.flag = False
        try:
            if self.entry_class.get() == 'thor':
                self.flag_in_or_tor = False
            else:
                self.flag_in_or_tor = True
            self.params_height = int(self.entry_height.get())
            self.params_width = int(self.entry_width.get())
            if int(self.entry_height.get()) < 0:
                self.params_height = 100
            if int(self.entry_width.get()) < 0:
                self.params_width = 100
            self.calculate_sell_size()
        except ValueError:
            pass
        if self.flag:
            self.r.destroy()

    def calculate_sell_size(self):
        estimated_cize = 10
        if self.params_height < estimated_cize:
            estimated_cize = self.params_height
        if self.params_width < estimated_cize:
            estimated_cize = self.params_wight
        while self.params_height % estimated_cize != 0:
            self.params_height += 1
        while self.params_width % estimated_cize != 0:
            self.params_width += 1
        while self.params_height < 200 or self.params_width < 200:
            self.params_height *= 2
            self.params_width *= 2
            estimated_cize *= 2
        self.cell_params = estimated_cize
        if self.params_height <= 0:
            self.params_height = 100
        if self.params_width <= 0:
            self.params_width = 100
        if self.params_height > self.screen_height:
            self.params_height = 3 * self.screen_height // 4
        if self.params_width > self.screen_width:
            self.params_width = self.screen_width // 2

    def make_buttons(self):
        self.button1 = Button(self.frame, text='Next', command=self.step)
        self.button2 = Button(self.frame, text='Clear', command=self.clear)
        self.button3 = Button(self.frame, text='Play', command=self.play)
        # self.button5 = Button(self.frame, text='Back', command=self.back)
        self.button3.grid(row=0, column=0, columnspan=3 * self.cell_params)
        self.button1.grid(row=0, column=3 * self.cell_params, columnspan=3 * self.cell_params)
        # self.button5.grid(row=0, column=6 * self.cell_params, columnspan=3 * self.cell_params)
        self.button2.grid(row=0, column=24 * self.cell_params, columnspan=3 * self.cell_params)

    def step(self):
        field_state = self.field.relive()
        for i in range(len(field_state)):
            for j in range(len(field_state[i])):
                if field_state[i][j]:
                    self.relive_cell(i, j)
                else:
                    self.kill_cell(i, j)
        self.repaint()

    def relive_cell(self, i, j):
        if i > self.field_height - self.cell_params or j > self.field_width - self.cell_params:
            self.canv.itemconfig(self.interf_matrix[i][j],
                                 state=HIDDEN,
                                 tags=('vis', 'to_vis'))
            self.matrix_field[i][j] = [1, 1]
        else:
            self.canv.itemconfig(self.interf_matrix[i][j],
                                 state=NORMAL,
                                 tags=('vis', 'to_vis'))
            self.matrix_field[i][j] = [1, 1]

    def kill_cell(self, i, j):
        if i > self.field_height - self.cell_params or j > self.field_width - self.cell_params:
            self.canv.itemconfig(self.interf_matrix[i][j],
                                 state=HIDDEN,
                                 tags=('hid', 'to_hid'))
            self.matrix_field[i][j] = [0, 0]
        else:
            self.canv.itemconfig(self.interf_matrix[i][j],
                                 state=HIDDEN,
                                 tags=('hid', 'to_hid'))
            self.matrix_field[i][j] = [0, 0]

    def repaint(self):
        for i in range(self.field_height):
            for j in range(self.field_width):
                tag_life = self.matrix_field[i][j][1]
                if self.flag_in_or_tor:
                    if i >= self.field_height - self.cell_params or j >= self.field_width - self.cell_params:
                        self.repaint_inf(tag_life, i, j)
                    else:
                        self.repaint_tor(tag_life, i, j)
                else:
                    self.repaint_tor(tag_life, i, j)

    def repaint_tor(self, tag_life, i, j):
        if tag_life == 0:
            self.canv.itemconfig(self.interf_matrix[i][j],
                                 state=HIDDEN,
                                 tags=('hid', '0'))
            self.matrix_field[i][j] = [0, 0]
        if tag_life == 1:
            self.canv.itemconfig(self.interf_matrix[i][j],
                                 state=NORMAL,
                                 tags=('vis', '0'))
            self.matrix_field[i][j] = [1, 1]

    def repaint_inf(self, tag_life, i, j):
        if tag_life == 0:
            self.matrix_field[i][j] = [0, 0]
            self.canv.itemconfig(self.interf_matrix[i][j],
                                 state=HIDDEN,
                                 tags=('hid', '0'))
        if tag_life == 1:
            self.matrix_field[i][j] = [1, 1]
            self.canv.itemconfig(self.interf_matrix[i][j],
                                 state=HIDDEN,
                                 tags=('vis', '0'))

    def clear(self):
        for i in range(self.field_height):
            for j in range(self.field_width):
                self.canv.itemconfig(self.interf_matrix[i][j],
                                     state=HIDDEN,
                                     tags=('hid', '0'))
                self.matrix_field[i][j] = [0, 0]

    def play(self):
        self.button_click += 1
        if self.button_click % 2 != 0:
            self.play_game()
        else:
            self.root.after_cancel(self.solve)

    def play_game(self):
        self.step()
        self.solve = self.root.after(100, self.play_game)

    def toroid_field(self):
        self.flag_in_or_tor = False

    def infinity_field(self):
        self.flag_in_or_tor = True

    def prepare_field(self):
        x = 0.5
        y = 0.5
        while x < self.params_height + self.cell_params:
            self.canv.create_line(0, x, self.params_width, x)
            x += self.cell_params
        while y < self.params_width + self.cell_params:
            self.canv.create_line(y, 0, y, self.params_height)
            y += self.cell_params
        self.canv.pack(expand=YES, fill=BOTH)
        field_color = "green"
        for i in range(self.field_height):
            for j in range(self.field_width):
                spec_cell = self.canv.create_rectangle(
                    2 + self.cell_params * j,
                    2 + self.cell_params * i,
                    self.cell_params + self.cell_params * j - 2,
                    self.cell_params + self.cell_params * i - 2,
                    fill=field_color,
                    outline="black")
                self.canv.itemconfig(spec_cell, state=HIDDEN, tags=('hid', '0'))
                self.interf_matrix[i][j] = spec_cell

    def close_win(self):
        self.root.destroy()

    def draw_mouse(self, pos):
        pos_y = pos.y // self.cell_params
        pos_x = pos.x // self.cell_params
        try:
            self.canv.itemconfig(self.interf_matrix[pos_y][pos_x],
                                 state=NORMAL,
                                 tags='vis')
            self.matrix_field[pos_y][pos_x] = [1, 1]
        except IndexError:
            pass

    def correction_params(self):
        while self.params_height % self.cell_params != 0:
            self.params_height += 1
        while self.params_wight % self.cell_params != 0:
            self.params_wight += 1
