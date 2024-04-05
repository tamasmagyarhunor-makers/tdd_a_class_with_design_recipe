# {{Toybox}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._
```
As a User
So I can keep my room tidy
I want to have a Toybox

As a User
So I can keep my room tidy
I want to put my toys into the Toybox

As a User
So I know whats in my Toybox
I want to check the contents of my Toybox
```

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Toybox:

    def __init__(self, name):
        self.name = name
        self.storage = []
        # Parameters:
        #   name: string
        # Side effects:
        #   Sets the name property of the self object
        pass # No code here yet

    def add_toy(self, toy):
        # Parameters:
        #   toy: string representing a toy
        # Returns:
        #   Nothing
        # Side-effects
        #   Saves the toy to the self objects storage variable
        pass # No code here yet

    def see_toybox_contents(self):
        # Returns:
        #   A list of toys
        # Side-effects:
        #   No side-effects
        pass # No code here yet

```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given we want to store toys
#we can instantiate a new Toybox
"""
toybox = Toybox('Childrens room')
actual = toybox.name

expected = 'Childrens room'

assert actual == expected

"""
Given we have a Toybox
we can add toys into it
"""
toybox = Toybox('Childrens room')
toybox.add_toy('car')

actual = toybox.storage
expected = ['car']

assert actual == expected

"""
Given we have a toybox
we can check the contents of it
"""
toybox = Toybox('Childrens room')
toybox.add_toy('car')
toybox.add_toy('G.I Joe')
toybox.add_toy('wrestler')
toybox.add_toy('Barbie')

actual = toybox.see_toybox_contents()
expected = ['car', 'G.I Joe', 'wrestler', 'Barbie']

assert actual == expected

```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._


<!-- BEGIN GENERATED SECTION DO NOT EDIT -->

---

**How was this resource?**  
[😫](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😫) [😕](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😕) [😐](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😐) [🙂](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=🙂) [😀](https://airtable.com/shrUJ3t7KLMqVRFKR?prefill_Repository=makersacademy%2Fgolden-square-in-python&prefill_File=resources%2Fsingle_class_recipe_template.md&prefill_Sentiment=😀)  
Click an emoji to tell us.

<!-- END GENERATED SECTION DO NOT EDIT -->
