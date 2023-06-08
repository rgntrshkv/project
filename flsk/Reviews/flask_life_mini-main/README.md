Для скачивания проекта с GitHub создайте у себя на компьютере
папку и находясь в ней запустите терминал.
В терминале выполните комманду:
git clone https://github.com/vitaliy19v81/flask_life_mini

Откройте проект в своей среде разработки.
Установка виртуального окружения:

python3 -m venv venv

Активация виртуального окружения:

source venv/bin/activate

Для установки проекта Жизнь воспользуйтесь файлом requirements.txt.
Укажите абсолютный путь к файлу.

pip install -r /path/to/requirements.txt

Для запуска приложения в терминале:

export FLASK_APP=main.py

А затем:

flask run

Запуск происходит по адресу
http://127.0.0.1:5000

Проект создавался на ОС:
Ubuntu 22.04.2 LTS

В среде разработки:
PyCharm 2023.1 (Community Edition)

Python 3.10.6