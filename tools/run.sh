#!/bin/bash

# cd to the directory of the script
cd "$(dirname "$0")"/..

uwsgi --ini 'config/uwgsi.ini'