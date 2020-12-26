#school Administrative Program
import csv

def write_into_csv(info_list):
    with open('student_inf.csv','a', newline='') as csv_file:
        writer = csv.writer(csv_file)

        if csv_file.tell()==0:
            writer.writerow(["Name","Age","Contact Number","Email ID"])
            
        writer.writerow(info_list)

if __name__ == '__main__':
    condition = True
    student_num = 1
    
    while(condition):
            student_information = input("Enter student information for student #{} in the following format (Name Age Contact_Number Email_ID):".format(student_num))
            #split
            student_info_list = student_information.split(' ')

            print("\nThe Entered Information is -\nName: {}\nAge: {}\nContact_No.: {}\nEmail ID: {}".format(student_info_list[0],student_info_list[1],student_info_list[2],student_info_list[3]))
            choice_check = input("Is the entered information correct?(yes or no):")

            if choice_check == "yes":
                  write_into_csv(student_info_list)

                  condition_check = input("Enter (yes or no) if you want to enter information for another student:")
                  if condition_check == "yes":
                      condition = True
                      student_num = student_num + 1
                  elif condition_check == "no":
                      condition = False
            elif choice_check == "no":
                 print("\n Please re-enter the values:")
                 
        
                  
    
        
          
    
