def arithmetic_arranger(problems, show_answers=False):
    
    if len(problems) > 5:
        return "Error: Too many problems."

    
    first_line = []
    second_line = []
    dashes_line = []
    answer_line = []

    for problem in problems:
        
        num1, operator, num2 = problem.split()

        
        if operator not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."

        
        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits."
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        
        width = max(len(num1), len(num2)) + 2  # +2 for space and operator

        
        first_line.append(num1.rjust(width))
        second_line.append(operator + " " + num2.rjust(width - 2))
        dashes_line.append("-" * width)

        
        if show_answers:
            if operator == "+":
                answer = str(int(num1) + int(num2))
            else:
                answer = str(int(num1) - int(num2))
            answer_line.append(answer.rjust(width))

    
    arranged_problems = (
        "    ".join(first_line) + "\n" +
        "    ".join(second_line) + "\n" +
        "    ".join(dashes_line)
    )
    
    if show_answers:
        arranged_problems += "\n" + "    ".join(answer_line)

    return arranged_problems

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print()
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
