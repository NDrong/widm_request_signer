## 'Wie is de Mol?' API Request Signer
This repository contains a simple Python 3 application that takes a raw HTTP request from `./signature`
and signs it using the HMAC algorithm (SHA-256) used by the 'Wie is de Mol?' Android app and its API. See 
[this article](https://n04m.nl/reverse-engineering-the-wie-is-de-mol-app) on my blog for more details on the background behind this utility.

### Why?
I was interested in reverse engineering the API behind the popular 'Wie is de Mol?' app. When I started reversing
the Android app, I noticed that requests are signed, with the signatures being verified by the backend. In order to 
execute arbitrary request against the API, I needed a tool that would sign requests using the app's hardcoded secret.

### Where?
You can find the API on `api.wieisdemol.nl`. So far, I've come across the following routes while using the Android 
application:

- `/config/`
- `/profile/`
- `/profile/forgot_password/`

I might add more details when I have the time later (as it's currently already past 1 AM...)

### License
See [`LICENSE`](LICENSE) for more information.
