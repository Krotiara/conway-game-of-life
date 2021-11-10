import class_Field
import unittest


class Test(unittest.TestCase):
    def testOvercrowding(self):
        matrix_field = [[[1, 1], [1, 1], [1, 1]],
                        [[1, 1], [1, 1], [1, 1]],
                        [[1, 1], [1, 1], [1, 1]]]
        field = class_Field.Field(3, 3, matrix_field)
        field.flag_field = False
        result = field.relive()
        assert_answer = [[False, False, False], [False, False, False], [False, False, False]]
        self.assertEqual(assert_answer, result)

    def testStatic_figure(self):
        matrix_field = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                        [[0, 0], [0, 0], [0, 0], [1, 1], [1, 1]],
                        [[0, 0], [0, 0], [0, 0], [1, 1], [1, 1]]]
        field = class_Field.Field(5, 5, matrix_field)
        field.flag_field = False
        result = field.relive()
        assert_answer = [[False, False, False, False, False],
                         [False, False, False, False, False],
                         [False, False, False, False, False],
                         [False, False, False, True, True],
                         [False, False, False, True, True]]
        self.assertEqual(assert_answer, result)

    def testMove_figure(self):
        matrix_field = [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                        [[0, 0], [0, 0], [1, 1], [1, 1], [0, 0]],
                        [[0, 0], [0, 0], [0, 0], [0, 0], [0, 0]],
                        [[0, 0], [1, 1], [0, 0], [1, 1], [0, 0]],
                        [[0, 0], [0, 0], [0, 0], [1, 1], [0, 0]]]
        field = class_Field.Field(5, 5, matrix_field)
        field.flag_field = False
        result = field.relive()
        assert_answer = [[False, False, True, True, False],
                         [False, False, False, False, False],
                         [False, False, False, True, False],
                         [False, False, True, False, False],
                         [False, False, True, False, False]]
        self.assertEqual(assert_answer, result)


if __name__ == '__main__':
    unittest.main()
