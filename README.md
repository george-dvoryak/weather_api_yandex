# weather_forecast_by_george_dvoryak
Weather Forecast project supp. by Yandex.API

Умный сервис прогноза погоды - Уровень задача со звездочкой

Для реализации данного проекта я использовал python 3.8 с PyQT5 и программу Qt Designer
Пользовательский интерфейс - десктопное приложение, исполняемый файл main.exe
Данные о погоде и городе, полученные с Yandex API (API Яндекс.Погоды и Геокодер) подставляются в дружелюбный пользовательский интерфейс

Видео с демонстрацией программы доступно по ссылке https://www.loom.com/share/872909cfe22c49a795417c9df750e248

Десктопное приложение, выдающее текущий прогноз погоды в заданном городе.
 -Пользователь запускает программу, файл main.exe
 -Пользователь вводит город (улицу и город, район и город и т.д.)
 -При помощи Яндекс Геокодера получаем значение кооринат города
 -При помощи API Яндекс.Погоды получаем данные о погоде (температура, давление и т.д.)
 -Сравниваем данные с шаблоном и проверяем, какую одежду нужно надеть пользователю
 -Выводим все данные в интерфейс программы
 
 Программу можно запустить, просто открыв файл main.exe . На Гитхаб он не поместился, ссылка для скачивания: https://yadi.sk/d/y3b9wNDmTSXhyw
 Либо запустить main.py при наличии необходимых библиотек
 
 Ключ к API Яндекс.Погоды позволяет сделать всего 50 запросов в день. Пожалуйста, если программа будет постоянно выдавать ошибку, вставьте свой ключ в 32 строку файла main.py . Тариф - Погода на вашем сайте. Ключ после создания активируется, по моим наблюдениям, до часа.
