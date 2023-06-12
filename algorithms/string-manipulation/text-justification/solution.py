# Efficient Solution
def full_justify_efficient(words, max_width):
    lines, cur, num_of_letters = [], [], 0
    for w in words:
        if num_of_letters + len(w) + len(cur) > max_width:
            for i in range(max_width - num_of_letters):
                cur[i%(len(cur)-1 or 1)] += ' '
            lines.append(''.join(cur))
            cur, num_of_letters = [], 0
        cur += [w]
        num_of_letters += len(w)
    return lines + [' '.join(cur).ljust(max_width)]

# Inefficient Solution
def full_justify_inefficient(words, max_width):
    res, cur, num_of_letters = [], [], 0
    for w in words:
        if num_of_letters + len(w) + len(cur) > max_width:
            if len(cur) == 1:
                res.append( cur[0] + ' '*(max_width - num_of_letters) )
            else:
                num_spaces = max_width - num_of_letters
                space_between_words, num_extra_spaces = divmod( num_spaces, len(cur)-1 )
                for i in range(num_extra_spaces):
                    cur[i] += ' '
                res.append( (' '*space_between_words).join(cur) )
            cur, num_of_letters = [], 0
        cur += [w]
        num_of_letters += len(w)
    res.append( ' '.join(cur) + ' '*(max_width - num_of_letters) )
    return res
