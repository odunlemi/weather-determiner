# A basic weather determiner using inputted values

intro = "This is a fun weather determiner. All you've got to do is look out a window and input what you see."
print(intro)

# variables
instruction = "Just enter 'True', 'False' or 'Not Sure' for each of the prompts."
sun = input("Sun out? ")
clouds = input("Cloudy? ")
rain = input("Is it raining? ")
fog = input("Does it look foggy out? ")

# conditionals
if sun == "True":
    print("Okay, sun out!")
else:
    pass
if clouds == "True":
    print("Some clouds.")
else:
    pass
if rain == "True":
    print("Rain!")
else:
    pass
if fog == "True":
    print("Foggy!")
    print("Your weather does not seem good!")
else:
    print("Likely good weather!")