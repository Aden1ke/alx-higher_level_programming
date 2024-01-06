#!/bin/bash
#sends a request to that URL,displays the size
curl -s "$1" | wc -c
