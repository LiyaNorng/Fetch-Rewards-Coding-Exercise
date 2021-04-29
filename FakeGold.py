
from selenium import webdriver
import time
# Have to change the path according to where your chromedriver locate
PATH = "C:\Program Files (x86)\chromedriver.exe"  

driver = webdriver.Chrome(PATH)
driver.get("http://ec2-54-208-152-154.compute-1.amazonaws.com/")

arrayOfBar = []
arrayLeftBowl = []
arrayRightBowl = []
n = 9;
for i in range(n):
	arrayLeftBowl.append(driver.find_element_by_id("left_" + str(i)))
	arrayRightBowl.append(driver.find_element_by_id("right_" + str(i)))
	arrayOfBar.append(driver.find_element_by_id("coin_" + str(i)))

"""
	This problem is best to divide and conquer. It is suited for Binary Search Algorithm. 
	We can divide the array of gold bar into three locations. Left table, mid, and the right table.
	If the left table and right table are equal weight then it mean the mid is FAKE GOLD. 
	But if the left table is less than the right table. Then we would toss everthing from mid + 1 
	to n (size of array). Or if the left table is greater than the right table, then we would toss everything from 0 to mid - 1. 
	Doing this we are dividing the search item by half of the size of the array and conquer it by picking the table that is less than. 
	This would give us time complexity of O(logn) time. 
"""

low = 0
high = len(arrayOfBar) - 1
while(low < high):
	mid = int(low + ((high - low) / 2))
	# reset the table
	driver.find_element_by_xpath("/html/body/div/div/div[1]/div[4]/button[1]").click()
	j = 0
	for i in range (low, mid):
		# setting the left table
		arrayLeftBowl[j].send_keys(i)
		j += 1
	j = 0
	for i in range (mid + 1, high + 1):
		# setting the right table
		arrayRightBowl[j].send_keys(i)
		j += 1

	# Weight the item
	driver.find_element_by_xpath("/html/body/div/div/div[1]/div[4]/button[2]").click()
	time.sleep(5)
	# getting the result after weight
	result = driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/button").text

	if(j == 1):
		if(result == "<"):
			print("Fake gold is " + str(low))
			arrayOfBar[low].click()
			break
		elif(result == ">"):
			print("Fake gold is " + str(high))
			arrayOfBar[high].click()
			break

	if(result == "="):
		print("Fake gold is " + str(mid))
		arrayOfBar[mid].click()
		break
	elif( result == ">"):
		low = mid;
	else:
		high = mid;
	
time.sleep(3)
driver.quit()