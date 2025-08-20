from src.basics.practice_mutation import (
    add_item_bad,
    add_item_good,
    add_rebind,
    append_mutate,
)


def test_append_mutate_keeps_id_and_changes_content():
    lst = [1,2]
    id_pre, id_posle, out = append_mutate(lst, 3)
    assert id_pre == id_posle
    assert out is lst
    assert lst == [1,2,3]

def test_add_rebind_changes_id_and_preserves_original():
    lst = [1,2]
    id_pre, id_posle, nova = add_rebind(lst, 3)
    assert id_pre != id_posle
    assert lst == [1,2]
    assert nova == [1,2,3]

def test_bad_default_argument_shares_state_across_calls():
    out1 = add_item_bad(1)
    out2 = add_item_bad(2)
    assert out1 is out2
    assert out2 == [1,2]

def test_good_default_argument_isolated_calls():
    a = add_item_good(1)
    b = add_item_good(2)
    assert a == [1] and b == [2]
    assert a is not b
