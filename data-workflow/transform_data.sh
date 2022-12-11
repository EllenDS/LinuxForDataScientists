#!/bin/bash

dest_file=transformed_data.csv
dest_dir=~/Desktop/data-workflow
files=~/Desktop/data-workflow/Data/"*"
list_files=~/Desktop/data-workflow/lijst.txt


echo "name,value,type" >> $dest_dir/$dest_file

for f in $files
do
    name="$f"
    fname=${name:55:16}
    echo "$fname" >> $list_files
    cat "$f" | jq -r ' .rates[]| del(.unit) | join(",")' >>"$dest_dir"/"$dest_file"
done

