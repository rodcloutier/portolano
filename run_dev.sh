#! /bin/bash

mkdir -p $PWD/instance

export FLASK_APP=portolano
export DEBUG=1
export FLASK_FS_OVERWRITE=1
export FS_LOCAL_ROOT=$PWD/instance
export CHARTS_FS_URL=http://127.0.0.1:5000

flask run $@
