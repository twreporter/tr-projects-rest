#! /bin/bash
`mkdir -p /tmp/twreporters/articles`
`gsutil -m -h "Content-Type:text/html" -h "Cache-Control:max-age=3600,public" -h "Content-Language:zh" cp -z html -a public-read /tmp/twreporters/articles/* gs://twreporter-article.twreporter.org`
`rm /tmp/twreporters/articles/*`
