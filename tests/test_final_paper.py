'''Unit-тесты для final_paper.py'''

import unittest
import final_paper

class TestSorts(unittest.TestCase):
    '''Тестирование сортировок'''

    def __init__(self, *args, **kwargs):
        super(TestSorts, self).__init__(*args, **kwargs)
        self.test_lst = [9, -2, 0, 1, 0]
        self.result_lst = [-2, 0, 0, 1, 9]
        self.bubble_sort = final_paper.bubble_sort
        self.pyramid_sort = final_paper.pyramid_sort
        self.merge_sort = final_paper.merge_sort
        self.quick_sort = final_paper.quick_sort


    def test_buble_sort(self):
        '''Тест сортировки пузырьком'''

        self.assertEqual(self.bubble_sort(self.test_lst),
                        self.result_lst)


    def test_pyramid_sort(self):
        '''Тест пирамидальной сортировки'''

        self.assertEqual(self.pyramid_sort(self.test_lst),
                        self.result_lst)


    def test_merge_sort(self):
        '''Тест сортировки слиянием'''

        self.assertEqual(self.merge_sort(self.test_lst),
                        self.result_lst)

    def test_quick_sort(self):
        '''Тест быстрой сортировки'''

        self.assertEqual(self.quick_sort(self.test_lst),
                        self.result_lst)

if __name__ == "__main__":
    unittest.main()
