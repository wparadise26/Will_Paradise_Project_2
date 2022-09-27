file = open("sample.txt", "r")
lines = file.readlines()
for both in lines:
    both = both.strip()
    both = both.split(':')
    id = both[0]
    grade = both[2]
    print(f"You're student id is {id}, & you're GPA is {grade}.")