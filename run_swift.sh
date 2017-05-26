#! /bin/bash

export CHARTS_FS_BACKEND=swift
export FS_SWIFT_AUTHURL=http://127.0.0.1:8080/auth/v1.0
export FS_SWIFT_USER=test:tester
export FS_SWIFT_KEY=testing
export CHARTS_FS_URL=http://127.0.0.1:8080

source ./run_dev.sh
