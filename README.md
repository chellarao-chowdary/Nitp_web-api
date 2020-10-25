# Nitp_Web API [Unofficial]

---
This **API** is capable of fetching notices from **[NITP Website](http://www.nitp.ac.in/php/home.php)**

---
### Show some :heart: and :star: the repo to support the project

Thank You:)
---

:facepunch: Script written in ***Python*** using ***Beautiful Soup*** and **Flask**

---

:construction: Categories

This API supports category wise. Here is a complete list of all categories.

- [x] __all__
- [x] __events__
- [x] __important__
- [x] __announcements__
- [x] __blink__
- [x] __archive__

---

## Usage

Make a request specifying the category of notices you want
```
https://nitp-web-api.vercel.app/news?category={category_name}
```
Example - https://nitp-web-api.vercel.app/news?category=announcements

### Note:- As the [official website](http://www.nitp.ac.in/php/home.php) is too slow, response may delay and the API is hosted on free service.
---

## Response Format

The response JSON Object looks something like this -

```JSON
{
	"category": "announcements",
	"data": [
		{
		"link": "http://www.nitp.ac.in/uploads/Walk-in-interviewforProject%20Assistant.pdf",
		"title": " Walk-in-interview for Project Assistant"
		},
		{
		"link": "http://www.nitp.ac.in/uploads/evaluation-21.10.2020.pdf",
		"title": " Assessment of students i.r.o July-December,2020"
		},
	],
	"success": true,
	"total":2
}
```

---
## Setup :arrow_upper_right:

Use the [git](https://git-scm.com/) to clone script of Nitp_webite-scraping

```bash
git clone https://github.com/chellarao-chowdary/Nitp_web-api.git
```

## Install dependencies

Install all dependencies listed in *requirements.txt* file

1. To install all dependencies run - 

    ```bash
    $ sudo -H pip3 install -r requirements.txt
    ```

2. Start the server

    ```bash 
    $ python3 app.py
    ```

:round_pushpin:In case of MAC OS or Linux OS, use **pip3** and **python3**

---

## Run :runner:

```python
python scrape.py
```

---
## Apps using this API
#### [Telegram Channel](https://telegram.dog/NITP_news) of  NITP Web
[![Telegram](https://img.shields.io/badge/Telegram-Channel-orange)](https://t.me/NITP_news)

---

### You can fork the repo and deploy on VPS, Heroku or Vercel :)  

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/chellarao-chowdary/Nitp_web-api/tree/master)

[![Deploy to Vercel](https://vercel.com/button)](https://vercel.com/import/project?template=https://github.com/chellarao-chowdary/Nitp_web-api/tree/master)

---
#### :star: the Repo in case you liked it :)
#### Made with :heart: in India

## Contributing :100:
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

# © [Chellarao Chowdary](https://myselfchowdary.me)