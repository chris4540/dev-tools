#!/bin/bash
#
#  An example to show how to profile a python script
#
kernprof -l to_time.py
python -m line_profiler to_time.py.lprof

