otus_qa_course


03.03.2023 Домашнее задание #1
Создан проект, добавлен readme, gitignore

12.03.2023 Домашнее задание #2 

Треугольник создается через статический метод create_triangle, в нем происходит валидация
входных параметров и, в зависимости от результата, выброс ValueError или создание экземпляра.
В задании указано, что создание объекта должно иметь вид triangle = Triangle(13, 14, 15), но 
отдавать валидацию входных данных конструктору, говорить ему "создай объект", а потом падать с ошибкой
не совсем корректное решение. 

24.03.2023 Домашнее задание #3
Добавлен скрипт file_reader, который считывает 2 файла с книгами и юзерами, а потом создает 
новый json, в котором имеющимся пользователям распределяются имеющиеся книги по соответствующей структуре.
Пути к файлам прописаны helpers.paths, который является вспомогательным подмодулем file_reader. 

29.03.2023 Домашнее задание #4 
Написаны тесты на 3 сервиса + тест с использованием pytest.addoption
Для некоторых сервисов проверяется схемы ответов по некоторым ручкам. Их схемы вынесены в файл schema_validation.
Первый тест в test_task3_1.py во время выполнения забирает список имеющихся пород и записывает их в отдельный файл с 
данными. Тесты, которые проверяют запросы отдельной породы и субпороды, берут данные из файла.
