#!/usr/bin/env perl
use utf8;
use strict;
use XML::RSS;
use LWP::Simple;
use JSON;
my $rss = new XML::RSS(version => '2.0');
$rss->channel(
    title => "報導者",
    description => "報導者－深入挖掘新聞",
    link => "https://www.twreporter.org/",
    copyright => "CC BY-NC-ND 3.0",
    language => "zh-TW"
);
$rss->image(
    title => "報導者",
    url => "https://www.twreporter.org/asset/favicon.png",
    link => "https://www.twreporter.org/",
);

my $api = decode_json(get('https://www.twreporter.org/api/article?max_results=100'));
for (@{ $api->{_items} }) {
    $rss->add_item(
        title => $_->{title},
        description => $_->{excerpt},
        permaLink => ($_->{story_link} or next),
        dc => {
            creator => ($_->{byline} or next),
        },
        # pubDate => scalar localtime($_->{lastPublish}),
        pubDate => gmtime($_->{lastPublish}) . " +0000",
    );
}
$rss->save("/tmp/twreporters/articles/rss2.xml");
