HELP_DOC = """
COLUMN OPERATIONS
(version 1.0)
by Angelo Chan

This is a program for performing simple operations on table data such as adding,
subtracting, multiplying, and dividing columns.

Current functionality:
    - Add      (2 columns)
    - Sum      (N columns)
    - Subtract (2 columns)
    - Multiply (2 columns)
    - Product  (N columns)
    - Divide   (2 columns)



USAGE:
    
    python27 Column_Operations.py <input_file> <input_format> [-o <output_file>]
            [-h none|skip|keep] [-a add|sum|sub|mul|pro|div <col_no>...]



MANDATORY:
    
    input_file
        
        The filepath of the input file. No headers allowed.
    
    input_format
        
        The file format of the input file. Acceptable options are:
            tsv - Tab-separated values
            csv - Comma-separated values
            ssv - Space-separated values

OPTIONAL:
    
    output_file
        
        (DEFAULT path generation available)
        
        The filepath of the output file.
    
    none|skip|keep
        
        (DEFAULT: none)
        
        Whether or not the input file contains headers, and if so, what to do
        with them:
            
            {N}one - No headers are present.
            {S}kip - Don't include the headers in the output file.
            {K}eep - Keep the headers in the output file.
    
    add|sum|sub|mul|pro|div
        
        The operation to perform on the subsequent columns. The operations are:
            {ADD}         - Add up two columns
            {SUM}         - Sum up multiple columns
            {SUB}tract    - Subtract the second column from the first one
            {MUL}tiply    - Multiple two columns
            {PRO}duct     - Multiple multiple columns
            {DIV}ide      - Divide the first column by the second one
            {AV}era{G}e   - Calculate the average value of multiple columns.
            con{CAT}enate - Concatenate the text of the two columns.
    
    col_no
        
        The columns on which the operation(s) will be performed.
        
        The column numbers use the index 1 system, not index 0. Ex. To keep the
        first column, enter "1".



EXAMPLES EXPLANATION:
    
    1:
    Add the second and third columns.
    
    2:
    Calculate the average value of the second, third, and fourth columns.
    
    3:
    Divide the second column by the third column and subtract the fifth column
    from the fourth column.
    
    4:
    Add the second and third columns, with a specified output file. Keep the
    headers.

EXAMPLE:
    
    python27 Column_Operations.py Path/Input.tsv tsv -a add 2 3
    
    python27 Column_Operations.py Path/Input.tsv tsv -a avg 2 3 4
    
    python27 Column_Operations.py Path/Input.tsv tsv -a div 2 3 -a sub 4 5
    
    python27 Column_Operations.py Path/Input.tsv tsv -a add 2 3 -h K
            -o Path/Difference.tsv

USAGE:
    
    python27 Column_Operations.py <input_file> <input_format> [-o <output_file>]
            [-h none|skip|keep] [-a add|sum|sub|mul|pro|div <col_no>...]
"""

NAME = "Column_Operations.py"



# Configurations ###############################################################

AUTORUN = True

WRITE_PREVENT = False # Completely prevent overwritting existing files
WRITE_CONFIRM = True # Check to confirm overwritting existing files

PRINT_ERRORS = True
PRINT_PROGRESS = True
PRINT_METRICS = True



# Minor Configurations #########################################################

FILEMOD = "__POST_OP"



# Defaults #####################################################################
"NOTE: altering these will not alter the values displayed in the HELP DOC"

DEFAULT__header = 1 # None



# Imported Modules #############################################################

import _Controlled_Print as PRINT
from _Command_Line_Parser import * # 2.1

from Table_File_Reader import * # 1.1.1



# Enums ########################################################################

class OPERATION:
    ADD=1
    SUM=2
    SUBTRACT=3
    MULTIPLY=4
    PRODUCT=5
    DIVIDE=6
    AVERAGE=7
    CONCATENATE=8



# Strings ######################################################################

STR__use_help = "\nUse the -h option for help:\n\t python "\
"Column_Operations.py -h"



STR__invalid_column_no = """
ERROR: Invalid column number: {s}
Please specify a positive integer.
"""

STR__missing_columns_2 = """
ERROR: Insufficient number of columns specified.
Please specify two columns.
"""

STR__missing_columns_N = """
ERROR: Insufficient number of columns specified.
Please specify at least two columns.
"""

STR__no_operations = """
ERROR: No operations were specified.
Please specify at least one operation.
"""



STR__column_not_found = """
ERROR: Column not found: {c} (0-index)
    AT:             Row: {r}
"""

STR__invalid_value = """
ERROR: Invalid value: {s}
    Found at:
        Row:    {r}
        Column: {c} (0-index)
"""



STR__invalid_hsk = """
ERROR: Invalid option specified: {s}
Please specify one of the following:
    NONE
    SKIP
    KEEP
"""

STR__invalid_operation = """
ERROR: Invalid operation specified: {s}
Please specify one of the following:
    ADD
    SUM
    SUBTRACT
    MULTIPLE
    PRODUCT
    DIVIDE
    AVERAGE
"""

STR__invalid_operation_ENUM = """
ERROR: Invalid operation ENUM
"""



STR__metrics = """
    Rows of data: {A}
     New columns: {B}

    Average value of new columns:
        {C}
"""

STR__metrics_0 = """
    WARNING: No new columns were created.
    
    Rows of data: {A}
"""

STR__no_rows = """
    WARNING: No data in the input file.
"""



STR__calc_begin = "\nRunning Calculate_New_Columns..."

STR__calc_complete = "\nCalculate_New_Columns successfully finished."



# Lists ########################################################################

LIST__add = ["ADD", "Add", "add", "ADDITION", "Addition", "addition"]
LIST__sum = ["SUM", "Sum", "sum"]
LIST__sub = ["SUB", "Sub", "sub", "SUBTRACT", "Subtract", "subtract",
        "SUBTRACTION", "Subtraction", "subtraction"]
LIST__mul = ["MUL", "Mul", "mul", "MULTIPLY", "Multiply", "multiply",
        "MULTIPLICATION", "Multiplication", "multiplication"]
LIST__pro = ["PRO", "Pro", "pro", "PRODUCT", "Product", "product"]
LIST__div = ["DIV", "Div", "div", "DIVIDE", "Divide", "divide", "DIVISION",
        "Division", "division"]
LIST__avg = ["AVG", "Avg", "avg", "AVERAGE", "Average", "average", "MEAN",
        "Mean", "mean"]
LIST__cat = ["CAT", "Cat" ,"cat", "CONCATENATE", "Concatenate", "concatenate"]



# Dictionaries #################################################################

DICT__operation = {}
for i in LIST__add: DICT__operation[i] = OPERATION.ADD
for i in LIST__sum: DICT__operation[i] = OPERATION.SUM
for i in LIST__sub: DICT__operation[i] = OPERATION.SUBTRACT
for i in LIST__mul: DICT__operation[i] = OPERATION.MULTIPLY
for i in LIST__pro: DICT__operation[i] = OPERATION.PRODUCT
for i in LIST__div: DICT__operation[i] = OPERATION.DIVIDE
for i in LIST__avg: DICT__operation[i] = OPERATION.AVERAGE
for i in LIST__cat: DICT__operation[i] = OPERATION.CONCATENATE

DICT__operation_str = {
    OPERATION.ADD: "Addition",
    OPERATION.SUM: "Addition",
    OPERATION.SUBTRACT: "Subtraction",
    OPERATION.MULTIPLY: "Multiplication",
    OPERATION.PRODUCT: "Multiplication",
    OPERATION.DIVIDE: "Division",
    OPERATION.AVERAGE: "Mean"
    }

DICT__header = DICT__none_skip_keep



# Apply Globals ################################################################

PRINT.PRINT_ERRORS = PRINT_ERRORS
PRINT.PRINT_PROGRESS = PRINT_PROGRESS
PRINT.PRINT_METRICS = PRINT_METRICS



# Functions ####################################################################

def Calculate_New_Columns(path_in, delim, path_out, header_mode, operations):
    """
    Generate a series of FASTA files each containing a synthetic chromosome.
    
    @path_in
            (str - filepath)
            The filepath of the input file.
    @delim
            (str)
            The delimiter use by the input file.
    @path_out
            (str - filepath)
            The filepath of the output file.
    @header_mode
            (int) - Pseudo ENUM
            Whether or not the file contains headers, and if so, how they should
            be dealt with. Acceptable options are:
                1:  None - There are no headers in the input file.
                2:  Skip - Skip the header row in the input file.
                3:  Keep - Keep the headers, and generate new ones for the new
                           column(s).
    @operations
            (list<list<int>>)
            A series of lists. Each nested list denotes an operation to be
            performed. The first integer in each nested list corresponds to a
            type of operation, while the subsequent integers correspond to
            column numbers.
            Types of operation are:
                1:  Add up two columns
                2:  Sum up multiple columns
                3:  Subtract the second column from the first one
                4:  Multiple two columns
                5:  Multiple multiple columns
                6:  Divide the first column by the second one
                7:  Calculate the average value of multiple columns.
                8:  Concatenate the text of the two columns.
            Column numbers use an index-0 system.
    
    Return a value of 0 if the function runs successfully.
    Return a value of 1 if there are insufficient columns specified in an
            operation.
    Return a value of 2 if there is a problem with the header.
    Return a value of 3 if one of the rows in the data file does not contain the
            required columns.
    Return a value of 4 if there is another problem.
    
    Tally_Column(str, str, str, int, list<list<int>>) -> int
    """
    PRINT.printP(STR__calc_begin)
    
    # Setup reporting
    total_rows = 0
    total_new_cols = len(operations)
    totals_new = total_new_cols*[0]
    
    # Setup
    total_new_cols_f = float(total_new_cols)
    range_ = range(total_new_cols)
    
    # I/O setup
    f = Table_Reader()
    f.Set_New_Path(path_in)
    f.Set_Delimiter(delim)
    if header_mode != NSK.NONE:
        f.Set_Header_Params([1])
    f.Open()
    o = open(path_out, "w")
    
    # Header
    if header_mode == NSK.KEEP:
        sb = f.Get_Header_Text()
        if sb[-1] == "\n": sb = sb[:-1]
        for op_set in operations:
            if len(op_set) < 3:
                o.close()
                f.close()
                PRINT.printE(STR__missing_columns_N)
                return 1
            op = op_set[0]
            op_str = DICT__operation_str.get(op, "")
            if not op_str:
                o.close()
                f.close()
                PRINT.printE(STR__invalid_operation_ENUM)
                return 2
            sb += delim + op_str
        sb += "\n"
        o.write(sb)
    
    # Main loop
    f.Open()
    while not f.EOF:
        f.Read()
        total_rows += 1
        #
        values = f.current_element # Soft copy
        if f.prev_raw[-1] == "\n":
            sb = f.prev_raw[:-1]
        else:
            sb = f.prev_raw
        for i in range_:
            operation = operations[i]
            op_result = Perform_Operation(values, operation)
            if operation[0] != OPERATION.CONCATENATE:
                totals_new[i] += op_result
                op_result = str(op_result)
            sb += delim + op_result
        sb += "\n"
        o.write(sb)
    
    # Finish
    f.Close()
    o.close()
    PRINT.printP(STR__calc_complete)
    
    # Reporting
    Report_Metrics(total_rows, total_new_cols, totals_new)
    
    # Wrap up
    return 0



def Perform_Operation(data, operation):
    """
    Perform the required operation on a row of data and output the result.
    
    @data
            (list<str>) - Soft copy
            The row of data the operation is to be performed on.
    @operation
            (<list<int>)
            Integers denoting the operation to be performed. The first integer
            corresponds to a type of operation, while the subsequent integers
            correspond to column numbers.
            Types of operation are:
                1:  Add up two columns
                2:  Sum up multiple columns
                3:  Subtract the second column from the first one
                4:  Multiple two columns
                5:  Multiple multiple columns
                6:  Divide the first column by the second one
                7:  Calculate the average value of multiple columns.
                8:  Concatenate the text of the two columns.
            Column numbers use an index-0 system.
    
    Return a sttring if the concatenate operation is performed. Return a number
    otherwise
    
    Perform_Operation(list<str>, list<int>) -> int
    Perform_Operation(list<str>, list<int>) -> float
    Perform_Operation(list<str>, list<int>) -> str
    """
    op = operation[0]
    values = []
    # Parse
    for col_no in operation[1:]:
        try:
            val = data[col_no]
        except:
            PRINT.printE(STR__column_not_found.format(
                    r = total_rows, c = col_no))
            o.close()
            f.close()
            return 3
        if op != OPERATION.CONCATENATE:
            try:
                try:
                    val = int(val)
                except:
                    val = float(val)
            except:
                PRINT.printE(STR__invalid_value.format(
                        s = val, r = total_rows, c = col_no))
                o.close()
                f.close()
                return 3
        values.append(val)
    # Process
    if op == OPERATION.ADD or op == OPERATION.SUM:
        result = sum(values)
    elif op == OPERATION.SUBTRACT:
        result = values[0] - values[1]
    elif op == OPERATION.MULTIPLY or op == OPERATION.PRODUCT:
        result = 1
        for v in values:
            result = result * v
    elif op == OPERATION.DIVIDE:
        result = values[0] / float(values[1])
    elif op == OPERATION.AVERAGE:
        result = sum(values)
        result = result/float(len(values))
    else: # op == OPERATION.CONCATENATE
        result = ""
        for s in values:
            result += s
    # Return
    return result
    



def Report_Metrics(rows, new_cols, totals_new):
    """
    Print a report into the command line interface of the metrics of the
    operation.
    
    @rows
            (int)
            The number of rows of data.
    @new_cols
            (int)
            The number of newly added columns.
    @totals_new
            (list<int>)
            The total values of the newly added columns.
    
    Report_Metrics(int, int, list<int>) -> None
    """
    # Empty
    if rows == 0:
        PRINT.printM(STR__no_rows)
        return
    if new_cols == 0:
        PRINT.printM(STR__metrics_0.format(A = rows))
        return
    # Calculations
    rows_f = float(rows)
    avgs = []
    for t in totals_new:
        avg = t/rows_f
        avgs.append(avg)
    # Strings
    rows = str(rows)
    new_cols = str(new_cols)
    avgs_strs = []
    for i in avgs:
        s = str(i) + "000000"
        s = Trim_Percentage_Str(s, 6)
        avgs_strs.append(s)
    # Pad column (1)
    col_1 = [rows, new_cols]
    col_1 = Pad_Column(col_1, 0, 0, " ", 0)
    rows, new_cols = col_1
    # Pad column (2)
    avgs_strs = Pad_Column(avgs_strs, 0, 0, " ", 0)
    averages_str = "\n        ".join(avgs_strs)
    # Print
    PRINT.printM(STR__metrics.format(A = rows, B = new_cols, C = averages_str))



# Command Line Parsing #########################################################

def Parse_Command_Line_Input__Calculate_New_Columns(raw_command_line_input):
    """
    Parse the command line input and call the Generate_Synthetic_Genome function
    with appropriate arguments if the command line input is valid.
    """
    PRINT.printP(STR__parsing_args)
    # Remove the runtime environment variable and program name from the inputs
    inputs = Strip_Non_Inputs(raw_command_line_input, NAME)
    
    # No inputs
    if not inputs:
        PRINT.printE(STR__no_inputs)
        PRINT.printE(STR__use_help)
        return 1
    
    # Help option
    if inputs[0] in LIST__help:
        print(HELP_DOC)
        return 0
    
    # Initial validation
    if len(inputs) < 2:
        PRINT.printE(STR__insufficient_inputs)
        PRINT.printE(STR__use_help)
        return 1
    
    # Setup mandatory inputs
    path_in = inputs.pop(0)
    input_format = inputs.pop(0)
    
    # Validate mandatory inputs
    valid = Validate_Read_Path(path_in)
    if valid == 1:
        PRINT.printE(STR__IO_error_read.format(f = path_in))
        PRINT.printE(STR__use_help)
        return 1
    delim = Validate_Table_File_Format(input_format)
    if not delim:
        PRINT.printE(STR__invalid_table_format.format(f = table_format))
        PRINT.printE(STR__use_help)
        return 1
    
    # Set up rest of the parsing
    path_out = Generate_Default_Output_File_Path_From_File(path_in, FILEMOD,
            True)
    header = DEFAULT__header
    operations = []
    
    # Validate optional inputs (except output path)
    while inputs:
        arg = inputs.pop(0)
        flag = 0
        try: # Following arguments
            if arg in ["-o", "-h"]:
                arg2 = inputs.pop(0)
            elif arg in ["-a"]:
                arg2 = inputs.pop(0)
                other_args = []
                while inputs and inputs[0][0] != "-":
                    temp = inputs.pop(0)
                    other_args.append(temp)
            else: # Invalid
                arg = Strip_X(arg)
                PRINT.printE(STR__invalid_argument.format(s = arg))
                PRINT.printE(STR__use_help)
                return 1
        except:
            PRINT.printE(STR__insufficient_inputs)
            PRINT.printE(STR__use_help)
            return 1
        if arg == "-o":
            path_out = arg2
        elif arg == "-h":
            if arg2 in LIST__none: header = NSK.NONE
            elif arg2 in LIST__skip: header = NSK.SKIP
            elif arg2 in LIST__keep: header = NSK.KEEP
            else:
                PRINT.printE(STR__invalid_hsk.format(s = arg2))
                return 1
        else: # arg == "-a"            
            function = Validate_Operation(arg2)
            if not function:
                PRINT.printE(STR__invalid_operation.format(s = arg2))
                return 1
            if len(other_args) < 2:
                if operation in [OPERATION.SUBTRACT, OPERATION.DIVIDE]:
                    PRINT.printE(STR__missing_columns_2)
                    return 1
                else:
                    PRINT.printE(STR__missing_columns_N)
                    return 1
            col_nos = []
            for col_str in other_args:
                col_no = Validate_Int_Positive(col_str)
                if col_no == -1:
                    PRINT.printE(STR__invalid_column_no.format(s = col_str))
                    return 1
                col_nos.append(col_no-1)
            operation = [function] + col_nos
            operations.append(operation)
    
    # Validate operations
    if len(operations) < 1:
        PRINT.printE(STR__no_operations)
        return 1
    
    # Validate output paths
    valid_out = Validate_Write_Path(path_out)
    if valid_out == 2: return 0
    if valid_out == 3:
        PRINT.printE(STR__IO_error_write_forbid)
        return 1
    if valid_out == 4:
        PRINT.printE(STR__In_error_write_unable)
        return 1
    
    # Run program
    exit_state = Calculate_New_Columns(path_in, delim, path_out, header,
            operations)
    
    # Exit
    if exit_state == 0: return 0
    else: return 1



def Validate_Operation(string):
    """
    Validates the string given which is supposed to indicate an operation to be
    performed on two or more data columns.
    
    Return 0 if the string is invalid.
    Return an ENUM integer corresponding to an operation if the string is valid.
    """
    if string in LIST__add: return OPERATION.ADD
    elif string in LIST__sum: return OPERATION.SUM
    elif string in LIST__sub: return OPERATION.SUBTRACT
    elif string in LIST__mul: return OPERATION.MULTIPLY
    elif string in LIST__pro: return OPERATION.PRODUCT
    elif string in LIST__div: return OPERATION.DIVIDE
    elif string in LIST__avg: return OPERATION.AVERAGE
    elif string in LIST__cat: return OPERATION.CONCATENATE
    else: return 0

def Validate_Write_Path(filepath):
    """
    Validates the filepath of the input file.
    Return 0 if the filepath is writtable.
    Return 1 if the user decides to overwrite an existing file.
    Return 2 if the user declines to overwrite an existing file.
    Return 3 if the file exists and the program is set to forbid overwriting.
    Return 4 if the program is unable to write to the filepath specified.
    
    Validate_Write_Path(str) -> int
    """
    try:
        f = open(filepath, "U")
        f.close()
    except: # File does not exist. 
        try:
            f = open(filepath, "w")
            f.close()
            return 0 # File does not exist and it is possible to write
        except:
            return 4 # File does not exist but it is not possible to write
    # File exists
    if WRITE_PREVENT: return 3
    if WRITE_CONFIRM:
        confirm = raw_input(STR__overwrite_confirm.format(f=filepath))
        if confirm not in LIST__yes: return 2
    # User is not prevented from overwritting and may have chosen to overwrite
    try:
        f = open(filepath, "w")
        f.close()
        if WRITE_CONFIRM: return 1 # User has chosen to overwrite existing file
        return 0 # Overwriting existing file is possible
    except:
        return 4 # Unable to write to specified filepath



# Main Loop ####################################################################

if AUTORUN and (__name__ == "__main__"):
    exit_code = Parse_Command_Line_Input__Calculate_New_Columns(sys.argv)



