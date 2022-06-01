# Return-Values
  # What is the syntax for returning a value?
  #### Syntax:
    The value can be any value or variable from within the function
    When returning a variable, the variable name is still only usable within the scope of the function
    Still causes the function to end early
      *return value*
  # What can be done with returned values?
  * The function call is "replaced" with the return values
  * Functions that return values are expressions
  * Can be used anywhere expressions are used, including:
  * Right side of assignment statements (variable = function call)
  * Print out the value
  * Conditions
  * Part of a larger calculation
  # What if a function doesn't return a value?
  * The value None is returned by default
  * Has the type NoneType
  * Doesn't matter if the value isn't saved
  # When should a function return a value?
  * The function calculates a value that the main program needs
  * The function creates a new value or object that needs to be stored
  * The function performs an action and returns information about what it did
