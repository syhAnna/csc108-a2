def is_palindrome(letters):
    ''' (str) -> bool
    
    precondition: letters has only lowercase alphabetic letters.
    
    Return True iff letter is a palindrome.
    
    >>> is_palindrome('radar')
    True
    >>> is_palindrome('toot')
    True
    >>> is_palindrome('eate')
    False
    '''
    flag = True 
    for i in range(len(letters) // 2):
        if letters[i] != letters[-(i + 1)]:
            flag = False
    return flag

def is_palindromic_phrase(letters):
    ''' (str) -> bool
    
    Preconditions: non-alphabetic charaters in letters should be ignored as 
    if they are not present, and uppercase letters should be considered to be 
    equal to their lowercase equivalent.
    
    Return True iff letters is a palindrome, ignoring case and non-alphabetic 
    characters.

    >>> is_palindromic_phrase('R!?a3dAr')
    True
    >>> is_palindromic_phrase('T__o%O5t')
    True
    >>> is_palindromic_phrase('ranG23e')
    False
    '''
    lower_letters = ''
    for char in letters:
        if char.isalpha():
            lower_letters += char.lower()
    return is_palindrome(lower_letters)

def get_odd_palindrome_at(letters, ind):
    ''' (str, int) -> str
    
    Precondition: letters only has lowercase alphabetic charcters, and 
    ind < len(letters)
    
    Return the longest odd-length palindrome in the letters that is centered
    at the specified ind.
    
    >>> get_odd_palindrome_at('acnmreedeerap', 7)
    'reedeer'
    >>> get_odd_palindrome_at('acnmreedeerap', 3)
    'm'
    >>> get_odd_palindrome_at('abcndabmambadna', 8)
    'ndabmambadn'
    '''
    half = ''
    switch = 1
    for char in letters[:ind]:
        if letters[ind - switch] == letters[ind + switch]:
            half += letters[ind + switch]
            switch += 1
    return half[::-1] + letters[ind] + half

        

    
    
            
        
        
        