#!/usr/bin/env perl

use strict;
my $dir = '/tmp/twreporters/articles/';
opendir (DIR, $dir) or die $!;

while (my $file = readdir(DIR)) {
    my $mime_type = 'text/html';
    if ($file =~ /\.js$/) {
        $mime_type = 'text/jacascript'; 
    } elsif ($file =~/\.css/) {
        $mime_type = 'text/css'
    }
    my $gsutil_string = "gsutil -h \"Content-Type:".$mime_type."\" -h \"Cache-Control:max-age=3600,public\" -h \"Content-Language:zh\" cp -z html -a public-read /tmp/twreporters/articles/".$file." gs://twreporter-article.twreporter.org/uploads/";
    `$gsutil_string`;
        
}
close (DIR);

`gsutil -m mv -a public-read gs://twreporter-article.twreporter.org/uploads/* gs://twreporter-article.twreporter.org/`;

`sudo rm -f /tmp/twreporters/articles/*`;
