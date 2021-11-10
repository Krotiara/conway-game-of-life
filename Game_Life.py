from tkinter import Tk, Canvas, Frame, BOTH, YES
import class_Field
import class_Interface

if __name__ == '__main__':
    ints = class_Interface.Interface()
    ints.make_params()
    ints.root = Tk()
    ints.root.resizable(0, 0)
    try:
        ints.field_width = ints.params_width // ints.cell_params
        ints.field_height = ints.params_height // ints.cell_params
        if ints.params_height > ints.screen_height:
            ints.params_height = ints.screen_height
        if ints.params_width > ints.screen_width:
            ints.params_width = ints.screen_width
        config_string = "{0}x{1}".format(21 * ints.params_width // 20, 12 * ints.params_height // 11 + ints.cell_params)
        ints.root.geometry(config_string)
        ints.canv = Canvas(ints.root, width=ints.params_width - 2 * ints.cell_params, height=ints.params_height,
                           bg='lightblue')
        if ints.flag_in_or_tor:
            ints.field_height = ints.field_height + ints.cell_params
            ints.field_width = ints.field_width + ints.cell_params
            ints.matrix_field = [[[0, 0]] * ints.field_width for i in range(ints.field_height)]
            ints.interf_matrix = [[[0, 0]] * ints.field_width for i in range(ints.field_height)]
        else:
            ints.matrix_field = [[[0, 0]] * ints.field_width for i in range(ints.field_height)]
            ints.interf_matrix = [[[0, 0]] * ints.field_width for i in range(ints.field_height)]
        ints.prepare_field()
        ints.field = class_Field.Field(ints.field_width, ints.field_height, ints.matrix_field)
        ints.field.flag_field = ints.flag_in_or_tor
        ints.frame = Frame(ints.root)
        ints.make_buttons()
        ints.frame.pack(side='bottom', expand=YES, fill=BOTH)
        ints.canv.bind('<Button-1>', ints.draw_mouse)
        ints.canv.bind('<ButtonPress>', ints.draw_mouse)
        ints.root.mainloop()
    except TypeError:
        pass
