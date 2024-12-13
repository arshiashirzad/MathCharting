import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

def precedence(op):
    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    if op == '^':
        return 3
    return 0

def is_negative(expression, i):

    if expression[i] == '-' and (i == 0 or expression[i - 1] in '+-*/^('):
        return True
    return False

def infix_to_postfix(expression):
    stack = []
    output = []
    i = 0
    while i < len(expression):
        token = expression[i]
        
        if token.isdigit() or token.isalpha():
            number = token
            while i + 1 < len(expression) and (expression[i + 1].isdigit() or expression[i + 1].isalpha()):
                i += 1
                number += expression[i]
            output.append(number)

        elif token == '(':
            stack.append(token)

        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()

        elif token in '+-*/^':
            while stack and stack[-1] != '(' and precedence(token) <= precedence(stack[-1]):
                output.append(stack.pop())
            stack.append(token)

        elif is_negative(expression, i):
            number = '-' + expression[i + 1] 
            output.append(number)
            i += 1  

        i += 1

    while stack:
        output.append(stack.pop())

    return ' '.join(output)

def infix_to_prefix(expression):
    expression = expression[::-1]  
    expression = expression.replace('(', 'temp').replace(')', '(').replace('temp', ')') 
    postfix = infix_to_postfix(expression)
    return postfix[::-1]







# Codes for plotting
def plot_function():
    func = input("Enter a mathematical function with 'x':")
    
    func = func.replace("^", "**")
    
    # Get the x-range for the plot
    try:
        min_x = float(input("Enter the minimum value of x: "))
        max_x = float(input("Enter the maximum value of x: "))
        step_size = float(input("Enter the step size for x: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return
    
    # Generate x values from min_x to max_x with the given step size
    x_values = np.arange(min_x, max_x, step_size)
    y_values = []
    
    # Evaluate the function for each x value
    for x in x_values:
        try:
            y_values.append(eval(func))
        except Exception as e:
            print(f"Error evaluating function at x={x}: {e}")
            y_values.append(None)
    
    # Plot the graph
    plt.plot(x_values, y_values, label=f"y = {func}")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f"Plot of {func}")
    plt.grid(True)
    plt.axhline(0, color='black',linewidth=1)
    plt.axvline(0, color='black',linewidth=1)
    plt.legend()
    plt.show()

# Function for 3D plot (function of x and y)
def plot_3d_function():
    func = input("Enter a mathematical function with 'x' and 'y' (e.g., x**2 + y**2): ")
    
    func = func.replace("^", "**")
    
    try:
        min_x = float(input("Enter the minimum value of x: "))
        max_x = float(input("Enter the maximum value of x: "))
        min_y = float(input("Enter the minimum value of y: "))
        max_y = float(input("Enter the maximum value of y: "))
        step_size = float(input("Enter the step size for x and y: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return
    
    x_values = np.arange(min_x, max_x, step_size)
    y_values = np.arange(min_y, max_y, step_size)
    X, Y = np.meshgrid(x_values, y_values)
    
    Z = np.zeros_like(X)
    for i in range(len(x_values)):
        for j in range(len(y_values)):
            try:
                Z[i, j] = eval(func.replace('x', str(X[i, j])).replace('y', str(Y[i, j])))
            except Exception as e:
                print(f"Error evaluating function at (x={X[i, j]}, y={Y[i, j]}): {e}")
                Z[i, j] = None
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z, cmap='viridis')
    
    # Labels and title
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title(f"3D Plot of {func}")
    
    # Show the plot
    plt.show()


if __name__ == "__main__":
   
    expr = input("Enter an infix expression: ")

   
    print(f"Infix Expression: {expr}")
    
   
    postfix_expr = infix_to_postfix(expr)
    prefix_expr = infix_to_prefix(expr)

   
    print(f"Postfix Expression: {postfix_expr}")
    print(f"Prefix Expression: {prefix_expr}")

   
    plot_choice = input("Would you like to plot a function (2D or 3D)? (y/n): ").strip().lower()
    if plot_choice == 'y':
        plot_type = input("Enter the plot type (2D/3D): ").strip().lower()
        if plot_type == '2d':
            plot_function()
        elif plot_type == '3d':
            plot_3d_function()
        else:
            print("Invalid plot type selected. Please choose 2D or 3D.")
