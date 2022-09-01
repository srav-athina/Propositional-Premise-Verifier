import itertools

LOGICAL_CONNECTORS = ["¬", "∧", "∨", "→", "⇔"]
prs = ["(", ")"]

def is_valid(premises, conclusion):
    # Identify set of models and build truth table
    models = identify_models(premises) # Slide 54
    print(models)
    truth_table = build_truth_table(models) # Slide 54
    # Add premises
    for premise in premises:
        add_premise(premise, truth_table)
    # Add conclusion
    add_premise(conclusion, truth_table)
    # Print out the truth table (make sure you full screen) and check critical rows
    print_truth_table(truth_table)
    return check_critical_rows(premises, conclusion, truth_table)
    

def identify_models(premises):
    models = set() 
    for premise in premises:
        chars = list(premise)
        letters = filter(lambda c: c not in LOGICAL_CONNECTORS and c not in prs, chars)
        models.update(letters)
    return models

def build_truth_table(models):
    booleans = [[] for i in range(len(models))]
    for row in itertools.product([False,True], repeat=len(models)):
        for i in range(len(row)):
            booleans[i].append(row[i])
    truth_table = {}
    for model, column in zip(models, booleans):
        truth_table[model] = column
    return truth_table

def add_premise(premise, truth_table):
    if len(premise) == 1:
        return
    tokens = []
    par_count = 0
    cur_string = ""
    for i in premise:
        if i == "(":
            par_count += 1
            if par_count > 1 or (par_count == 1 and cur_string and cur_string[0] == "¬"):
                cur_string += "("
        elif i == ")":
            par_count -= 1
            if par_count > 0 or (par_count == 0 and cur_string and  cur_string[0] == "¬"):
                cur_string += ")"
            if par_count == 0:
                tokens.append(cur_string)
                cur_string = ""
        elif par_count > 0:
            cur_string += i
        elif i in LOGICAL_CONNECTORS and i != "¬":
            tokens.append(i)
        elif i == "¬":
            cur_string += "¬"
        else:
            if cur_string == "¬":
                cur_string += i
                tokens.append(cur_string)
                cur_string = ""
            else:
                tokens.append(i)
    if len(tokens) > 1:
        for token in tokens:
            if token not in LOGICAL_CONNECTORS:
                add_premise(token, truth_table)
    elif tokens[0][0] == "¬" and len(tokens[0]) > 2:
        add_premise(tokens[0][2:-1], truth_table)
    update_truth_table(tokens, premise, truth_table)

def update_truth_table(premise, premise_string, truth_table):
    length = len(list(truth_table.values())[0])
    booleans = []
    for i in range(length):
        booleans.append(evaluate(premise, truth_table, i))
    truth_table[premise_string]= booleans

def evaluate(premise, truth_table, index):
    if len(premise) == 1:
        if len(premise[0]) > 2:
            return not truth_table[premise[0][2:-1]][index]
        else:
            return not truth_table[premise[0][1]][index]
    lhs = premise[0]
    rhs = premise[2]
    lhs_value = truth_table[lhs][index]
    rhs_value = truth_table[rhs][index]
    operator = premise[1]
    if operator == "∧":
        return lhs_value and rhs_value
    elif operator == "∨":
        return lhs_value or rhs_value
    elif operator == "→":
        if lhs_value and not rhs_value:
            return False
        return True
    else:
        return lhs_value == rhs_value

def check_critical_rows(premises, conclusion, truth_table):
    conclusion_values = truth_table[conclusion]
    premises_values = [truth_table[premise] for premise in premises]
    for i in range(len(conclusion_values)):
        is_critical = True
        for premise_value in premises_values:
            if not premise_value[i]:
                is_critical = False
                break
        if is_critical and not conclusion_values[i]:
            return False
    return True
        
## DEBUG FUNCTIONS
def print_truth_table(truth_table):
    header = list(truth_table.keys())
    rows = [[] for i in range(len(truth_table[header[0]]))]
    for model, values in truth_table.items():
        for i in range(len(values)):
            rows[i].append(values[i])
    format_row = "{:>14}" * (len(header)+1)
    print(format_row.format("", *header))
    for row in rows:
        print(format_row.format("", *row))
