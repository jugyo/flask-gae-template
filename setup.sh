#!/bin/sh
lib='flask jinja2 werkzeug'

for i in $lib
do
  rm -rf $i
done

easy_install -U -i http://pypi.python.jp/ Flask

for i in $lib
do
  d=`easy_install -m $i | grep Using | awk '{print $2}'`/$i
  cp -rf $d .
done
