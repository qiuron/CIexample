from utils.utils import Utils

from unittest import TestCase, main

class Testutils(TestCase):

    def setUp(self):
        self.util = Utils()
        
    def test_utils_method_add_raise_ValueError_when_given_argument_is_not_Integer(self):
        pass

    def test_utils_method_add_will_return_the_sum_of_input_arguments(self):
        sum = self.util.add(1, 2)

        self.assertEqual(sum, 3)

    def test_utils_method_minus_will_return_the_minus_of_input_arguments(self):
        ret = self.util.minus(3, 2)

        self.assertEqual(ret, 1)
        

    def test_utils_method_times_will_return_the_times_of_input_arguments(self):
        ret = self.util.times(1, 2)

        self.assertEqual(ret, 2)

    def test_utils_method_divided_will_return_the_divided_of_input_arguments(self):
        ret = self.util.divided(4, 2)

        self.assertEqual(ret, 2)
        
    def test_utils_method_GIVEN_two_int_argument_WHEN_diveded_by_zero_THEN_raise_Error(self):
        with self.assertRaises(Exception) as context:
            ret = self.util.divided(1, 0)

            self.assertTrue('The divided number can not be zero' in context)
        
if __name__ == '__main__':
    main()