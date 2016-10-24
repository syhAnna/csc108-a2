![UofT Logo](http://imgur.com/wSFIaD2.png)
# CSC108 A2 - Due November 1<sup>st</sup>
## Instruction
- [A2 Website](http://www.teach.cs.toronto.edu/~csc108h/fall/assignments/a2/index.shtml)
 
- This assignment is designed to give you practice with loops (over strings and lists), functions, and modules. 

### DNA Manipulation 

Computer science concepts can be applied to solve problems in many different domains. In this assignment, the problem domain is DNA manipulation. 

Below is a link to further reading. To help guide your reading, you should make sure that you learn what the following terms mean as you read the DNA manipulation page. We have written the rest of the handout under the assumption that you know their definitions. 
- base 
- base pair 
- DNA 
- palindrome 
- DNA palindrome 
- restriction site 
- restriction enzyme 
- recognition sequence
- DNA mutation 
- 1-cutter 
The reading is a [page on DNA manipulation](http://www.teach.cs.toronto.edu/~csc108h/fall/assignments/a2/dna.shtml) that covers the information — and defines the terms — that you will need. Bookmark this page: it will be a useful reference for this assignment. 

### What To Do

In this assignment, you will create two modules, called `palindromes.py` (which will contain the functions in the table under "Task 1" below), and `dna.py` (which will contain the functions in the table under "Task 2" below).

As with Assignment 1, we are providing a type check module, which you can and should run on your code as you work. You are responsible for doing thorough testing of your own code and making sure it works correctly, but the typechecker is a good first step. Make sure you use it!

[Download the Assignment 2 Type Check module here.](a2_type_checker.py)

### Task 1: Regular Palindromes

To get you warmed up, the first part of this assignment asks you to write code that deals with regular (not DNA) palindromes. Remember that a regular palindrome is a phrase that reads the same forwards and backwards.

In the file `palindromes.py`, complete the function definitions for the functions listed in the table below. Use the function design recipe that you have been learning. We have included the type contracts in the table; please read through the table to understand how the functions will be used.

<caption id="palindromes">**palindromes.py**</caption>

| Function name: (Parameter types) -> Return type | Full Description (paraphrase to get a proper docstring description) |
| --- | --- |
| `is_palindrome:` `(str) -> bool` | The parameter is a string consisting only of lowercase alphabetic letters that may or may not be a palindrome. Return `True` if and only if the parameter is a palindrome. |
| `is_palindromic_phrase:` `(str) -> bool` | The parameter is a string that may be a palindrome. Return `True` if and only if the parameter is a palindrome, ignoring case and non-alphabetic characters. (To be clear, non-alphabetic characters should be ignored as if they are not present, and uppercase letters should be considered to be equal to their lowercase equivalents.) |
| `get_odd_palindrome_at:` `(str, int) -> str` | The first parameter is a string consisting only of lowercase alphabetic characters, and the second parameter is a valid index into the string. Return the longest odd-length palindrome in the string that is centered at the specified index. |

## Task 2: DNA palindromes

This part of the assignment deals with DNA palindromes and restriction enzymes. Complete the function definitions for the functions listed in the table below in `dna.py`.

The tasks performed by these functions overlap — you should identify and call some of these functions from other functions as helpers.

<caption id="dna">**dna.py**</caption>

| Function name:(Parameter types) -> Return type | Full Description (paraphrase to get a proper docstring description) |
| --- | --- |
| `is_base_pair:` `(str, str) -> bool` | Each parameters is a single character representing a base (`'A'`, `'T'`, `'C'`, or `'G'`). Return `True` if and only if the two parameters form a base pair. |
| `is_dna:` `(str, str) -> bool` | Both parameters are strings representing DNA strands. The two strands are of equal length and only contain the four characters that represent bases. Return `True` if and only if the two strands form a properly base-paired DNA molecule. |
| `is_dna_palindrome:` `(str, str) -> bool` | Both parameters are strings representing DNA strands. The two strands form DNA: `is_dna` would return `True` if called on the two inputs. Return `True` if and only if the DNA strands represented by the two parameters form a DNA palindrome. |
| `restriction_sites:` `(str, str) -> list of int` | The first parameter represents a strand of DNA. The second parameter is a recognition sequence. Return a list of all the indices where the recognition sequence appears in the DNA strand. (These are the restriction sites.) For example, if the recognition sequence appears at the beginning of the DNA strand, then `0` would be one of the items in the returned list. Only look from left to right; don't reverse either parameter to look backwards. `str.find` will probably be helpful. |
| `match_enzymes:` `(str, list of str, list of str) ->` `list of two-item [str, list of int] lists` | The first parameter is a DNA strand. The last two parameters are parallel lists: the second parameter is a list of restriction enzyme names, and the third is the corresponding list of recognition sequences. (for example, if the first item in the second parameter is `'BamHI'`, then the first item in the second list would be `'GGATCC'`, since the restriction enzyme named BamHI has that recognition sequence — you can refer to the table on the [page on DNA manipulation](dna.shtml) to see more examples of restriction enzymes and their recognition sequences.) Return a list of two-item lists where the first item of each two-item list is the name of a restriction enzyme and the second item is the list of indices (in the DNA strand) of the restriction sites that the enzyme cuts. (Hint: See `restriction_sites`.) |
| `one_cutters:` `(str, list of str, list of str) ->` `list of two-item [str, int] lists` | The parameters are the same as for `match_enzymes`. Return a list of two-item lists representing the 1-cutters for the DNA strand that is the first parameter. The first item of each two-item list is the name of a restriction enzyme and the second item is the index (in the DNA strand) of the one restriction site that the enzyme cuts. |
| `correct_mutations:` `(list of str, str, list of str, list of str) ->` `NoneType` | The first parameter represents a list of mutated strands of DNA. The second parameter represents a clean strand of DNA. The third and fourth parameters are the same as the second and third parameters for `one_cutters`. The function modifies the list of mutated strands that share a 1-cutter with the clean strand by replacing all bases starting at the 1-cutter in the mutated strand with all bases starting at the 1-cutter in the clean strand, up to and including the end of the strand. Assume that the clean strand contains exactly one 1-cutter from the enzyme names and recognition sequences provided. Here is an example of a call to `correct_mutations`. You should use this example to help you understand what the function does, and then write two more of your own examples to include in your docstring.<pre>>>> strands = ['ACGTGGCCTAGCT', 'CAGCTGATCG']<br>>>> clean = 'ACGGCCTT'<br>>>> names = ['HaeIII', 'HgaI', 'AluI']<br>>>> sequences = ['GGCC', 'GACGC', 'AGCT']<br>>>> correct_mutations(strands, clean, names, sequences)<br>>>> strands <br>['ACGTGGCCTT', 'CAGCTGATCG']
</pre>|

### When you get stuck

If you get stuck, it's likely that the terminology is confusing you. Refer to the [DNA manipulation problem domain page](dna.shtml) often. Whenever you encounter a term you don't know, use "find" to search for it in this page.

Use the function design recipe process that we've been practicing. _In a new problem domain with tricky functions this is particularly important._ You need to be confident that you know what you are implementing before you start writing code. Come up with multiple examples — with expected return values — before you start coding. If you're not sure whether an example you've created is correct, you're welcome to post it on the discussion board to get feedback.

### Typechecker

The purpose of the type check module is to help you make sure that we will be able to test your code. To use the typechecker, place `a2_type_check.py`, `palindromes.py`, and `dna.py` in the **same** directory and run `a2_type_check.py`.

*   **If the type-check module reports a message that starts with** `Hooray! The type checker passed!`: Your function parameters and return types match the assignment specification. **This does not mean that your code works correctly in all situations.** We will do a thorough job of testing your code once you hand it in, so be sure to thoroughly test your code yourself before submitting.
*   **Otherwise:** Look carefully at the message provided by the type-check module. The error messages are there to help you! Most likely, one or more of your parameter or return types does not match the assignment specification. It's also possible that your code doesn't meet some other requirement of the assignment. Fix your code and re-run the type-check module tests. The type-checker checks each function in the order they are listed in this handout, so you can use it to check each function as you write it.

Make sure the type-check module tests pass on every function you have written before submitting your solution! Again, this doesn't mean your code works correctly in all situations, but it does mean we will be able to run our marking tests on your code.

### Want to earn a good mark? Test your work!

You should carefully verify your code _before submitting_ to determine whether it works: the Test step of the Function Design Recipe is particularly important for assignments. Once the deadline has passed, we will run our own set of tests on your submission.

To test your work, you should call on each function with a variety of different arguments and check that the function returns the correct value in each case. This can be done in the shell or using another `.py` file, but must not be done in your submitted `.py` files.

## What NOT to do

Both your `palindromes.py` and `dna.py` files must _not_ include any calls to `print` or `input`. Also, do _not_ include any extra code outside of the function definitions, and do not import any modules.

Your functions should not modify any of the list arguments passed in, other than where explicitly required.

## Marking

These are the aspects of your work that will be marked:

*   **Correctness:** Your functions should perform as specified. Correctness, as measured by our tests, will count for the largest single portion of your marks.
*   **Formatting style:** Make sure that you follow the [Python style guidelines](python_style_guide.shtml) that we have introduced!
*   **Programming style:** Your variable names should be meaningful and your code as simple and clear as possible. You should use constants rather than "magic" values. You should avoid duplicate code by calling other functions within the module as helpers — there will be some marks allocated to identifying and calling helper functions.
*   **Docstrings**: We want to see great docstrings. Each function should have a complete docstring, including a type contract, description, and two examples that you have created yourself. Docstrings should be formatted according to the function design recipe process we have demonstrated in class, including the appropriate whitespace.

### A Warning about Academic Offenses

<font style="color:red">**To detect plagiarism, a software program will be used to compare all assignments submitted with all other submissions.**</font> As always, the work that you submit must be your own and you must not share your work with others.

While online resources can sometimes be helpful, we strongly caution you against searching online for assignment solutions. A large number of the academic offenses in CS are between students who have never met, and who just happened to find the same solution online. If you find it, someone else will too. Please consult the syllabus for more information about academic offences.

### What to hand in:

As in assignment 1, [we are providing a type checker to help you verify that your parameter and return type are correct.](a2_type_checker.py) While this type checker cannot substitute for testing, <font style="color:red">**the very last thing you do before submitting should be to run the type check module one last time.**</font> Otherwise, you could make a small error in your final changes before submitting that causes your code to receive zero for correctness.

Submit your `palindromes.py` and `dna.py` files according to the instructions on the course website. Remember that spelling of filenames, including case, counts: your file must be named exactly as above.