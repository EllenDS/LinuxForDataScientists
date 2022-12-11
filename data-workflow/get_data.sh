#!/bin/bash

# data provided by CoinGecko

var_dir=~/Desktop/data-workflow/Data
var_url=https://api.coingecko.com/api/v3/exchange_rates
var_log=~/Desktop/data-workflow/opdrachtlog.txt
var_timestamp=$(date +"%F-%H-%M")
var_filename="currency-data-"$var_timestamp.json

echo "$var_timestamp" >> "$var_log"

curl "$var_url" >> "$var_log" 2>&1>> "$var_dir/$var_filename"

echo "--------------------------------------------------------------------------------------" >> "$var_log"

chmod ugo-wx "$var_dir"/"$var_filename"
