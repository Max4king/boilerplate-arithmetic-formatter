def arithmetic_arranger(problems, solution=False):
    if problems[-1] == True:
        solution = True
    new_problems = []
    list_problems = []
    arranged_problems = ""
    answer = []
    # creates a new list to store the problems
    for i in range(len(problems)):
        new_problems.append(problems[i].split())

    # check if the problem is valid number
    valid = valid_number_n_operator(new_problems)
    if not valid[0]:
        return valid[1]
    # print(int(new_problems[0][0]) + int(new_problems[0][2]))
    if solution == True:

        for i in range(len(new_problems)):
            if new_problems[i][1] == "+":
                answer.append(int(new_problems[i][0]) + int(new_problems[i][2]))
            elif new_problems[i][1] == "-":
                answer.append(int(new_problems[i][0]) - int(new_problems[i][2]))
        list_problems = ["", "", "", ""]
        for i in range(len(new_problems)):
            first, second, third, fourth = format_problem(new_problems[i], answer[i])
            list_problems[0] += first
            list_problems[1] += second
            list_problems[2] += third
            list_problems[3] += fourth
    else:
        list_problems = ["", "", ""]
        for i in range(len(new_problems)):
            first, second, third = format_problem(new_problems[i])
            list_problems[0] += first
            list_problems[1] += second
            list_problems[2] += third
    for i in range(len(list_problems)):
        list_problems[i] = list_problems[i].rstrip()
        arranged_problems = arranged_problems + list_problems[i] + "\n"
    return arranged_problems[:-1]


def format_problem(problem, answer=False):
    space = " "
    double_space = space * 2
    space_equation = space * 4
    first_line = ""
    second_line = ""
    third_line = ""
    fourth_line = ""
    space_num = space * (
        max(len(problem[0]), len(problem[2])) - min(len(problem[0]), len(problem[2]))
    )
    if len(problem[0]) > len(problem[2]):
        first_line = double_space
        second_line = problem[1] + space + space_num
    elif len(problem[0]) < len(problem[2]):
        first_line = double_space + space_num
        second_line = problem[1] + space
    else:
        first_line = double_space
        second_line = problem[1] + space
    first_line = first_line + problem[0] + space_equation
    second_line = second_line + problem[2] + space_equation
    third_line = "-" * (2 + max(len(problem[0]), len(problem[2]))) + space_equation
    if answer == False:
        return first_line, second_line, third_line
    elif answer < 0:
        fourth_line = space + str(answer) + space_equation
    else:
        fourth_line = double_space + str(answer) + space_equation
    # print(f"{first_line}\n{second_line}\n{third_line}\n{fourth_line}")
    return first_line, second_line, third_line, fourth_line


def valid_number_n_operator(problems):
    # check if the problem is valid number
    error_list = [
        "Error: Too many problems.",
        "Error: Operator must be '+' or '-'.",
        "Error: Numbers must only contain digits.",
        "Error: Numbers cannot be more than four digits.",
    ]
    if len(problems) > 5:
        return False, error_list[0]
    for i in range(len(problems)):
        # fix Still stuck with TypeError: 'int' object is not subscriptable\
        if problems[i][1] != "-" and problems[i][1] != "+":
            return False, error_list[1]
        elif not problems[i][0].isdigit() or not problems[i][2].isdigit():
            print(problems[i][0], problems[i][2])
            return False, error_list[2]
        elif not len(problems[i][0]) <= 4 or not len(problems[i][2]) <= 4:
            return False, error_list[3]
    return True, "No error found"
