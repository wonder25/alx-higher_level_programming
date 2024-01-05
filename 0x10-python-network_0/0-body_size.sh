#!/bin/bash
# displays size of the body of the response

curl -w "%{size_download}\n" "$1" -so /dev/null
