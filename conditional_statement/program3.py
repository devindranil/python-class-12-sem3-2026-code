# college admission eligiblity

passed=input("Have you passed class 12? type (Y for Yes and N for No)")

if passed=="Y":
    percentage=float(input("Enter your Percentage: "))
    if percentage>=80:
        print("You are eligible for admission into BCA Degree")
    else:
        coma_coms=int(input("Enter your computer appplication or computer science total marks out of 100: "))
        if coma_coms>=75:
            print("You are elgibile for admission into BCA degree but you need to appear into college interview no need for admission test")
        else:
            print("You need to appear the college admission test to take admission into BCA degree")
            adm_test_score=int(input("Enter the score of your college admission test out of 100: "))
            if adm_test_score>=60:
                print("You are now eligible for admission")
            else:
                print("You are not eligible for admission")
else:
    print("Sorry you are not eligible for admission")