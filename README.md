IMPORTANT: GOOGLE SHEET MATRIX TO STRING TRANSLATOR, NEEDED FOR MAKING YOUR OWN ANIMATIONS: https://docs.google.com/spreadsheets/d/1nLzNgmt7ZzwulCrQPWVYLt563ayicPx0T74myMAICf0/edit?usp=sharing


DISCLAIMER: I CANT GAURENTEE ANY OF MY CODE WILL WORK IN YOUR CASE, PLS TAKE CAUTION

TO RUN THIS CODE, YOU MUST HAVE A BOARD THAT RUNS CIRCUT PYTHON, PREFERABLY CIRCUT PLAYGROUND BLUEFRUIT

How to use:
1. Download both the Blank and extension repository and move the repo to your board files
2. open the Blank file in a py editor such as MuEditor and open the google sheet linked above and follow the instructions inside
3. Once done, save code to your board
4. Download bluefruit connect and connect to the board
5. go to control and go to buttons or color wheel
6. enjoy :P

To explain kinda what the program dose, the code takes the frame data you put into each library as instructions. Think of the program as a pegboard opperator(or stanley from the stanley parable loll) and each individual light as an on/off switch. Each time the program decides when the next frame comes(depending on the times you insert), the program will receive specific lights and it will swap their state from on to off.
for example if i had a 3x3 grid and wanted to turn this pattern,

0xx

x0x

xx0

, into this pattern

0xx

0xx

0xx

, id need to tell the program to toggle the middle and bottom right lights as well as the left middle and left bottom lights, making the instructions in the library look like this,

xxx

00x

0x0

reach out if you have any questions pls, thanks for reading!!!
