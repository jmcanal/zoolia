#!/bin/sh

# baseline 2 - rules over dependency output
tb_parser_output='../../outputs/tb_parser/filtered_tweets_train.out'
output='../../outputs/SnowBreds/sb_train_out.txt'

python3 bootstrap_rules.py ${tb_parser_output} ${output}
