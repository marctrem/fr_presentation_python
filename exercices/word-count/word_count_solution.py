__author__ = 'marc'

from collections import defaultdict
import re
import operator
import itertools
from functools import partial

chars_to_strip_re = re.compile('[,\."\';:-]')

word_holder = defaultdict(int)

curryied_update = lambda word: word_holder.update(word, )

with open('hp1.txt', 'r') as file:
    line = file.read()

    # On peut faire ça. Si vous avez fait ça vous avez 2 bières :)
    good_words = filter(lambda x: len(x) > 3, map(partial(chars_to_strip_re.sub, ''), line.split()))
    for word in good_words:
        word_holder[word] += 1

    # ou on peut aussi faire ça...
    # for word in line.split():
    #     filtered_word = chars_to_strip_re.sub('', word)
    #     print(filtered_word)
    #     if len(filtered_word) > 3:
    #         word_holder[filtered_word] += 1

word_sorted = sorted(word_holder.items(), key=operator.itemgetter(1))

print(list(itertools.islice(reversed(word_sorted), 10)))

# Answer:
# ('Harry', 1189)
# ('said', 791),
# ('that', 570),
# ('they', 425),
# ('with', 403),
# ('were', 329),
# ('Hagrid', 322),
# ('them', 319),
# ('have', 287),
# ('back', 254)]