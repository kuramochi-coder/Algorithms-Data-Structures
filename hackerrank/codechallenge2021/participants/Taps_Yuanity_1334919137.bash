#!/bin/bash

declare -A single_tap_capability=()
total_taps=0

count=0
while IFS= read -r opt || [[ -n "${opt}" ]]
do
  #echo "Input: ${opt}"
  if [[ ${count} -eq 0 ]]
  then
    total_taps="${opt}"
    count=$(( ${count} + 1 ))
    continue
  fi

  single_tab_duration="${opt}"
  total_tab_with_similar_duration="${single_tap_capability[${single_tab_duration}]}"
  if [[ -z "${total_tab_with_similar_duration}" ]]
  then
    total_tab_with_similar_duration=1
  else
    total_tab_with_similar_duration=$(( ${total_tab_with_similar_duration} + 1 ))
  fi
  single_tap_capability[${single_tab_duration}]=${total_tab_with_similar_duration}  
done

current_rate_of_flow=0
for current_tap_capability in "${!single_tap_capability[@]}"
do
    current_tap_capability_seconds=$(( ${current_tap_capability} * 60 ))
    current_total_taps=${single_tap_capability[${current_tap_capability}]}
    #echo "Processing: ${current_tap_capability_seconds} with ${current_total_taps}"
    current_tap_rate_of_flow=$( awk -v a=${current_tap_capability_seconds} \
            -v b=${current_total_taps} \
            'BEGIN{print 1 / a * b}' )
    current_rate_of_flow=$( awk -v a="${current_rate_of_flow}" \
            -v b="${current_tap_rate_of_flow}" \
            'BEGIN{print a + b}' )
done

#current_seconds_not_rounded=$( awk -v a=${current_rate_of_flow} \
#            'BEGIN{printf "%.2f", (1/a)}' )
current_seconds_required=$( awk -v a=${current_rate_of_flow} \
            'BEGIN{printf "%.0f", (1/a)}' ) 

#echo "${current_seconds_not_rounded}"
echo "${current_seconds_required}"
