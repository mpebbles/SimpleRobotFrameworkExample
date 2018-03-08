*** Settings ***
Documentation     Practice test suite using the keyword-driven testing approach.
Library           lib/SimpleRPN.py

*** Test Cases ***
No input
    Run program without args

Valid input
    [Template]     Output should be
    22+            4
    99+            18
    01+            1
    00+            0

Invalid input
    [Template]     Output should be
    -222           ${INVALID INPUT}
     22a           ${INVALID INPUT}

*** Keywords ***
Output should be
    [Arguments]    ${input}    ${output}
    Run program with input     ${input}
    Result should be           ${output}

Run program without args
    Run program without input
    Result should contain      ${USAGE MESSAGE}

*** Variables ***
${INVALID INPUT}   Invalid input.
${USAGE MESSAGE}   Usage:
