import os
import filecmp
from dateutil.relativedelta import *
from datetime import date
today = date.today()

def getData(file):
	inFile = open(file, "r")
	lines = inFile.readlines()
	inFile.close()
	dictList = []
	for line in lines:
		classDict = {}
		values = line.split(",")
		firstname = values[0]
		lastname = values[1]
		email= values[2]
		year = values[3]
		dob = values[4]


		classDict['First'] = firstname
		classDict['Last'] = lastname
		classDict['Email'] = email
		classDict['Class'] = year
		classDict['DOB'] = dob
		dictList.append(classDict)
	return dictList
# get a list of dictionary objects from the file
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows

	pass

def mySort(data,col):
	sortedList = sorted(data, key = lambda x: x[col])

# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName
	firs = str(sortedList[0]["First"])
	las = str(sortedList[0]["Last"])
	return firs + " " + las
	pass


def classSizes(data):
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
	tupleList = []
	fresh = 0
	soph = 0
	junior = 0
	senior = 0


	for student in data:
		if student['Class'] == "Freshman":
			fresh += 1
		elif student['Class'] == "Sophomore":
			soph += 1
		elif student['Class'] == "Junior":
			junior += 1
		elif student["Class"] == "Senior":
			senior += 1


	tupleList.append(("Senior", senior))
	tupleList.append(("Junior", junior))
	tupleList.append(("Sophomore", soph))
	tupleList.append(("Freshman", fresh))
	sort_tuples= sorted(tupleList, key = lambda y: y[1], reverse = True)

	return sort_tuples

	pass


def findMonth(a):
# Find the most common birth month form this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data

	pass
	monthDict = {}
	for student in a:
		date = student['DOB'].split("/")
		month = date[0]
		if month in monthDict:
			monthDict[month] += 1
		else:
			monthDict[month] = 1
	months = sorted(monthDict.items(), key = lambda z: z[1], reverse = True)
	most_common = int(months[0][0])
	return most_common



def mySortPrint(a,col,fileName):
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written
	outfile = open(fileName, "w")
	sortA= sorted(a[1:], key = lambda w: w[col])
	for student in sortA:
		info = student['First'] + "," + student["Last"] + "," + student["Email"]
		outfile.write(info + '\n')

	outfile.close()


	pass

def findAge(a):




	Agetotal = 0

	numbstudents= len(a) - 1

	currentYear = int(today.year)

	currentMonth = int(today.month)

	currentDay = int(today.day)


	for student in a[1:]:
		birthdate = student["DOB"].split("/")

		birthMonth = int(birthdate[0])
		birthDay = int(birthdate[1])
		birthYear = int(birthdate[2])
		if birthMonth > currentMonth:
			age = currentYear - birthYear - 1
			Agetotal += age
		elif birthMonth == currentMonth:
			if birthDay > currentDay:
				age = currentYear - birthYear - 1
				Agetotal += age
			else:
				age = currentYear - birthYear
				Agetotal += age
		else:
			age = currentYear - birthYear
			Agetotal += age
	averageAge = round(Agetotal/numbstudents)
	return averageAge




# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.

	pass


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
