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