# Обрезка ссылок с помощью Битли

Скрипт получает ссылку в качестве аргумента и делает следующее:
* если указана ссылка bitly, то показывает количество переходов по ссылке;
* если указана иная ссылка, то  сокращает переданную ссылку с помощью [BITLY API][1]

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` (или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

Для работы скрипта необходимо получить GENERIC ACCESS TOKEN на сайте [bitly.com](https://bitly.com/a/oauth_apps). 
Он нужен для взаимодействия с [BITLY API][1]. Токен выглядит как строка наподобие следующей: `ebb88ae0f4f7352e7966b3d805d09`. 

Полученный токен храните в файле с расширением `.env`, который используется для сокрытия важной информации. Например:  
`BITLY_TOKEN=ebb88ae0f4f7352e7966b3d805d09`

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).

[1]:https://dev.bitly.com/api-reference "dev.bitly.com/api-reference"