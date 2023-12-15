from day_15 import solution


def test_hash_term():
    cases = [
        ("rn=1", 30),
        ("cm-", 253),
        ("qp=3", 97),
        ("cm=2", 47)
    ]

    for case in cases:
        assert solution.hash_term(case[0]) == case[1]


def test_initialize():
    sequence = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
    assert solution.initialize(sequence) == 145


def test_hash_sum():
    sequence = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"
    assert solution.hash_sum(sequence) == 1320
