#!/bin/bash
cat input.txt | python map.py | sort | python reduce.py
