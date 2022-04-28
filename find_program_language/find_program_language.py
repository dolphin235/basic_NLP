
feature_char = ['<', '>', ';', ':', '=', '==', '#']

def include_program_language(text) -> bool:
    '''
    Check whether a programming language such as C, JAVA ... is included in the text.
    1. checks special characters that are often used in programming languages.
        Warning if 1 is found, Positive if 2 is found.
    (If there is a better way, you can add it or recommend it.)
    '''
    cnt = 0
    for char in feature_char:
        if char in text:
            cnt += 1
    
    if cnt == 1:
        print("[INFO] This text is suspected to contain a programming language. - ["+text+"]")
        return False
    
    if cnt > 1:
        return True
