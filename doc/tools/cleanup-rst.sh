#!/bin/bash

SOURCE=$1
COLUMNS=70

section1=$(python -c "print(\"=\" * $COLUMNS, end=\"\")")
section2=$(python -c "print(\"-\" * $COLUMNS, end=\"\")")
section3=$(python -c "print(\"^\" * $COLUMNS, end=\"\")")
section4=$(python -c "print(\"~\" * $COLUMNS, end=\"\")")

sed -e "s/^=\+$/$section1/" -e "s/^-\+$/$section2/" -e "s/^\^\+$/$section3/" -e "s/^~\+$/$section4/" $SOURCE;
