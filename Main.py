from Methods import Enter_number as enter
from Methods import Create_list_with_positive_real_nums as real
from Methods import Fractional_part as fract
from Methods import Diff_between_max_min as difference
import os

os.system('cls')

length = enter('Введите количество элементов: ')
max = enter('Введите максимальное значение элемента: ')
my_list = real(length, max)
print(my_list)

my_list = fract(my_list)
print(my_list)

diff = difference(my_list)
print(f'Разница между максимальным и минимальным значеним дробной части элементов равна {diff}')