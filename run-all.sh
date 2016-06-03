#!/bin/bash
echo "WELCOME : "
echo "MAKE SURE YOU HAVE ALL THE MODULES AND PACKAGES INSTALLED AS GIVEN IN THE README"
python scopus.py
javac Parser.java
java Parser
python graph.py