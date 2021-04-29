# Fetch-Rewards-Coding-Exercise
Fetch Rewards Coding Exercise - SDET

Question:
https://fetch-hiring.s3.amazonaws.com/SDET/FetchRewards_Coding_Exercise_SDET.pdf

Website used:
http://ec2-54-208-152-154.compute-1.amazonaws.com/

Tools used:
Sublime text https://www.sublimetext.com/3
Chome Web Driver https://sites.google.com/a/chromium.org/chromedriver/downloads
Selenium https://selenium-python.readthedocs.io/
Python3

Set Up:
Install python onto your system. Using pip to install Selenium. Download Chrome Web Driver. Downlaod and install Sublime text. Set the path according to the Chrome Web Driver location. 

Algorithm: 
        This problem is best to divide and conquer. It is suited for Binary Search Algorithm. 
	We can divide the array of gold bar into three locations. Left table, mid, and the right table.
	If the left table and right table are equal weight then it mean the mid is FAKE GOLD. 
	But if the left table is less than the right table. Then we would toss everthing from mid + 1 
	to n (size of array). Or if the left table is greater than the right table, then we would toss everything from 0 to mid - 1. 
	Doing this we are dividing the search item by half of the size of the array and conquer it by picking the table that is less than. This would give us time complexity of O(logn) time. 



-Liya Norng
-April 28, 2021
