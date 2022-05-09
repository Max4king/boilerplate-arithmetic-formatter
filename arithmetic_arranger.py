def arithmetic_arranger(problems, solution=False):
    arranged_problems = []

    # creates a new list to store the problems
    for i in range(len(problems)):
        arranged_problems.append(problems[i].split())

    # check if the problem is valid number
    valid = valid_number_n_operator(arranged_problems)
    if not valid[0]:
        return valid[1]

    return arranged_problems,valid[1]

def valid_number_n_operator(problems):
    # check if the problem is valid number
    error_list = [
        "Error: Too many problems.",
        "Error: Operator must be '+' or '-'.",
        "Error: Numbers must only contain digits.",
        "Error: Numbers cannot be more than four digits."]
    if (len(problems) > 5):
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

print("This is the last line print:",arithmetic_arranger(["32 - 698", "3801 - 2", "45 + 43", "123 + 49","34 - 44"]))