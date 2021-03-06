EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Device:Battery BT1
U 1 1 5EC12AB4
P 2500 2000
F 0 "BT1" H 2608 2046 50  0001 L CNN
F 1 "V" H 2608 2000 50  0001 L CNN
F 2 "" V 2500 2060 50  0001 C CNN
F 3 "~" V 2500 2060 50  0001 C CNN
	1    2500 2000
	1    0    0    -1  
$EndComp
$Comp
L Device:Q_NPN_CEB Q1
U 1 1 5EC13616
P 3000 1400
F 0 "Q1" V 3236 1400 50  0001 C CNN
F 1 "Q_NPN_CEB" V 3326 1400 50  0001 C CNN
F 2 "" H 3200 1500 50  0001 C CNN
F 3 "~" H 3000 1400 50  0001 C CNN
	1    3000 1400
	0    -1   1    0   
$EndComp
$Comp
L Device:L L
U 1 1 5EC14E99
P 4000 1500
F 0 "L" V 4190 1500 50  0001 C CNN
F 1 "L" V 4099 1500 50  0001 C CNN
F 2 "" H 4000 1500 50  0001 C CNN
F 3 "~" H 4000 1500 50  0001 C CNN
	1    4000 1500
	0    -1   -1   0   
$EndComp
$Comp
L Device:R R1
U 1 1 5EC1598E
P 4500 2000
F 0 "R1" H 4570 2046 50  0001 L CNN
F 1 "R" H 4570 2000 50  0001 L CNN
F 2 "" V 4430 2000 50  0001 C CNN
F 3 "~" H 4500 2000 50  0001 C CNN
	1    4500 2000
	1    0    0    -1  
$EndComp
Wire Wire Line
	4150 1500 4500 1500
Wire Wire Line
	4500 1500 4500 1850
Wire Wire Line
	4500 2150 4500 2500
Wire Wire Line
	4500 2500 3500 2500
Wire Wire Line
	2500 2500 2500 2200
Wire Wire Line
	3500 2150 3500 2500
Connection ~ 3500 2500
Wire Wire Line
	3500 2500 2500 2500
Wire Wire Line
	3850 1500 3500 1500
Wire Wire Line
	2800 1500 2500 1500
Wire Wire Line
	2500 1500 2500 1800
Wire Wire Line
	3500 1850 3500 1500
Connection ~ 3500 1500
Wire Wire Line
	3500 1500 3200 1500
$Comp
L Device:D D1
U 1 1 5EC147E4
P 3500 2000
F 0 "D1" V 3454 2080 50  0001 L CNN
F 1 "D_F" V 3545 2080 50  0001 L CNN
F 2 "" H 3500 2000 50  0001 C CNN
F 3 "~" H 3500 2000 50  0001 C CNN
	1    3500 2000
	0    1    1    0   
$EndComp
$EndSCHEMATC
