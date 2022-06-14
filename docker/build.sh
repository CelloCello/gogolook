#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BUILDROOT=$DIR/..
echo $BUILDROOT

DOCKER_IMAGE=gogolook:latest
cmd="docker build -t $DOCKER_IMAGE -f $DIR/Dockerfile $BUILDROOT"
echo $cmd
eval $cmd
