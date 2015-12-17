#! /bin/bash

`gsutil -m -h "Content-Type:text/html" -h "Cache-Control:max-age=3600,public" -h "Content-Language:zh" cp -z html -a public-read /tmp/twreporters/articles/* gs://twreporter-article.twreporter.org`
`sudo rm -rf /tmp/twreporters/articles/*`
