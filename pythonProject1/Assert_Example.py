"""
def avg(marks):
    assert len(marks) !=0, "List is empty."
    return sum(marks) / len(marks)
"""
def avg2(marks):
    try:
        assert  len(marks) !=0
    except AssertionError:
        return "Exception raised, no marks entered"
    return sum(marks)/len(marks)
marks2 = [55, 88, 78, 90, 79]
print("Average of marks2: ", avg2(marks2))