#!/usr/bin/bash

less='-l';
more='-m';
help='-h';

if [[ "$1" == "$less" ]];
then
    args='-h';
elif [[ "$1" == "$more" ]];
then 
    args='-rh';
elif [[ "$1" == "$help" ]];
then
    echo "-l sort by decreasing size, -m sort by increasing size, -h to print help";
    exit 0;
fi;

get_size() {
    local path="$1";
    local size=$(du -hs "$path" 2>/dev/null | cut -f1);
    echo $size;
}

items=$(ls -A);

declare result;

for item in $items;
do
    size=$(get_size "$item");
    result+=("$size $item");
done;

printf "%s\n" "${result[@]}" | sort $args | column -t;
