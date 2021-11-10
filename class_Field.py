import class_Interface


class Field:
    def __init__(self, field_wight, field_height, matrix_field):
        self.flag_field = None
        self.field_wgt = field_wight
        self.field_hgt = field_height
        self.m_field = matrix_field
        self.cell_tag = None
        self.relive()
        self.solve_life_death(i=0, j=0, i_near=0, j_near=0)
        self.new_tag = ''

    def relive(self):
        field_state = [[False] * int(self.field_wgt) for i in range(int(self.field_hgt))]
        for i in range(int(self.field_hgt)):
            for j in range(int(self.field_wgt)):
                n_bors = 0
                for i_near in range(-1, 2):
                    for j_near in range(-1, 2):
                        if self.solve_life_death(i, j, i_near, j_near):
                            n_bors += 1
                self.new_tag = self.m_field[i][j][0]
                field_state[i][j] = n_bors == 3 or (n_bors == 2 and self.new_tag == 1)
        return field_state

    def solve_life_death(self, i, j, i_near, j_near):
        if not self.flag_field:
            cell_tag = self.m_field[(i + i_near) % len(self.m_field)][(j + j_near) % len(self.m_field[0])]
            return cell_tag[0] == 1 and any((i_near, j_near))
        if self.flag_field:
            if i + i_near < 0 or i + i_near >= self.field_hgt or j + j_near < 0 or j + j_near >= self.field_wgt:
                return False
            else:
                cell_tag = self.m_field[i + i_near][j + j_near]
                if cell_tag[0] == 1 and (i_near != 0 or j_near != 0):
                    return True
                return False
