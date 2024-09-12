def longest_common_prefix(strs):
    if not strs:
        return ""
    
    # plockar ut längden på den minsta strängen
    the_string = min(strs, key=len)

    # kollar index 0 upp till och med the_string
    for i in range(len(the_string)):

        # för alla strängar i listan
        for string in strs:

            if string[i] != the_string[i]:

                return the_string[:i]
            
    return the_string

l1 = ['flower', 'flow', 'flowing', 'flow', 'flire', 'flight', 'fly', 'flight', 'flyger', 'flingor']
l2 = ['something', 'else', 'and']

print(longest_common_prefix(l1))
print(longest_common_prefix(l2))