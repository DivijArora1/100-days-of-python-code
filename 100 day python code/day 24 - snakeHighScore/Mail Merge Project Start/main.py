#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


PLACEHOLDER= "[name]"

with open(r"day 24\Mail Merge Project Start\Input\Names\invited_names.txt") as names_file:
    names= names_file.readlines() #as a list
    print(names)

with open("day 24\Mail Merge Project Start\Input\Letters\starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip() #remove extra spaces
        new_letter = letter_contents.replace(PLACEHOLDER,stripped_name)
        # print(new_letter)

        with open (f"day 24\Mail Merge Project Start\Output\ReadyToSend\letter_for_{stripped_name}.txt",mode='w') as f:
            f.write(new_letter)




