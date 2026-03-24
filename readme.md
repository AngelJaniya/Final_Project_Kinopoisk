 Дипломный проект: Автоматизация API Кинопоиска

Проект содержит автотесты для проверки публичного API Кинопоиска (на базе домена poiskkino.dev). Тесты написаны на Python с использованием фреймворка Pytest.

## Технологии в проекте
* Python 3.14
* Pytest (тестовый фреймворк)
* Requests (библиотека для API-запросов)
* Allure (отчеты о тестировании)

### Шаги
1. Склонировать проект 'git clone https://github.com/AngelJaniya/Final_Project_Kinopoisk
2. Установить зависимости
3. Запустить тесты 'pytest'
4. Сгенерировать отчет 'allure generate allure-files -o allure-report'
5. Открыть отчет 'allure open allure-report'

Для запуска теста используйте команду:
```
pytest --alluredir=./allure-result
```
Для просмотра отчета используйте команду:
```
allure serve allure-result/
```

Для генерации отчета используйте команду:
```
allure generate allure-result -o allure-report
```
Для просмотра отчета используйте команду:
```
allure open allure-report
```

### Стек:
- pytest
- selenium
- webdriver-manager 
- requests
- allure-pytest
- configparser
- json


### Структура:
- ./test - тесты
- ./page - описание страниц
- ./api - хелперы для работы с API
- ./configuration - провайдер настроек
   - test_config.ini - настройки для тестов
- ./test_data - провайдер тестовых данных
   - test_data.json - тестовые данные



### Запуск тестов:
- Запуск только UI-тестов,
- Запуск только API-тестов,
- Запуск всех тестов

### Библиотеки
- pip3 install pytest
- pip install selenium
- pip install webdriver-manager 
- pip install allure-pytest
- pip install requests

- Финальный проект по ручному тестированию https://bocharovaea-qa111-2-skypro.yonote.ru/share/89e35d08-ba59-4ce7-999d-43397a3f0112/doc/finalnyj-proekt-po-ruchnomu-testirovaniyu-otchyot-o-testirovanii-UrgGQg3dSw