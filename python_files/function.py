
# local function

def print_codd():
    print("im doing this work.and ill be succeed")
    print("im doing this work.and ill be succeed")
    print("im doing this work.and ill be succeed")
    print("im doing this work.and ill be succeed")
    print("im doing this work.and ill be succeed")
    print("im doing this work.and ill be succeed")
    print("im doing this work.and ill be succeed")

print_codd()
#2
def print_codd():
    text = "im doing this work.and ill be succeed"
    print(text)
    print(text)


print_codd()

# defining a function with if else staments
my_age = 24
eligible_for_ppsc = 28
def school_cal(my_age):
    if my_age==eligible_for_ppsc:
        print("you are eligible")
    elif my_age > eligible_for_ppsc:
        print("overaged")
    elif my_age < eligible_for_ppsc:
        print("underaged") 
    else :
        print("not eligible")
school_cal(28)