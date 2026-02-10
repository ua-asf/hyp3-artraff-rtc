#!/bin/bash --login
set -e
conda activate hyp3-artraff-rtc
exec python -um hyp3_artraff_rtc "$@"
