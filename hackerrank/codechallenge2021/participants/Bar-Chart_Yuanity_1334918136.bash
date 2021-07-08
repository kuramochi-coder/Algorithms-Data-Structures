#!/bin/bash

greatest_number=0
declare -A maximum_numbers

while read -r opt
do
    #echo "${opt}"

    while IFS=',' read -ra current_array || [[ -n "${current_array}" ]]
    do
        count=0
        for current_number in "${current_array[@]}"; do
            #echo "${current_number}"
            current_max_number="${maximum_numbers[${count}]}"
            if [[ -z "${current_max_number}" || ${current_number} -gt ${current_max_number} ]]
            then
                #echo "New Max: ${current_number}"
                maximum_numbers[${count}]="${current_number}"
                if [[ ${current_number} -gt ${greatest_number} ]]
                then
                    greatest_number=${current_number}
                fi
            fi
            count=$(( ${count} + 1 ))
        done        
    done <<< "${opt}"
done

current_maximum_row=${greatest_number}
current_maximum_index=${#maximum_numbers[@]}
current_maximum_index=$(( ${current_maximum_index} - 1 ))
while [[ ${current_maximum_row} -gt 0 ]]
do
    for maximum_number_idx in $( seq 0 ${current_maximum_index} )
    do
        maximum_number="${maximum_numbers[${maximum_number_idx}]}"
        #echo "#${current_maximum_row} - is greater than ${maximum_number}?"
        if [[ ${maximum_number} -ge ${current_maximum_row} ]]
        then
            echo -e "+\c"
        else
            echo -e " \c"
        fi
    done
    echo
    current_maximum_row=$(( ${current_maximum_row} - 1 ))
done
