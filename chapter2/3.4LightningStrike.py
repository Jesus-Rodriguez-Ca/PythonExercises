# Assigment 2 Lighthning Strike
# Jesus Manuel Rodriguez Castro
# 9/17/2019
# Determines the distance to a lightning strike based om the time-
# -elapsed between the flash and the sound of the thunder.

def main():
    print("This program will determine the distance to a lightning strike"" "
          "based on the time elapsed between the flash and the sound of a thunder")
    Time = eval(input("Enter the time, in seconds: "))
    Sound = Time * 1100
    Distance = Sound / 5280
    print(Distance)

main()

    
                
                      
