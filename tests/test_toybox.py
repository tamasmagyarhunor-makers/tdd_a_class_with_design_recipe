from lib.toybox import *

"""
Given we want to store toys
#we can instantiate a new Toybox
"""
def test_toybox_instantiates_with_a_name():
    toybox = Toybox('Childrens room')
    actual = toybox.name

    expected = 'Childrens room'

    assert actual == expected

"""
Given we have a Toybox
we can add toys into it
"""
def test_adding_to_storage():
    toybox = Toybox('Childrens room')
    toybox.add_toy('car')

    actual = toybox.storage
    expected = ['car']

    assert actual == expected

"""
Given we have a toybox
we can check the contents of it
"""
def test_display_toybox_contents():
    toybox = Toybox('Childrens room')
    toybox.add_toy('car')
    toybox.add_toy('G.I Joe')
    toybox.add_toy('wrestler')
    toybox.add_toy('Barbie')

    actual = toybox.see_toybox_contents()
    expected = ['car', 'G.I Joe', 'wrestler', 'Barbie']

    assert actual == expected