HELP_DOC = """
MULTITOOL FOR TABLES
(version 1.0)
by Angelo Chan

This is a multi-purpose tool for parsing table files. It combines the
functionality of the following tools contained within the Table_Tools package:
    - Add_Column.py
    - Column_Operations.py
    - Table_to_Table.py



The functionality of Multitool_For_Tables includes:
    - Converting the file format
    - Retaining, creating, or omitting column headers
    - Retaining, duplicating, or omitting different columns
    - Adding new columns with a set value
    - Adding new columns which are derived from data in existing columns
    - Filtering individual rows based on user-specified criteria
    - Omit rows with non-unique values in a specific combination of columns

The order in which columns are specified (whether it's keeping an existing
column, or adding a new column of some kind) is the order they will appear in
the output file.



Accepted file formats:
    - TSV (Tab-Separated Values)
    - CSV (Comma-Separated Values)
    - SSV (Space-Separated Values)

Filtering options (For data in the specified column):
    - EQUALS str        (Data must match the specified text exactly)
    - NOT EQUALS str    (Data must not match the specified value exactly)
    - CONTAINS          (Data must contain the specified value/substring)
    - NOT CONTAINS      (Data must not contain the specified value/substring)
    - GREATER THAN      (Data must be strictly greater than the specified value)
    - GREAQUALS         (Data must be equal to or greater than the specified
                        value)
    - LESS THAN         (Data must be strictly less than the specified value)
    - LEQUALS           (Data must be equal to or less than the specified value)
    - EQUALS int        (Data must match the specified value exactly)
    - NOT EQUALS int    (Data must not match the specified value exactly)
    - EQUALS float      (Data must match the specified value exactly)
    - NOT EQUALS float  (Data must not match the specified value exactly)

Valid column operations include:
    - ADD       (2 columns)
    - SUM       (N columns)
    - SUBTRACT  (2 columns)
    - MULTIPLE  (2 columns)
    - PRODUCT   (N columns)
    - DIVIDE    (2 columns)



USAGE:
    
    python27 Multitool_For_Tables.py <input_path> <{input_format}>
            [-o <output_path> {output_format}]
            [-h keep|skip|rearrange N|C <number>|<character>]... [-a]
            [-k <col_nos>]... [-f <col_no> <criteria> C|V <col_no>|<value>]...
            [-n <header> <contents>]... [-c <col_operation> <col_nos>]...
            [-u <col_nos>]



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
    
    output_format
        
        (DEFAULT: same as input_format)
        
        The file format of the output file. If no format is specified, the
        output format will be the same as the input format. Acceptable options
        are:
            tsv - Tab-separated values
            csv - Comma-separated values
            ssv - Space-separated values
    
    keep|skip|rearrange
        
        keep
            Keep lines at the start of the file.
        
        skip
            Skip lines at the start of the file.
        
        rearrange
            Treat these lines as column headers. Rearrange and keep them where
            applicable.
    
    N|C
        
        N
            Keep/skip/rearrange a set [n]umber of lines.
        
        C
            Keep/skip/rearrange lines that begin with a given [c]haracter.
    
    number
        
        If option "N" was chosen, then this specifies the number of lines to
        Keep/skip/rearrange.
    
    character
        
        If the option "C" was chosen, then this specifies which character a line
        should start with to keep/skip/rearrange it.
    
    (-a)
        
        Create new column headers.
    
    col_nos
        
        An underscore separated list of column numbers. Users can also use "ALL"
        to specify all columns.
        
        The "ALL" option will calculate column numbers after skip any header
        rows designated as keep/skip.
        
        The column numbers use the index 1 system, not index 0. Ex. To specify
        the first column, use "1".
        
        (-k)
            This specifies which columns to keep.
        
        (-c)
            This specifies which columns to perform the operation on.
            For add, multiply, sum, and product, the order doesn't matter.
            For subtract, the first number in the list is the minuend, (the
            "positive" number) while the second number in the list is the
            subtrahend. (the "negative" number)
            For division, the first number in the list is the divided, (the
            numerator, or the number on top in a fraction) while the second
            number in the list is the divisor. (the denominator, or the number
            on the bottom in a fraction)
        
        (-u)
            This specifies the columns which are to be combined to form the key.
            If multiple rows have the same combination of values in the
            specified columns, only the first row will be retained. This is not
            the same as specifying that the combination of values in the "key"
            columns need to be unique across the entire file. If no unique
            columns are specified, no rows of data will be filtered out.
    
    col_no
        
        The column number of a column.
        
        In the context of "-f", the first <col_no> denotes the column whose
        value is being filtered on. If the "C" option is taken, the second
        <col_no> denotes the column containing the data being used for the
        filter.
        
        Ex. "-f 1 cont c 2" specifies that the string in column 2 must be a
        substring of the string in column 1.
        
        The column numbers use the index 1 system, not index 0. Ex. To keep the
        first column, enter "1".
    
    criteria
    
        The filtering criteria to use. Valid criteria are:
                    
            STR_EQ      Equals <string query>
            STR_EQ!     Does not equal <string query>
            CONT        Contains <string query>
            CONT!       Does not contain <string query>
            ">"         Greater than <number query>
            "<"         Less than <number query>
            ">="        qual to or greater than <number query>
            "<="        Equal to or less than <number query>
            INT_EQ      Equals <int query>
            INT_EQ!     Does not equal <int query>
            FLO_EQ      Equals <float query>
            FLO_EQ!     Does not equal <float query>
                
        The "Equals" and "Does not equal" operators can compare ints with
        floats, but may not work perfectly.
    
    C|V
        
        C
            Use the data in another column for the filtering.
        
        V
            Use a specific value for the filtering.
    
    value
    
        The value being used for filtering. Depending on <criteria>, this will
        be treated as either a string, integer, or float.
    
    header
    
        The header used for the newly created column.
    
    contents
    
        The contents of the newly created column.
    
    col_operation
    
        The operation to perform on the columns. The operations are:
            {ADD}         - Add up two columns
            {SUM}         - Sum up multiple columns
            {SUB}tract    - Subtract the second column from the first one
            {MUL}tiply    - Multiple two columns
            {PRO}duct     - Multiple multiple columns
            {DIV}ide      - Divide the first column by the second one
            {AV}era{G}e   - Calculate the average value of multiple columns
            con{CAT}enate - Concatenate the text of the two columns
            {DIF}ference  - Calculate the difference between two columns



EXAMPLES EXPLANATION:
    
    01:
    Convert a TSV file to a CSV file. Retain all data.
    
    02:
    Only keep the first 5 columns of the file.
    
    03:
    The file contains a header comments section consisting of lines which begin
    with a hash, and then contains column headers. Omit the comments section,
    but retain the headers.
    
    04:
    Keep only the data entries which have the letters "A", "B", and "C" in
    column 2, in any order.
    
    05:
    Keep only the data entries which do not contain have any of the letters "X",
    "Y", and "Z" anywhere in column 2, in any order.
    
    06:
    Keep only the data entries whose value in column 3 is greater than or equal
    to 1000, and also greater than the value in column 4.
    
    07:
    Keep only the data entries whose numerical value in column 5 is exactly 150.
    Round the decimal numbers down (floor) before making the comparison.
    
    08:
    Keep the 10th, 8th, and 9th columns. Create a new column for notes. Then
    include the 5th column. The table has headers. Keep them.
    
    09:
    Keep the first 5 columns of the file. Calculate the difference between
    columns 2 and 3. Calculate column 3 minutes column 2. Calculate the sum of
    columns 4 and 5. The original file has no column headers. Create new ones.
    
    10:
    Keep all the data, but remove all duplicate entries after the first
    occurence. Duplicates are defined by the value in column 1.

EXAMPLES:
    
    01:
    python27 Multitool_For_Tables.py Path/Input.tsv tsv -o Path/Output.csv csv
            -k ALL
    
    02:
    python27 Multitool_For_Tables.py Path/Input.tsv tsv -k 1_2_3
    
    03:
    python27 Multitool_For_Tables.py Path/Input.tsv tsv -k ALL -h skip C "#"
            -h keep N 1
    
    04:
    python27 Multitool_For_Tables.py Path/Input.tsv tsv -f 2 cont v A
            -f 2 cont v B -f 2 cont v C
    
    05:
    python27 Multitool_For_Tables.py Path/Input.tsv tsv -f 2 cont! v X
            -f 2 cont! v Y -f 2 cont! v Z
    
    06:
    python27 Multitool_For_Tables.py Path/Input.tsv tsv -f 3 ">=" v 1000
            -f 3 ">" c 4
    
    07:
    python27 Multitool_For_Tables.py Path/Input.tsv tsv -f 5 int_eq v 150
    
    08:
    python27 Multitool_For_Tables.py Path/Input.tsv tsv -k 10_8_9
            -n Notes Placeholder_Text -k 5
    
    09:
    python27 Multitool_For_Tables.py Path/Input.tsv tsv -k 1_2_3_4_5
            -c difference 2_3 -c substract 3_2 -c sum 4_5 -a
    
    10:
    python27 Multitool_For_Tables.py Path/Input.tsv tsv -u 1 -k ALL 



USAGE:
    
    python27 Multitool_For_Tables.py <input_path> <{input_format}>
            [-o <output_path> {output_format}]
            [-h keep|skip|rearrange N|C <number>|<character>]... [-a]
            [-k <col_nos>]... [-f <col_no> <criteria> C|V <col_no>|<value>]...
            [-n <header> <contents>]... [-c <col_operation> <col_nos>]...
            [-u <col_nos>]
"""



SUPPLEMENTARY_DOC = """
Some alternative methods for specifying criteria, which don't involve
problematic characters ("!", ">", "<", "=") include:
    
    STR_EQ!     STR_N_EQ, STRING_NOT_EQUAL
    CONT!       N_CONT, NOT_CONTAINS
    ">"         GREATER, GREATER_THAN
    "<"         LESS, LESS_THAN
    ">="        GR_EQ, GREQUALS
    "<="        LS_EQ, LEQUALS
    INT_EQ!     INT_N_EQ, INTEGER_NOT_EQUAL
    FLO_EQ!     FLO_N_EQ, FLOAT_NOT_EQUAL
"""



# Configurations ###############################################################

AUTORUN = True

WRITE_PREVENT = False # Completely prevent overwritting existing files
WRITE_CONFIRM = True # Check to confirm overwritting existing files

PRINT_ERRORS = True
PRINT_PROGRESS = True
PRINT_METRICS = True



# Imported Modules #############################################################

import sys

import _Controlled_Print as PRINT
from _Command_Line_Parser import * # 2.1

from Table_File_Reader import * # 1.1.1



# Enums ########################################################################



# Strings ######################################################################



# Lists ########################################################################



# Dictionaries #################################################################



# Apply Globals ################################################################

PRINT.PRINT_ERRORS = PRINT_ERRORS
PRINT.PRINT_PROGRESS = PRINT_PROGRESS
PRINT.PRINT_METRICS = PRINT_METRICS



# Functions ####################################################################



# Command Line Parsing #########################################################

def Parse_Command_Line_Input__Multitool_For_Tables(raw_command_line_input):
    """
    Parse the command line input and call the Multitool_For_Tables function with
    appropriate arguments if the command line input is valid.
    """    
    # Safe exit
    return 0



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
    exit_code = Parse_Command_Line_Input__Multitool_For_Tables(sys.argv)


