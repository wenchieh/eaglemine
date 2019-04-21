#!/usr/bin/env bash
rm eaglemine.tar.gz
rm -rf ealgemine
mkdir eaglemine
cp -R ./{package.sh,install_libs.sh,demo.sh,run_*.py,./output,./src,./example,Makefile,README.*,requirements,user_guide.pdf} ./eaglemine
tar czf eaglemine.tar.gz --exclude='._*' --exclude='*.pyc' eaglemine
rm -rf eaglemine
echo done.
