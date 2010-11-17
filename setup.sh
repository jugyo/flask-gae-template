#!/bin/sh
mkdir lib

libs='flask jinja2 werkzeug'

for i in $libs
do
  rm -rf $i
done

easy_install -U Flask

for i in $libs
do
  d=`easy_install -m $i | grep Using | awk '{print $2}'`/$i
  cp -rf $d lib
done

rm -rf .git

rm setup.sh

cat <<EOS > README.md
my-app
======

Run
------

    dev_appserver.py .

Deploy
------

    appcfg.py update .
EOS