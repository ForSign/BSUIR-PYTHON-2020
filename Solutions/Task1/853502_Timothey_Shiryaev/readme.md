Python 3.7.4 

1. Создается словарь на вход которого поступает список слов, считанных из файла TexForLab.txt.
   Слова выбираются из предложения через регулярное выражение (только буквы).
   После используется метод колекций Counter для заполнения словаря в формате: Word - Counts, - после чего выводится на экран.

2. Используя все тот же Counter обновляем словарь и выводим 10 самых повторяющихся его значений (Counter(list) - most_common(n), где n - количество элементов)
3. Реализована быстрая сортировка разбиением Ломуто (выбран крайний правый элемент в качестве опорного, весьма медленно :) )
   На вход поступают случайные значения из файла /dev/random после чего выводятся на экран, затем сортируются и снова выводятся на экран.

4. В четвертом задании реализован метод сортирвоки слияниями,- делит массив пополам до тех пор пока не останутся единичные значения, после чего сливает 
   в единый массив параллельно сравнивая значения. Входные данные такие же как и в 3-ей задаче.