### О программе
Данная программа позволяет сравнить разлиичные методы сортировки. Написана на python, используется всего 1 библиотека (*MatPlotLib*).
### Настройка
Настроить окружение для работы данной программы можно с помощью скрипта `setup.bat`, либо командами `python -m venv .venv` и `pip install -r requirements.txt`.
### main.py
Главный скрипт программы. Позволяет запустить тесты или же посмотреть результаты прошлого теста. Данные тестов хранятся в директории results, её **нельзя** удалять.

Использование:

`python -m main.py [-r, --read [file=<YEAR-MONTH-DAY HOURMINSEC.json>] | -g, --generate [array-length=1000, [sort-repeats=100], [step=10]] | -c, --clear [file=<YEAR-MONTH-DAY HOURMINSEC.json> | --all]]`

`-r, --read [file=<YEAR-MONTH-DAY HOURMINSEC.json>]` - просмотреть результаты теста. Если не указан аргумент `[<file>]`, то открывает самый последний тест.

`-g, --generate [array-length=1000, [sort-repeats=100], [step=10]]` - протестировать функции, указанных в `cfg.py`.

`-c, --clear [file=<YEAR-MONTH-DAY HOURMINSEC.json> | --all]` - удалить результаты теста. Если не указан аргумент `[<file>]`, то удаляет самый последний тест. Если указать --all, то удаляет все тесты.

### Дальнейшее использование
В папке `scripts/` хранятся компоненты программы:

В скрипте `cfg.py` содержатся стандартные настройки и массив функций для сортировки. ARRAY_LENGTH - максимальная длина массива, который будет сортироваться, SORT_REPEATS - усреднение результатов, STEP - шаг, с которым будет увеличиваться длина массива, SORTING_FUNCTIONS - массив вышеупомянутых функций.

В скрипте `sorting_functions.py` содержатся функции для сортировки.
