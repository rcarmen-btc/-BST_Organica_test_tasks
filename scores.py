import random
from pprint import pprint


def find_top_20(conds):

    # scores format:
    #
    # for math and computer science separately
    # scores = [
    #     (scores_for_all_subjects, scores_for_math, scores_for_computer_science)
    # ]
    #
    # or
    #
    # for sum of math and computer science
    # scores = [
    #     (scores_for_all_subjects, sum_of_scores_for_math_and_computer_science)
    # ]
    #
    scores = list(
        map(
            lambda x: (
                x["scores"]["math"] + x["scores"]["russian_language"] + x["scores"]["computer_science"] + x["extra_scores"],
                # for math and computer science separately
                x["scores"]["computer_science"], x["scores"]["math"]
                # for sum of math and computer science
                # x["scores"]["computer_science"] + x["scores"]["math"]
            ),
            conds
        )
    )

    # [(index, (scores...)]
    scores_with_indexes = list((i, c) for i, c in enumerate(scores))

    sorted_scores = sorted(scores_with_indexes, key=lambda item: item[1], reverse=True)

    top_20 = [(conds[c[0]]) for c in sorted_scores]

    # for ease of comparison, return with sum scores
    # top_20 = [(conds[c[0]], c[1]) for c in sorted_scores]

    return top_20[:20]


if __name__ == "__main__":
    # There are many options to solve this task.
    # With OOP or use a database, for example Postgres,
    # but this is overengineering for this case.

    # It seems I have abused functional programming, sorry.

    students_num = 100

    # generate test input
    candidates = [
        {
            'name': f'student_{s}',
            'scores': {'math': random.randint(1, 100), 'russian_language': random.randint(1, 100), 'computer_science': random.randint(1, 100)},
            'extra_scores': random.randint(1, 10)
        } for s in range(students_num)
    ]
    pprint(find_top_20(candidates))

