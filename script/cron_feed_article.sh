#! /bin/bash
echo 'fetching articles'
`python ./fetch.py`
echo 'update articles'
`./sync_article.sh`
