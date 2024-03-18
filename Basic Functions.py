'''Block of code that performs a particular task
TYPES OF FUNCTIONS
-Built-in Functions
-User-defined Function
-Recursive Function
-Lambda Function'''

def performOperation(num1, num2, operation='sum'):
    if operation == 'sum':
        return num1 + num2
    if operation == 'multiply':
        return num1 * num2
    
performOperation(2,3,'sum')


