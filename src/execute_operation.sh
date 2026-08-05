#!/bin/bash

# bash script to execute the operation.py python script

# directory information
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# variables
PYTHON_FILE="$SCRIPT_DIR/operation.py"
OPERATION="MULTIPLY" # keyword: "ADD" or "MULTIPLY"
INT_1=6
INT_2=7

# execute operation.py with arguments
python "$PYTHON_FILE" "$OPERATION" $INT_1 $INT_2 