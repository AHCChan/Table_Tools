HELP_DOC = """
ADD COLUMN
(version 1.0)
by Angelo Chan

This is a program to insert new columns into a table file, filled with the
specified string.

Insertions will take place in the order specified. If columns are not specified
in a right-to-left order, the final output will not have all columns in their
specified column number.

(Ex. If the user specifies inserting a blank column into column "4", and then
into column "2", the final outcome will be a blank column in columns 2 and 5.)



USAGE:
    
    python27 Add_Column.py <input_path> <input_format> [-o <output_path>] [-a
            <col_no> <column_header> <body_text>] [-h <header>]



MANDATORY:
    
    input_path
        
        The filepath of the input file.
    
    input_format
        
        The file format of the input file. Acceptable options are:
            tsv - Tab-separated values
            csv - Comma-separated values
            ssv - Space-separated values

OPTIONAL:
    
    output_path
        
        (DEFAULT path generation available)
        
        The filepath of the output file.
    
    col_no
        
        The column number where the following column header and body text will
        be inserted. Follows an index-1 system, so to insert into the very first
        column, <col_no> should be 1. Also applies allows negative indexes to
        insert from the end, so to insert into the last column, <col_no> should
        be -1.

        When inserted into an existing column, its contents will all be shifted
        to the right.

        To add a column at the very end and not displace the existing contents,
        <col_no> should be 0.
    
    column_header
        
        The column header. Must be enclosed by inverted commas. This must be
        included even if there are no headers.
    
    body_text
        
        The string to be inserted. Inverted commas need to be escaped or
        enclosed in other inverted commas.
    
    header
        
        (DEFAULT: N)
        
        The string to be inserted. Inverted commas need to be escaped or
        enclosed in other inverted commas.



EXAMPLES EXPLANATION:
    
    1:
    Add an empty column to the left of the TSV table.
    
    2:
    Add an empty column to the right of the CSV table.
    
    3:
    Add an empty column to the left and to the right of the TSV table.
    
    4:
    The fourth column will now be titled "Preferred Name" and contain the text
    "(Same as given name)" in the body. The original contents of the table from
    the fourth column onwards will be shifted to the right. The file is a CSV.

EXAMPLES:
    
    python27 Add_Column.py data\data_file.tsv tsv -a 1 "" "" -h N
    
    python27 Add_Column.py data\data_file.tsv tsv -a -1 "" "" -h N
    
    python27 Add_Column.py data\data_file.tsv tsv -a 1 "" "" -a -1 "" "" -h N
    
    python27 Add_Column.py data\data_file.tsv tsv -o data\new_data_file.tsv -a 4
            "Preferred Name" "(Same as given name)" -h Y

USAGE:
    
    python27 Add_Column.py <input_file> <input_format> [-o <output_file>] [-a
            <col_no> <column_header> <body_text>]
"""

NAME = "Add_Column.py"



# Configurations ###############################################################

AUTORUN = True

WRITE_PREVENT = False # Completely prevent overwritting existing files
WRITE_CONFIRM = True # Check to confirm overwritting existing files

PRINT_ERRORS = True
PRINT_PROGRESS = True
PRINT_METRICS = True



# Minor Configurations #########################################################

FILEMOD__ADDED =   "__ADDED"



# Defaults #####################################################################
"NOTE: altering these will not alter the values displayed in the HELP DOC"

DEFAULT__headers = False



# Imported Modules #############################################################

import _Controlled_Print as PRINT
from _Command_Line_Parser import *

from Table_File_Reader import *



# Strings ######################################################################

STR__use_help = "\nUse the -h option for help:\n\t python "\
"Add_Column.py -h"


STR__invalid_headers = """
ERROR: Invalid value given for whether or not there are headers."""



STR__metrics = "Rows in file: {N}"



STR__add_columns_begin = "\nRunning Add_Columns..."

STR__add_columns_complete = "\nAdd_Columns successfully finished."



# Lists ########################################################################

LIST__yes = ["Y", "y", "YES", "Yes", "yes", "T", "t", "TRUE", "True", "true"]
LIST__no = ["N", "n", "NO", "No", "no", "F", "f", "FALSE", "False", "false"]



# Apply Globals ################################################################

PRINT.PRINT_ERRORS = PRINT_ERRORS
PRINT.PRINT_PROGRESS = PRINT_PROGRESS
PRINT.PRINT_METRICS = PRINT_METRICS



# Functions ####################################################################

def Add_Columns(path_in, delimiter, path_out, additions, headers):
    """
    Generate a series of FASTA files each containing a synthetic chromosome.
    
    @path_in
            (str - filepath)
            The filepath of the input file where the original data is saved.
    @delimiter
            (str)
            The delimiter used to separate the different columns.
    @path_out
            (str - dirpath)
            The filepath of the output file where the new data is outputted.
    @additions
            (list<[int, str, str]>)
            A list of the contents to be added. The information for each column
            is stored in a sublist. Each sublist consists of:
            
                1)  The column number where the following column header and body
                    text will be inserted. Follows an index-1 system, so to
                    insert into the very first column, this number should be 1.
                    Also applies allows negative indexes to insert from the end,
                    so to insert into the last column, this number should be -1.
                    
                    When inserted into an existing column, its contents will all
                    be shifted to the right.
                    
                    To add a column at the very end and not displace the
                    existing contents, this number should be 0.
            
                2)  The column header. Must be enclosed by inverted commas.
    
                3)  The string to be inserted. Must be enclosed by inverted
                    commas.
    @headers
            (bool)
            Whether or not the input file contains headers.
    
    Return a value of 0 if the function runs successfully.
    Return a value of 1 if there is a problem.
    
    Add_Columns(str, str, str, list<[int, str, str]>) -> int
    """
    # Setup reporting
    row_count = 0
    
    # Unpacking
    additions_h = []
    additions_b = []
    for i in additions:
        additions_h.append([i[0], i[1]])
        additions_b.append([i[0], i[2]])
    
    # Starting up
    f = Table_Reader()
    f.Set_New_Path(path_in)
    f.Set_Delimiter(delimiter)
    f.Open()
    o = open(path_out, "w")
    
    PRINT.printP(STR__add_columns_begin)
    
    # Header
    if headers:
        f.Read()
        values = f.Get()
        new_values = Add_Values(values, additions_h)
        new_str = delimiter.join(new_values) + "\n"
        o.write(new_str)
    
    # Main loop
    while not f.EOF:
        f.Read()
        row_count += 1
        values = f.Get()
        new_values = Add_Values(values, additions_b)
        new_str = delimiter.join(new_values) + "\n"
        o.write(new_str)
    
    # Finish
    f.Close()
    o.close()
    PRINT.printP(STR__add_columns_complete)
    
    # Reporting
    PRINT.printM(STR__metrics.format(N=row_count))
    
    # Wrap up
    return 0

def Add_Values(original_list, additions):
    """
    Add new values to an original list of values and return the modified list.
    New values will be added in the order specified.
    
    @original_list
        (list<str>)
        The original list of values.
    @additions
        (list<[int,str]>)
        Sets of integer-string pairs. The integer specifies which column the
        string should be inserted into. If the string is inserted into an
        existing column, it will push the contents of that column, and all
        subsequent columns, to the right.
        This follows an index-1 system, so to insert into the very first column,
        the column number should be 1. Also applies allows negative indexes to
        insert from the end, so to insert into the last column, <col_no> should
        be -1. To add a column at the very end and not displace the existing
        contents, the column number should be 0.
    
    Add_Values(list<str>, list<[int,str]>) -> list<str>
    """
    original_list = list(original_list) #   Remove this line to speed things up,
    #                                       but will cause the original list to 
    #                                       be modified.
    for pair in additions:
        coords, value = pair
        if coords == 0:
            original_list.append(value)
        elif coords < 0:
            original_list.insert(coords, value)
        else:
            coords = coords - 1
            original_list.insert(coords, value)
    return original_list



# Command Line Parsing #########################################################

def Parse_Command_Line_Input__Add_Column(raw_command_line_input):
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
    
    # Initial validation (Redundant in current version)
    if len(inputs) < 3:
        PRINT.printE(STR__insufficient_inputs)
        PRINT.printE(STR__use_help)
        return 1
    
    # Validate mandatory inputs
    path_in = inputs.pop(0)
    valid = Validate_Read_Path(path_in)
    if valid == 1:
        PRINT.printE(STR__IO_error_read.format(f = path_in))
        PRINT.printE(STR__use_help)
        return 1
    table_type = inputs.pop(0)
    delim = Validate_Table_Type(table_type)
    if not delim:
        PRINT.printE(STR__invalid_table_format(f = table_type))
        PRINT.printE(STR__use_help)
        return 1
    
    # Set up rest of the parsing
    headers = DEFAULT__headers
    additions = []
    path_out = Generate_Default_Output_File_Path_From_File(path_in,
            FILEMOD__ADDED, True)
    
    # Validate optional inputs (except output path)
    while inputs:
        arg = inputs.pop(0)
        flag = 0
        try: # Following arguments
            if arg in ["-o", "-h"]:
                arg2 = inputs.pop(0)
            elif arg in ["-a"]:
                arg2 = inputs.pop(0)
                arg3 = inputs.pop(0)
                arg4 = inputs.pop(0)
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
            headers = Validate_Bool(arg2)
            if headers == None:
                PRINT.printE(STR__invalid_headers.format(s = arg2))
                return 1
        else: # arg == "-a"
            try:
                coord = int(arg2)
            except:
                PRINT.printE(STR__invalid_int.format(s = arg2))
                PRINT.printE(STR__use_help)
                return 1
            additions.append([coord, arg3, arg4])
    
    # Validate output paths
    valid_out = Validate_Write_Path(path_out)
    if valid_out == 2: return 0
    if valid_out == 3:
        printE(STR__IO_error_write_forbid)
        return 1
    if valid_out == 4:
        printE(STR__In_error_write_unable)
        return 1
    
    # Run program
    exit_state = Add_Columns(path_in, delim, path_out, additions, headers)
    
    # Exit
    if exit_state == 0: return 0
    else: return 1


    
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
    exit_code = Parse_Command_Line_Input__Add_Column(sys.argv)
