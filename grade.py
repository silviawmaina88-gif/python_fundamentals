def grade_converter():
    """converts numeric scores into letter grade using ternery operations"""
    try:
        score=int(input("enter your score(0-100):"))

    #multiple ternay operations chained
        letter_grade=(
            "A" if score >= 90 else
            "B" if score >= 80 else
            "C" if score >= 70 else
            "D" if score >= 60 else
            "F" if score >= 0 else
            "invalid score"
        )
        # another ternary for pass and fail
        status = "passed" if score >=60 else "failed"
        print(f"score : {score}-> grade :{letter_grade}({status})")

    except ValueError:
        print("please enter a valid number")
        
grade_converter()