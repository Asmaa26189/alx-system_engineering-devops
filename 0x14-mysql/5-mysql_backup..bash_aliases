#!/usr/bin/env bash
# Create dump sql db
mysqldump -u root -p"$1" --opt --events --all-databases > backup.sql
tar czvf "$(date '+%d-%m-%Y').tar.gz" backup.sql