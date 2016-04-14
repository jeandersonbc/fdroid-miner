#!/usr/bin/bash
#
# Extract sources in their respective location
#
# Contributors:
#     Jeanderson Candido <http://jeandersonbc.github.io>
OUTPUT_DIR="downloads"

if [ ! -d "$OUTPUT_DIR" ]; then
    echo "Did not find expected directory \"$OUTPUT_DIR\""
    echo "Aborted"
    exit 1
fi

for dir in $( ls $OUTPUT_DIR ); do
    current_dir=$OUTPUT_DIR/$dir
    tar -xf $current_dir/*.tar.gz -C $current_dir 2>/dev/null
done
