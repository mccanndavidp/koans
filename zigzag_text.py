from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

'''You're given a string, and a number of rows.
The idea is that the given string is written in a zigzag pattern
, and the function should return what the string would read like when read line-by-line.

I think the problem is written out in a particularly confusing way, so let's take a look at an example.
If the given string was "ALGORITHMOFTHEDAY", and the number of rows was 4, it would look like this:
A      T      H
L   I  H   T  E
G  R   M  F   D  Y
O      O      A
Read line-by-line, you get the string "ATHLIHTEGRMFDYOOA", which would be the output of this function.
'''


# We could map character index to line number depending on n rows.
# ie, in 1 indexing:  indexes 1 to 4 map to lines 1 to 4 , indexes 5,6 map to lines 3 and 2

#approach one : for i > n subtract the appropriate amout from n
def line_no(i, nrows):
    n_positions = (2 * nrows) - 2  #eg n down n-2 diagonal leaving off the top and bottom.
    pos = i % n_positions
    pos = pos + 1  # 1 indexed for % arithmetic to work as desired

    # To map those pos above n , they should be subtracted from n eg 4th item on 4 5th item on line before 4
    if pos > nrows :
        pos = nrows - (pos - nrows)

    res=pos
    # resume 0 indexing
    res=res-1
    return(res)

#check
line_no (0,4)
line_no (1,4)
line_no (2,4)
line_no (3,4)
line_no (4,4)
line_no (5,4)
line_no (6,4)
line_no (7,4)

def zigzag(string , nrows):
    lines = ['' for line in range(nrows)]
    for i in range(len(string)):
        char = string[i]
        line_num = line_no(i,nrows)
        lines[line_num ] += char
    answer=''
    for line in lines :
        answer = answer + line
    return(answer)


# Approach two : the line number desired can be gotten from the distance from n both for indexes both before and after n
def line_no2(i, nrows):
    n_positions = (2 * nrows) - 2
    #eg n down, and n-2 up diagonally, leaving off the top and bottom.
    pos = i % n_positions # position repeats every n_positions
    pos = pos + 1  # 1 indexed for % arithmetic to work as desired
    
    linenum = nrows - abs (nrows - pos)
    # ie. for index n, the linenumber wanted is n  . And for indexes either 1 before or 1 after n, the line number wanted is n-1 . And so on, n-2 for positions 2 before or 2 after n
    
    linenum = linenum - 1 # back to zero indexing
    return(linenum)

def zigzag2(string,nrows):
    lines = ['' for line in range(nrows)]
    for i in range(len(string)):
        char = string[i]
        line_num = line_no2(i,nrows)
        lines[line_num ] += char
    answer=''
    for line in lines :
        answer += line
        # Really not sure I like += since x = x + n seems less arcane. Not fussed on arcane.
    return(answer)
zigzag("ALGORITHMOFTHEDAY",4)
zigzag2("ALGORITHMOFTHEDAY",4)

