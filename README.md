## tr-projects-rest

twreporter middle-ware rest-api server

## Requirements 
``` shell
# linux
apt-get install libevent-dev
apt-get install python-all-dev
apt-get install python-pip
pip install -r requirements.txt

# mac
# install homebrew first
brew install python
/usr/local/bin/pip install -r requirements.txt
``` 

## Development
``` shell
# set mongo database in settings.py
python server.py

# mac
/usr/local/bin/python server.py
```

## Deploy

``` shell
sudo python gevent_web.py &
```

## Script

- scripts have been moved to https://github.com/twreporter/tr-projects-crontab

## Examples

http://localhost:8080/posts
http://localhost:8080/posts/the-post-slug
http://localhost:8080/posts?embedded={'authors':1,'tags':1,'categories':1}
http://localhost:8080/posts?content_type=html
http://localhost:8080/contacts?where={"_id":{"$in":["56cec38678c3ee45f715b077","56cec37a78c3ee45f715afd6"]}}
http://localhost:8080/contacts?where={"_id":{"$in":["56cec38678c3ee45f715b077","56cec37a78c3ee45f715afd6"]}, "email":"feugiat.nec.diam@idante.org"}
http://localhost:8080/posts?where={%22tags%22:{%22$in%22:[%2256d01094b4710c3602715ad2%22]}}
http://localhost:8080/users/
http://localhost:8080/contacts

# License

MIT http://mit-license.org 
