#2. VariableRulesAndAssignment
myvar=10 #valid Var
Myvar=10 #valid Var
#1myvar=10 ** SyntaxError: invalid syntax
#@myvar=10 ** SyntaxError: invalid syntax
my_var=10 #valid Var
#my@var=10 ** [SyntaxError]

myvar=10 #valid Var
Myvar=10 #valid Var
myvar1=10 #valid Var
_myvar=10 #valid Var

myVar=10 #case-sensistive
Myvar=20 #case-sensitive
print(myvar,Myvar)#10 20

