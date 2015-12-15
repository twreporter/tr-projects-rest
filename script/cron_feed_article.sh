#! /bin/bash

file_path="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
cd $file_path
echo 'fetching articles'
sudo ./fetch.py
echo 'update articles'
./sync_articles.sh
