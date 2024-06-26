import os
import platform

global listStd,listBranch
listStd = ["Alisha"]
listBranch=["ECM"]
listRollNo=["211053"]

def manageStudent(): 

	print(""" 

  
 |======================================================| 
 |==========    Student Registering System    ==========|
 |======================================================|
  

Enter 1 : Display Student List 
Enter 2 : Create new Student Record 
Enter 3 : Search Existing Student
Enter 4 : Delete Student 
		
		""")

	try: 
		userInput = int(input("Please select an option: ")) 
	except ValueError:
		exit("\nHy! That's Not A Number")
	else:
		print("\n")

		
	if(userInput == 1): 
		print("List Students\n")  
		for x in range(len(listStd)):
			print("Name:-",listStd[x],"Branch:-",listBranch[x],"RollNo:-",listRollNo[x])


	elif(userInput == 2): 
		newStd = input("Enter New Student: ")
		newbranch=input("Enter Student Branch: ")
		newRollNo=input("Enter Student Roll No: ")
		if(newStd in listStd):  
			print("\nThis Student {} Already In The Database".format(newStd))  #Error Message
		else:	
			listStd.append(newStd)
		listBranch.append(newbranch)
		listRollNo.append(newRollNo)
		print("\n=> New Student {} Successfully Add \n".format(newStd))
		for students in listStd:
				print("=> {}".format(students))	

	elif(userInput == 3): 
		srcStd = input("Enter Student Name To Search: ")
		if(srcStd in listStd):
			for x in range (len(listStd)) :
				if(listStd[x]==srcStd):
					print("\n=> Record Found Of Student {}".format(srcStd))
					print("Name:-",listStd[x],"Branch:-",listBranch[x],"RollNo:-",listRollNo[x])

			
		else:
			print("\n=> No Record Found Of Student {}".format(srcStd)) #Error Message

	elif(userInput == 4): 
		rmStd = input("Enter Student Name To Remove: ")
		if(rmStd in listStd):  
			listStd.remove(rmStd)
			print("\n=> Student {} Successfully Deleted \n".format(rmStd))
			for students in listStd:
				print("=> {}".format(students))
		else:
			print("\n=> No Record Found of This Student {}".format(rmStd)) #Error Message
	 
	elif(userInput < 1 or userInput > 4): 
		print("Please Enter Valid Option")		
						

manageStudent()

def runAgain(): 
	runAgn = input("\nWant to continue y/n?: ")
	if(runAgn.lower() == 'y'):
		if(platform.system() == "Windows"): 
			print(os.system('cls')) 
		else:
			print(os.system('clear'))
		manageStudent()
		runAgain()
	else:
		quit() 

runAgain()