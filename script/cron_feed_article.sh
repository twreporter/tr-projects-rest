#! /bin/bash

# get full directory name of the script no matter where it is being called from
file_path="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $file_path
echo 'fetching articles'
sudo ./fetch.py
echo 'making rss'
./rss.pl
echo 'update articles'
./sync_articles.sh
