def OccurenceFinder(str1, str2):
    last_letter = str2[-1]
    occurence = 0
    for i in str1:
        if i == last_letter:
            occurence += 1
    return occurence

print(OccurenceFinder("going to go to goa", "go"))
