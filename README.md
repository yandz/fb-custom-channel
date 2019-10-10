# FB Custom Channel

Package untuk mebuat Facebook Custom Channel di Qiscus Multichannel.



## Overview

Jika kamu menggunakan Qiscus Multichannel, kamu akan mengetahui bahwa ia hanya mendukung satu buat channel untuk Facebook Messenger. Jika kamu memiliki lebih dari satu Facebook Page, maka kamu tidak akan bisa menggunakannya di satu akun Qiscus Multichannel yang sama.

Package ini dapat membantumu untuk mengoneksikan lebih dari satu Facebook Page ke dalam satu akun Qiscus Multichannel. Kamu dapat mengintegrasikan sebanyak apapun Facebook Page yang kamu mau.



## Requirements

- Akun Facebook Page (tentu saja!)

- Akun Qiscus Multichannel

- Akun Heroku

  

## Instalasi

- Clone repository ini dengan command `git clone git@bitbucket.org:qiscus/fb-custom-channel.git`
- Pindah ke directory fb-custom-channel. `cd fb-custom-channel`
- Create new heroku app. `heroku create your-app-name`
- Buat custom channel Qiscus Multichannel baru. [Link](https://multichannel.qiscus.com/integration)
  - Nama channel bisa sesuai dengan yang kamu suka
  - Identifier Key usahakan memiliki minimal 13 karakter
  - Webhook URL menggunakan https://your-heroku-app-name/qismo-message
- Set config variables melalui GUI atau CLI: `bash script/set-conf-vars.sh`
- Deploy ke heroku: `git push heroku master`
- Set config variables:
  - heroku config:set FB_ACCESS_TOKEN=change-with-your-fb-access-token
  - heroku config:set FB_VERIFY_TOKEN=change-with-your-fb-verify-token
  - heroku config:set FLASK_APP=app.py
  - heroku config:set FLASK_ENV=production
  - heroku config:set QISMO_APP_ID=[your-multichannel-app-id](https://multichannel.qiscus.com/settings#information)
  - heroku config:set QISMO_BASE_URL=https://multichannel.qiscus.com
  - heroku config:set QISMO_IDENTIFIER_KEY=your-custom-channel-identifier-key