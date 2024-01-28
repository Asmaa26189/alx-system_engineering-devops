#!/usr/bin/env bash
# display message
file_h="/etc/passwd"
while IFS= read -r line
do
    echo "$line" | cut -d":" -f1,3,6
done < "$file_h"