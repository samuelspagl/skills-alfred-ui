#!/bin/sh
# Produce only JSON on stdout. This timestamp format contains no JSON-sensitive characters.
stamp=$(date +%H:%M:%S)
printf '{"update":{"ids":{"clock":{"text":"%s"}}}}\n' "$stamp"
