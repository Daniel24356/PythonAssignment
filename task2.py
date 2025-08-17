import re

#3
def groupAnagrams(sentences):
    groups = {}

    for s in sentences:
        # normalize the sentences
        cleaned = re.sub(r'[^a-z]', '', s.lower())
        # sort the normalized sentence
        key = ''.join(sorted(cleaned))
        # if the key doesnt exist in groups:
        if key not in groups:
            groups[key] = [] #create one
        groups[key].append(s) # if it exists, add the sentence

    return list(groups.values()) # return the list of values


print(groupAnagrams(['Listen to me', 'Enlist to me', 'The eyes', 'They see']))

#4
def rankStudentsByAvgScore(dicts):
    students = []
    for name, scores in dicts.items():
        #find the avg of the values
        avg = sum(scores) / len(scores)
        students.append((name, round(avg, 2)))
    
    #sort by descending order (-x[1]) and if avg is equal sort name by aplabetical order(x[0])
    sorted_students = sorted(students, key=lambda x: (-x[1], x[0]))
    return sorted_students

print(rankStudentsByAvgScore({'Alice':[90,85,88], 'Bob':[90,85,88], 'Charlie':[95,80,85]}))