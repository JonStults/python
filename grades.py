for x in range(1,11):
    score = input("Enter your score:")
    if score >= 60 and score <= 69:
        print "Score: {}; Your grade is D".format(score)
    elif score >= 70 and score <= 79:
        print "Score: {}; Your grade is C".format(score)
    elif score >= 80 and score <= 89:
        print "Score: {}; Your grade is B".format(score)
    elif score >= 90 and score <= 100:
        print "Score: {}; Your grade is A".format(score)
else:
    print "End of the program.Bye!"
