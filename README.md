# redis
## Домашняя работа №3. Redis
**Цель:** В результате выполнения ДЗ вы научитесь разворачивать Redis в кластере, заполнять данными и делать запросы.
**Описание/ инструкция выполнения домашнего задания:**
1.	Сохранить большой JSON (~20МБ) в виде разных структур - строка, hset, zset, list;
2.	Протестировать скорость сохранения и чтения;
3.	Настроить редис кластер на 3х нодах с отказоустойчивостью, затюнить таймоуты.
4.	Предоставить отчет.

## Скачивание
Ubuntu 21.10
#### redis-cli
```
sudo apt install redis-server
```
#### redisinsight
скачиваем по [ссылке](https://download.redisinsight.redis.com/latest/RedisInsight-v2-linux-x86_64.AppImage)
```
chmod a+x RedisInsight-preview-linux.AppImage
./RedisInsight-preview-linux.AppImage
```
И создаём db в RedisInsight


![](https://github.com/FAnastasiaF/redis/blob/main/db.png)

## JSON

Я взяла, первую треть из [Jeopardy Dataset](https://www.reddit.com/r/datasets/comments/1uyd0t/200000_jeopardy_questions_in_a_json_file/) —  216,930 записей «вопрос-ответ» из телевизионной игры(~70МБ).

**Структура**
* 'category' : категория вопроса
* 'value': стоимость вопроса(нет для Final Jeopardy!)
* 'question' : текст вопроса
* 'answer' : текст ответа
* 'round' : один из "Jeopardy!","Double Jeopardy!","Final Jeopardy!" or "Tiebreaker"
* 'show_number' : строка номера шоу
* 'air_date' : дата выхода в эфир в формате ГГГГ-ММ-ДД.

## Сохранение и Чтение json

### строка
С помощью [кода](https://github.com/FAnastasiaF/redis/blob/main/str.py) на python сохраняем и читаем 1000 строк из нашего json
```
Сохранено 1000 строк
За 2.122185468673706 секунд
Прочитано 1000 строк
За 0.04412245750427246 секунд
```
### hzet
С помощью [кода](https://github.com/FAnastasiaF/redis/blob/main/hset.py) на python сохраняем и читаем 1000 строк из нашего json
```
Сохранено 1000 строк
За 2.62434720993042 секунд
Прочитано 1000 строк
За 0.004089832305908203 секунд
```
### zset
С помощью [кода](https://github.com/FAnastasiaF/redis/blob/main/zset.py) на python сохраняем и читаем 1000 строк из нашего json
```
Сохранено 1000 строк
За 2.411116361618042 секунд
Прочитано 1000 строк
За 0.004126310348510742 секунд
```
### list
С помощью [кода](https://github.com/FAnastasiaF/redis/blob/main/list.py) на python сохраняем и читаем 1000 строк из нашего json
```
Сохранено 1000 строк
За 2.4646692276000977 секунд
Прочитано 1000 строк
За 0.0021517276763916016 секунд
```
## Итог
### Сохранение
№ | Структура | Время
:--- | :------- | :----
1  | строка | 2.12 сек
2  | zset  | 2.41 сек
3  | list  | 2.46 сек
4  | hset  | 2.62 сек

### Чтение
№ | Структура | Время
:--- | :------- | :------
1  | list | 0.0021 сек
2  | hset  | 0.0040 сек
3  | zset  | 0.0041 сек
4  | cтрока  | 0.0441 сек

## Редис кластер

