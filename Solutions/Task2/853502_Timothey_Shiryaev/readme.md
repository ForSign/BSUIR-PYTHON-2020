Python 3.8.2

1. На вход поступает файл с числами в произвольном формате. На выходе получается файл с этими числами, упорядоченными по возрастанию, при помощи Merge-sort. Промежуточные результаты храниться во временных файлах.

2. На вход функции to_json() поступают данные, тип которых проверяется, и в соотвествии с этим типом данных выполняется форматирование к виду Json'а. Для проверки приведения класс -> json, реализовани класс Person

3. Реализован класс Vector, способный прововодить стандартные для векторов операции, а именно: сложение, вычитание, умножение на константу и скалярное произведение, сравнение на равенство.

4. Представлен декоратор @memory, кэширующий значение чисел фибоначчи для скорейшего вычисления, если операции с меньшими числами уже производились

5. Юнит-тесты использован модуль unittest, Coverage: 98%

Singletone: Реализован. Может быть использован для декорирования класса
Setup.py: Присутсвует