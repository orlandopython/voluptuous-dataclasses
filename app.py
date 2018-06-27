"""
Orlando Python Voluptuous + Dataclasses example main
"""

# stdlib
import json
import math
from collections import Counter
from pprint import pprint
# library
from begin import start
from voluptuous import Invalid, MultipleInvalid
# module
from comment_struct import Comment
from validators import comments_schema

@start
def main(datapath: 'Path to the payload') -> int:
    """
    Runs some basic calculations on simulated forum posts
    """
    # At the very start, we can load, validate, and convert our comments into dataclasses
    try:
        comments = [Comment(**c) for c in comments_schema(json.load(open(datapath)))]
    except (Invalid, MultipleInvalid) as exc:
        print(exc)
        return 1

    print(comments[0])

    print()
    print('Total comments:', len(comments))

    # Aggregate post IDs
    post_ids = {comment.post_id for comment in comments}
    print('Total forum posts:', len(post_ids))

    # Count comment lengths
    tot_len = sum([len(comment.body) for comment in comments])
    print(f'The total corpus length is {tot_len} characters')
    print(f'The average comment length is {round(tot_len/len(comments))} characters')

    # Count email top level domains
    counts = Counter([comment.email.split('.')[-1] for comment in comments])
    print('Most popular email TLDs:')
    pprint(counts)

    print()
    return 0
