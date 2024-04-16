#!/usr/bin/env bash
# Create dump sql db
mysqldump -u root --password="$1" -A --events > backup.sql
file_name=$(date +"%d-%m-%Y")
tar -czvf "$file_name".tar.gz backup.sql
