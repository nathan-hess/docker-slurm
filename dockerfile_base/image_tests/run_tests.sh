#!/bin/bash

## SETUP ---------------------------------------------------------------------
# Counters for number of passed and failed tests
num_pass=0
num_fail=0


## TESTS ---------------------------------------------------------------------
# Check operating system version
ubuntu_version=22.04
if [ "$(cat /etc/os-release | grep VERSION_ID)" == "VERSION_ID=\"${ubuntu_version}\"" ]; then
    echo PASS: Operating system: Ubuntu ${ubuntu_version}
    num_pass=$((num_pass+1))
else
    echo FAIL: Operating system: $(cat /etc/os-release | grep VERSION_ID)
    num_fail=$((num_fail+1))
fi


## TEST RESULTS --------------------------------------------------------------
# Display results
total_tests=$((num_pass + num_fail))
printf "\n---------------------------------------------\n"
printf "Ran $total_tests test(s)\n"
printf "  $num_pass test(s) passed\n"
printf "  $num_fail test(s) failed\n"

# Return exit code 0 if all tests passed and 1 otherwise
if [ "$num_fail" -eq "0" ]; then
    exit 0
else
    exit 1
fi
