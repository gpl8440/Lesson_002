#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['мама', 'папа', 'жена', 'дочь', 'тётя']


# список списков приблизителного роста членов вашей семьи
my_family_height = [
    # ['имя', рост],
    ['мама',164],
    ['папа',178],
    ['жена',165],
    ['дочь',58],
    ['тётя',172],
]


# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

print('Рост: '+my_family[1]+' - ', my_family_height[1][1], 'см.')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

sum_hight = 0
sum_hight += my_family_height[0][1]
sum_hight += my_family_height[1][1]
sum_hight += my_family_height[2][1]
sum_hight += my_family_height[3][1]
sum_hight += my_family_height[4][1]

print('Общий рост моей семьи -', sum_hight, 'см.')