#!/bin/sh

set -e

PATH=/usr/local/bin:/usr/bin:/bin
REMOTE="gogs@linux.xidian.edu.cn:xdlinux/xdosc-posts.git"
REPO=/home/bot/xdosc-posts
DATE=`date +%Y-%m-%d`
FILE=${DATE}-mirrors-access-count.md
COMMIT="automatic mirrors-access-count"

rm -rf $REPO
git clone $REMOTE $REPO
mirrors-access-count --lastmonth > $REPO/_posts/$FILE
git -C $REPO add --all
git -C $REPO commit -m $COMMIT
git -C $REPO push --force
