## tr-projects-rest

twreporter middle-ware rest-api server

## Requirements

``` shell
apt-get install libevent-dev
apt-get install python-all-dev
apt-get install python-pip
pip install -r requirements.txt
```

## Development

``` shell
# set mongo database in settings.py
python server.py
```

## Deploy

``` shell
sudo python gevent_web.py &
```

## Script

- scripts have been moved to https://github.com/twreporter/tr-projects-crontab
