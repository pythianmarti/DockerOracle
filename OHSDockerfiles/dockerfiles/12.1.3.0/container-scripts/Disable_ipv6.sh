#!/usr/bin/env bash

# Inline edits and moves don't work inside containers
sed 's/^::1.*localhost/::1\tip6-localhost/g' /etc/hosts > /etc/hosts.tmp
cat /etc/hosts.tmp > /etc/hosts
rm -f /etc/hosts.tmp

exec "$@"
