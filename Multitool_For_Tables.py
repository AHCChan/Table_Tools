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
            [-o <output_path> {output_format}] [-a]
            [-h keep|skip|rearrange C|N|(none) <number>|<character>|(none)]...
            [-k <col_nos>]...
            [-f include|exclude <col_no> <criteria> C|V <col_no>|<value>]...
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
            Keep lines at the start of the file as is.
        
        skip
            Skip lines at the start of the file.
        
        rearrange
            Treat these lines as column headers. Rearrange and keep them where
            applicable. [keep] and [skip] may be used an unlimited number of
            times, but [rearrange] may only be used once, and must be the last
            header section specified using "-h".
    
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
        
        A list of column numbers. Users can use one of several formats to
        specify the column numbers:
                
            1:  "ALL" to specify all columns.
            
            2:  Underscore-separated list.
                    1_2_3 specifies columns 1, 2, and 3
            
            3:  Square bracket indices. (but with a non-standard indeces system)
                    [:3] specifies the first 3 columns
                    [-3:] specifies the last 3 columns
                    [4:6] specifies columns 4, 5, and 6
                    [2:-2] specifies all columns except the first and last
        
        Negative indices and the "ALL" option are derived from the first row not
        designated as keep/skip by the header specifications.
        
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
    
    include|exclude
        
        include
            Require that all rows of data fulfil the following criteria.
        
        exclude
            Exclude all rows of data which fulfil the following criteria.
    
    criteria
        
        The filtering criteria to use. Valid criteria are:
            
            str_eq      Equals <string query>
            str_eq!     Does not equal <string query>
            cont        Contains <string query>
            cont!       Does not contain <string query>
            ">"         Greater than <number query>
            ">="        Equal to or greater than <number query>
            "<"         Less than <number query>
            "<="        Equal to or less than <number query>
            int_eq      Equals <int query>
            int_eq!     Does not equal <int query>
            flo_eq      Equals <float query>
            flo_eq!     Does not equal <float query>
        
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
            {GEO}metric   - Calculate the geometric mean of multiple columns



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
    python27 Multitool_For_Tables.py Path/Input.tsv tsv -k [1:5]
            -c difference 2_3 -c substract 3_2 -c sum 4_5 -a
    
    10:
    python27 Multitool_For_Tables.py Path/Input.tsv tsv -u 1 -k ALL 



USAGE:
    
    python27 Multitool_For_Tables.py <input_path> <{input_format}>
            [-o <output_path> {output_format}] [-a]
            [-h keep|skip|rearrange C|N|(none) <number>|<character>|(none)]...
            [-k <col_nos>]...
            [-f include|exclude <col_no> <criteria> C|V <col_no>|<value>]...
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
from _Command_Line_Parser import * # 2.3

from Table_File_Reader import * # 1.1.1



# Enums ########################################################################

class HEADER_TYPE:
    CHAR=1
    NUM=2



class CRITERIA:
    STR_EQ=1
    STR_NOT_EQ=2
    CONTAINS=3
    NOT_CONTAIN=4
    GREATER_THAN=5
    GREAQUALS=6
    LESS_THAN=7
    LEQUALS=8
    INT_EQ=9
    INT_NOT_EQ=10
    FLO_EQ=11
    FLO_NOT_EQ=12

class FILTER_TYPE:
    COL=1
    VAl=2



class OPERATION:
    ADD=1
    SUM=2
    SUB=3
    MUL=4
    PRO=5
    DIV=6
    AVG=7
    CAT=8
    DIF=9
    GEO=10



class COL_TYPE:
    KEEP=1
    NEW=2
    CALC=3



# Strings ######################################################################

STR__use_help = "\nUse the -h option for help:\n\t python "\
"Multitool_For_Tables.py -h"



STR__invalid_ksr = """
ERROR: Invalid header treatment option: {s}
Please specify one of the following:
    keep
    skip
    rear
"""
STR__invalid_header_type = """
ERROR: Invalid type action to take: {s}
Please specify one of:
    num
    char
"""



STR__invalid_column_no = """
ERROR: Invalid column number: {s}
Please specify a positive integer.
"""
STR__invalid_column_nos = """
ERROR: Invalid column numbers: {s}
Please specify either "ALL", an underscore-separate list of positive integers,
or a range of column numbers denoted by square brackets and colons.
"""
STR__missing_columns_2 = """
ERROR: Insufficient number of columns specified.
Please specify two columns.
"""
STR__missing_columns_N = """
ERROR: Insufficient number of columns specified.
Please specify at least two columns.
"""
STR__column_not_found = """
ERROR: Column not found: {c} (0-index)
    AT:             Row: {r}
"""

STR__invalid_criteria = """
ERROR: Invalid filtering criteria: {s}
Please specify one of the following:
    str_eq
    str_eq! (or str_not_eq)
    cont
    cont!
    ">"     (or greater_than)
    ">="    (or greaquals)
    "<"     (or lesser_than)
    "<="    (or lequals)
    int_eq
    int_eq! (or int_not_eq)
    flo_eq
    flo_eq! (or flo_not_eq)
"""
STR__invalid_criteria_type = """
ERROR: Invalid type action to take: {s}
Please specify one of:
    col
    val"""



STR__m4t_begin = "\nRunning Multitool_For_Tables..."
STR__m4t_complete = "\nMultitool_For_Tables successfully finished."



STR__metrics = """
    ORIGINAL FILE
        
        Rows of data: {A}
             Columns: {B}

    OUTCOME
        
        Rows of data: {C}
             Columns: {D}
        
        Number of rows which met each criteria:
                      {E}
        
        Average value of new columns:
                      {F}
"""



# Lists ########################################################################

# Filtering criteria
LIST__str_eq = ["S_EQ", "STR_EQ", "S_EQUAL", "S_EQUALS", "STR_EQUAL",
        "STR_EQUALS", "STRING_EQ", "STRING_EQUAL", "STRING_EQUALS"]
LIST__str_neq = ["S_EQ!", "STR_EQ!", "S_EQUAL!", "S_EQUALS!", "STR_EQUAL!",
        "STR_EQUALS!", "STRING_EQ!", "STRING_EQUAL!", "STRING_EQUALS!",
        "S_NEQ", "S_N_EQ", "STR_NEQ", "STR_N_EQ", "S_N_EQUAL", "S_N_EQUALS",
        "STR_N_EQUAL", "STR_N_EQUALS", "S_NOT_EQ", "STR_NOT_EQ", "STRING_N_EQ",
        "S_NOT_EQUAL", "S_NOT_EQUALS", "STR_NOT_EQUAL", "STR_NOT_EQUALS",
        "STRING_N_EQUAL", "STRING_N_EQUALS", "STRING_NOT_EQ",
        "STRING_NOT_EQUAL", "STRING_NOT_EQUALS"]
LIST__cont = ["CONT", "CONTAIN", "CONTAINS"]
LIST__ncont = ["!CONT", "CONT!", "N_CONT", "NOT_CONT", "N_CONTAIN",
        "N_CONTAINS", "NOT_CONTAIN", "NOT_CONTAINS"]
LIST__great = [">", "GREAT", "GREATER", "GREATER_THAN", "MORE_THAN"]
LIST__greq = [">=", "=>", "G_EQ", "GR_EQ", "GREAQUALS", "GREQUALS"]
LIST__less = ["<", "LESS", "LESSER", "LESS_THAN"]
LIST__leq = ["<=", "=<", "L_EQ", "LE_EQ",  "LEQUALS"]
LIST__int_eq = [ "I_EQ", "INT_EQ", "I_EQUAL", "I_EQUALS",  "INT_EQUAL",
        "INT_EQUALS", "INTEGER_EQ", "INTEGERING_EQUAL", "INTEGERING_EQUALS"]
LIST__int_neq = ["I_EQ!", "INT_EQ!", "I_EQUAL!", "I_EQUALS!", "INT_EQUAL!",
        "INT_EQUALS!", "INTEGER_EQ!", "INTEGERING_EQUAL!", "INTEGERING_EQUALS!",
        "I_EQ!", "INT_EQ!", "I_EQUAL!", "I_EQUALS!", "INT_EQUAL!",
        "INT_EQUALS!", "INTEGER_EQ!", "INTEGERING_EQUAL!", "INTEGERING_EQUALS!",
        "I_NEQ", "I_N_EQ", "INT_NEQ", "INT_N_EQ", "I_N_EQUAL", "I_N_EQUALS",
        "INT_N_EQUAL", "INT_N_EQUALS", "I_NOT_EQ", "INT_NOT_EQ", "INTEGER_N_EQ",
        "I_NOT_EQUAL", "I_NOT_EQUALS", "INT_NOT_EQUAL", "INT_NOT_EQUALS",
        "INTEGER_N_EQUAL", "INTEGER_N_EQUALS", "INTEGER_NOT_EQ",
        "INTEGER_NOT_EQUAL", "INTEGER_NOT_EQUALS"]
LIST__flo_eq = ["F_EQ", "FLO_EQ", "F_EQUAL", "F_EQUALS", "FLO_EQUAL",
        "FLO_EQUALS", "FLOAT_EQ", "FLOAT_EQUAL", "FLOAT_EQUALS"]
LIST__flo_neq = ["F_EQ!", "FLO_EQ!", "F_EQUAL!", "F_EQUALS!", "FLO_EQUAL!",
        "FLO_EQUALS!", "FLOAT_EQ!", "FLOAT_EQUAL!", "FLOAT_EQUALS!", "F_NEQ",
        "F_N_EQ", "FLO_NEQ", "FLO_N_EQ", "F_N_EQUAL", "F_N_EQUALS",
        "FLO_N_EQUAL", "FLO_N_EQUALS", "F_NOT_EQ", "FLO_NOT_EQ", "FLOAT_N_EQ",
        "F_NOT_EQUAL", "F_NOT_EQUALS", "FLO_NOT_EQUAL", "FLO_NOT_EQUALS",
        "FLOAT_N_EQUAL", "FLOAT_N_EQUALS", "FLOAT_NOT_EQ", "FLOAT_NOT_EQUAL",
        "FLOAT_NOT_EQUALS"]
LIST__str_eq = All_Cases(LIST__str_eq)
LIST__str_neq = All_Cases(LIST__str_neq)
LIST__cont = All_Cases(LIST__cont)
LIST__ncont = All_Cases(LIST__ncont)
LIST__great = All_Cases(LIST__great)
LIST__greq = All_Cases(LIST__greq)
LIST__less = All_Cases(LIST__less)
LIST__leq = All_Cases(LIST__leq)
LIST__int_eq = All_Cases(LIST__int_eq)
LIST__int_neq = All_Cases(LIST__int_neq)
LIST__flo_eq = All_Cases(LIST__flo_eq)
LIST__flo_neq = All_Cases(LIST__flo_neq)

LIST__cv__col_no = ["C", "COL", "COLUMN", "COL_NO", "COLUMN_NO"]
LIST__cv__col_no = All_Cases(LIST__cv__col_no)
LIST__cv__value = ["V", "v", "VAL", "Val", "val", "VALUE", "Value", "value"]



# Column operations
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
LIST__dif = ["DIF", "Dif", "dif", "DIFFERENCE", "Difference", "difference"]
LIST__geo = ["GEO", "Geo", "geo", "GEOMETRIC", "Geometric", "geometric"]



# Dictionaries #################################################################

DICT__header = DICT__keep_skip_rear



DICT__criteria = {}
for i in LIST__str_eq: DICT__criteria[i] = CRITERIA.STR_EQ
for i in LIST__str_neq: DICT__criteria[i] = CRITERIA.STR_NOT_EQ
for i in LIST__cont: DICT__criteria[i] = CRITERIA.CONTAINS
for i in LIST__ncont: DICT__criteria[i] = CRITERIA.NOT_CONTAIN
for i in LIST__great: DICT__criteria[i] = CRITERIA.GREATER_THAN
for i in LIST__greq: DICT__criteria[i] = CRITERIA.GREAQUALS
for i in LIST__less: DICT__criteria[i] = CRITERIA.LESS_THAN
for i in LIST__leq: DICT__criteria[i] = CRITERIA.LEQUALS
for i in LIST__int_eq: DICT__criteria[i] = CRITERIA.INT_EQ
for i in LIST__int_neq: DICT__criteria[i] = CRITERIA.INT_NOT_EQ
for i in LIST__flo_eq: DICT__criteria[i] = CRITERIA.FLO_EQ
for i in LIST__flo_neq: DICT__criteria[i] = CRITERIA.FLO_NOT_EQ

DICT__criteria_str = {
    CRITERIA.STR_EQ: "str==",
    CRITERIA.STR_NOT_EQ: "str!=",
    CRITERIA.CONTAINS: "Contains",
    CRITERIA.NOT_CONTAIN: "!Contains",
    CRITERIA.GREATER_THAN: ">",
    CRITERIA.GREAQUALS: ">=",
    CRITERIA.LESS_THAN: "<",
    CRITERIA.LEQUALS: "<=",
    CRITERIA.INT_EQ: "int==",
    CRITERIA.INT_NOT_EQ: "int!=",
    CRITERIA.FLO_EQ: "float==",
    CRITERIA.FLO_NOT_EQ: "float!="
    }



DICT__operation = {}
for i in LIST__add: DICT__operation[i] = OPERATION.ADD
for i in LIST__sum: DICT__operation[i] = OPERATION.SUM
for i in LIST__sub: DICT__operation[i] = OPERATION.SUB
for i in LIST__mul: DICT__operation[i] = OPERATION.MUL
for i in LIST__pro: DICT__operation[i] = OPERATION.PRO
for i in LIST__div: DICT__operation[i] = OPERATION.DIV
for i in LIST__avg: DICT__operation[i] = OPERATION.AVG
for i in LIST__cat: DICT__operation[i] = OPERATION.CAT
for i in LIST__dif: DICT__operation[i] = OPERATION.DIF
for i in LIST__geo: DICT__operation[i] = OPERATION.GEO

DICT__operation_str = {
    OPERATION.ADD: "Addition",
    OPERATION.SUM: "Addition",
    OPERATION.SUB: "Subtraction",
    OPERATION.MUL: "Multiplication",
    OPERATION.PRO: "Multiplication",
    OPERATION.DIV: "Division",
    OPERATION.AVG: "Mean",
    OPERATION.CAT: "Concatenate",
    OPERATION.DIF: "Difference",
    OPERATION.GEO: "Geometric_Mean"
    }



# Apply Globals ################################################################

PRINT.PRINT_ERRORS = PRINT_ERRORS
PRINT.PRINT_PROGRESS = PRINT_PROGRESS
PRINT.PRINT_METRICS = PRINT_METRICS



# Table Processing Functions ###################################################

def Main():
    pass



def Filter_Line(values, filters, filter_metrics=None):
    """
    Assess a row of data to see which filters if passes.
    Return True if it passes all "include" filters and fails all "exclude"
    filters. Return False otherwise.
    
    If the metrics for each individual filter are being tracked, a list can be
    added as an argument is updated in accordance with the outcome. The list is
    assumed to be a tracker for the number of lines which meet each filtering
    criteria.
    
    @values
            (list<str>)
            The row of data being filtered.
    @filters
            (<list<FILTER>)
                FILTER = [int(ENUM), int, int(ENUM), int(ENUM)/str]
            A list of filtering criteria. Each filter consists of the following:
                - Include/Exclude
                    (int) - Pseudo ENUM
                    Whether to include or exclude lines which meet this critera.
                - Target column
                    (int)
                    The column number of the column being targetted.
                - Criteria
                    (int) - Pseudo ENUM
                    What filtering criteria to use.
                - Comparison type
                    (int) - Pseudo ENUM
                    Whether to compare against another column, or against a
                    static value.
                - Value OR reference column
                    (*)
                    Either an integer denoting the column number of the column
                    containing the value to be used for the comparison, or the
                    value itself to be used for the comparison.
    @filter_metrics
            (list<int>)
            A list of counts for the number of lines (so far) which have met the
            corresponding criteria.
    
    Filter_Line(list<str>, list<list<>(5)>, list<int>) -> bool
    """
    pass



def Generate_New_Line(values, delimiter, new_row_specs, new_col_metrics=None):
    """
    Generate a new line of data according to [new_row_specs].
    
    @values
            (list<str>)
            The original data.
    @delim
            (str)
            The delimiter used by the output file.
    @new_row_specs
            (<list<SPECS>)
            A list of specs specifying what to add to the new row of data. Each
            SPECS falls into one of three types:
                KEEP:       Keep the value, as is, of a column in the original
                            data.
                NEW:        Add a new column with a static value for all rows.
                OPERATION:  Derive a new value from the data in the original
                            data.
            Each SPECS begins with an int (pseudo ENUM) signifying whether it is
            a KEEP, a NEW, or an OPERATION.
            For KEEP, there will only be one more value in the SPEC - the column
            number of the original data to include in the output.
            For NEW, there will only be one more value in the SPEC - the string
            to add to that column in all rows of the output.
            For OPERATION, there will be two more values in the SPEC - an int
            (pseudo ENUM) signifying which operation to perform, and a list of
            ints which are the column numbers of the columns to perform the
            operation on.
    @new_col_metrics
            (list<float>)
            A list of cumulative totals. Each total corresponds to an OPERATION
            column.
    
    Filter_Line(list<str>, str, list<list<>>, list<int>) -> bool
    """
    pass



# Table Metadata Functions #####################################################

def Get_Header_Params(header_specs):
    """
    Return the header specs ([keep/skip/rear, value]) as a list of header specs
    which can be used by Table_File_Reader.py. The "rearrange" option, if in the
    specs, will be converted to a 1, signifying a single-line skip.
    
    @header_specs
            (list<[int, int, int/str]>)
            A series of lists denoting the header details of a file. Each list
            contains three things:
                1)  A pseudo-ENUM int which denotes how the line(s) is/are to be
                    treated. Options are:
                        A)  Keep the line(s)
                        B)  Skip the line(s)
                        C)  Treat this line as the column headers
                2)  Either:
                        A)  An integer denoting a number of lines
                        B)  A char. This is the char found at the start of each
                            line
                        C)  None
            It is assumed that the [header_specs] specify the "rearrange" option
            no more than once, and will be specified last, if specified.
    
    Get_Header_Params(list<[int, int/str]>) -> list<int/str>
    """
    results = []
    for specs in header_specs:
        treatment, value = specs
        if treatment == KSR.REAR:
            results.append(1)
        else:
            results.append(value)
    return results

def Get_Column_Headers(filepath, delim, header_specs):
    """
    Return the column headers of a table file after skipping the comments
    section.
    Return an empty list if there is an error with the input.
    
    @filepath
            (str - filepath)
            The filepath of the input file.
    @delim
            (str)
            The delimiter use by the input file.
    @header_specs
            (list<[int, int, int/str]>)
            A series of lists denoting the header details of a file. Each list
            contains three things:
                1)  A pseudo-ENUM int which denotes how the line(s) is/are to be
                    treated. Options are:
                        A)  Keep the line(s)
                        B)  Skip the line(s)
                        C)  Treat this line as the column headers
                2)  Either:
                        A)  An integer denoting a number of lines
                        B)  A char. This is the char found at the start of each
                            line
                        C)  None
            It is assumed that the [header_specs] specify the "rearrange" option
            no more than once, and will be specified last, if specified.
    
    Get_No_Columns(str, str, list<[int, int, int/str]>) -> list<str>
    """# Open
    f = open(filepath, "U")
    line = f.readline()
    
    # Setup
    empty_flag = False
    
    # Headers
    for header_list in header_specs:
        action, value = header_list
        
        # A set number of lines
        if action == KSR.REAR:
            f.close()
            pass
        
        # Keep or skip
        else:
            if type(value) == int:
                if value < 0:
                    return -1
                while value > 0:
                    line = f.readline()
            elif type(value) == str:
                read_flag = True
                while read_flag:
                    if line.startswith(value):
                        line.readline()
                    else:
                        read_flag = False
            else:
                return -1
    
    # Close
    f.close()
    return []

def Get_No_Columns(filepath, delim, header_specs):
    """
    Return the number of columns in a file, after excluding header rows which
    are not part of the table, such as comments.
    Return -1 if there is an error with the input.
    
    @filepath
            (str - filepath)
            The filepath of the input file.
    @delim
            (str)
            The delimiter use by the input file.
    @header_specs
            (list<[int, int, int/str]>)
            A series of lists denoting the header details of a file. Each list
            contains three things:
                1)  A pseudo-ENUM int which denotes how the line(s) is/are to be
                    treated. Options are:
                        A)  Keep the line(s)
                        B)  Skip the line(s)
                        C)  Treat this line as the column headers
                2)  Either:
                        A)  An integer denoting a number of lines
                        B)  A char. This is the char found at the start of each
                            line
                        C)  None
            It is assumed that the [header_specs] specify the "rearrange" option
            no more than once, and will be specified last, if specified.
    
    Get_No_Columns(str, str, list<[int, int, int/str]>) -> int
    """
    # Open
    f = open(filepath, "U")
    line = f.readline()
    
    # Setup
    empty_flag = False
    
    # Headers
    for header_list in header_specs:
        action, value = header_list
        
        # A set number of lines
        if action == KSR.REAR:
            pass
        
        # Keep or skip
        else:
            if type(value) == int:
                if value < 0:
                    return -1
                while value > 0:
                    line = f.readline()
            elif type(value) == str:
                read_flag = True
                while read_flag:
                    if line.startswith(value):
                        line.readline()
                    else:
                        read_flag = False
            else:
                return -1
    
    # Close
    f.close()
    
    # Get column numbers
    if not line:
        return 0
    delim_count = line.count(delim)
    col_count = delim_count + 1
    return value_count



# Command Line Parsing #########################################################

def Parse_Command_Line_Input__Multitool_For_Tables(raw_command_line_input):
    """
    Parse the command line input and call the Multitool_For_Tables function with
    appropriate arguments if the command line input is valid.
    """    
    # Safe exit
    return 0



# Validators ###################################################################

def Validate_Header_Order(header_specs):
    """
    Determine whether or not a "rearrange" occurs for something other than the
    final header section specification.
    Return True if valid, False otherwise.
    
    Validate_Header_Order(list<[int, int/char]) -> bool
    """
    encountered_flag = False
    for specs in header_specs:
        if encountered_flag:
            return False
        treatment_type, value = specs
        if treatment_type == KSR.REAR:
            encountered_flag = True
    return True

def Validate_Header_Treatment(header_treatment):
    """
    Return an int (pseudo-ENUM) designating how a particular header section
    should be processed.
    Return 0 if [header_treatment] is invalid.
    
    Validate_Header_Treatment(str) -> int
    """
    if header_treatment in LIST__skip: return KSR.KEEP
    if header_treatment in LIST__keep: return KSR.SKIP
    if header_treatment in LIST__rear: return KSR.REAR
    return 0

def Validate_Header_Values(value_type, value):
    """
    Return a value for delimiting lines in the header section.
    Return -1 if the value type is invalid.
    Return -2 if the value given is invalid.
    
    Validate_Header_Values(str, str) -> str
    Validate_Header_Values(str, str) -> int
    """
    if value_type == FILTER_TYPE.CHAR:
        return value
    if value_type == FILTER_TYPE.NUM:
        try:
            result = int(value)
            if result < 1:
                return -2
            return result
        except:
            return -2
    else:
        return -1



def Validate_Columns(string, column_count):
    """
    Return a list of column numbers, as specified by [string].
    Return None if [string] is invalid for specifying column numbers.
    Return an empty list if a column number is specified which exceeds the
    number of columns as specified by [column_count].
    
    The input takes column numbers under an index 1 system, but produces numbers
    under an index 0 system.
    
    @string
            (str)
            The string denoting which column numbers to use. This string can use
            one of the following formats:
                
                1:  "ALL"
                    Specifies all columns in the file. This derives a list
                    of column numbers based on @column_count.
            
                2:  Underscore-separated list.
                    Integers separated by underscores.
                        Ex.:
                        1_2_3 denotes columns 1, 2, and 3
            
                3:  Square bracket indices.
                    Two numbers in square brackets, separated by a colon. These
                    two numbers denote the first and last columns in a series of
                    consecutive columns to be included.
                        Ex.:
                        [:3] specifies the first 3 columns
                        [-3:] specifies the last 3 columns
                        [4:6] specifies columns 4, 5, and 6
                        [2:-2] specifies all columns except the first and last
            
            The column numbers use the index 1 system, not index 0; the first
            column is 1, and not 0.
    @column_count
            (int)
            The number of columns in the file. Specified column numbers cannot
            exceed this.
    
    Validate_Columns(str, int) -> list<int>
    Validate_Columns(str, int) -> None
    """
    if not string: # No string
        return None
    if string in LIST__all: # All
        range_ = range(column_count)
        return range_
    if string[0] == "[": # Square bracket indices
        # Check for structural errors
        if string[-1] != "]":
            return None
        if ":" not in string:
            return None
        string = string[1:-1]
        numbers = string.split(":")
        if len(numbers) != 2:
            return None
        # Validate the numbers
        temp = []
        for num in numbers:
            if not num:
                temp.append(None)
            else:
                try:
                    num = int(num)
                except:
                    return None
                if num == 0:
                    return None
                if num > 0:
                    num = num - 1
                    temp.append(num)
                else: # num < 0
                    num = column_count + num
                    temp.append(num)
        # Blanks
        start, end = temp
        if start == None:
            start = 0
        if end == None:
            end = column_count - 1
        # Generate numbers
        if end > start:
            range_ = range(start, end+1)
        elif end < start:
            range_ = range(end, start-1, -1)
        else:
            range_ = [start]
        return range_
    else: # Underscore-separated list
        results = []
        strings = string.split("_")
        for s in strings:
            i = Validate_Int_NonNeg(s)
            if i == -1: return None
            i = i-1
            results.append(i)
        return results



def Validate_Filter(inc_exc, col_no, criteria, filter_type, col_no__value):
    """
    Validates the specs for a filter.
    Return a length-4 list of filter specifications if the arguments are valid.
    Return a length-5 list of error codes if the arguments are invalid.
    
    With error codes, a 0 indicates no error for the corresponding string, while
    a 1 indicates that the string was invalid.
    
    Validate_Write_Path(str, str, str, str, str) -> [int, int, int, int]
    Validate_Write_Path(str, str, str, str, str) -> [int, int, int, str]
    """
    # Setup
    errors = []
    error = False
    results = []
    # Validate inc_exc
    inc_exc = Validate_Inc_Exc(inc_exc)
    if inc_exc == None:
        errors.append(1)
        error = True
    else:
        errors.append(0)
        results.append(inc_exc)
    # Validate col_no
    col_no = Validate_Int_Positive(col_no)
    if col_no == -1:
        errors.append(1)
        error = True
    else:
        errors.append(0)
        results.append(col_no-1)
    # Validate criteria
    criteria = Validate_Criteria(criteria)
    if criteria == 0:
        errors.append(1)
        error = True
    else:
        errors.append(0)
        results.append(criteria)
    # Validate filter type (C|V)
    filter_type = Validate_Filter_Type(filter_type)
    if filter_type == 0:
        errors.append(1)
        error = True
    else:
        errors.append(0)
        results.append(filter_type)
    # Validate col_no|value
    if filter_type == FILTER_TYPE.COL:
        col_no__value = Validate_Int_Positive(col_no__value)
        if col_no__value == -1:
            errors.append(1)
            error = True
        else:
            errors.append(0)
            results.append(col_no__value-1)
    elif filter_type == FILTER_TYPE.VAL:
        results.append(col_no__value)
    else:
        errors.append(0)
    # Return
    if error:
        return errors
    return results

def Validate_Criteria(string):
    """
    Validate the filtering criteria specified by a string.
    Return the corresponding int ENUM if the string specifies a valid filtering
    criteria.
    Return 0 if the string is invalid.
    
    Validate_Criteria(str) -> int
    """
    if string in LIST__str_eq: return CRITERIA.STR_EQ
    if string in LIST__str_neq: return CRITERIA.STR_NOT_EQ
    if string in LIST__cont: return CRITERIA.CONTAINS
    if string in LIST__ncont: return CRITERIA.CONTAINS
    if string in LIST__great: return CRITERIA.GREATER_THAN
    if string in LIST__greq: return CRITERIA.GREAQUALS
    if string in LIST__less: return CRITERIA.LESS_THAN
    if string in LIST__leq: return CRITERIA.LEQUALS
    if string in LIST__int_eq: return CRITERIA.INT_EQ
    if string in LIST__int_neq: return CRITERIA.INT_NOT_EQ
    if string in LIST__flo_eq: return CRITERIA.FLO_EQ
    if string in LIST__flo_neq: return CRITERIA.FLO_NOT_EQ
    return 0

def Validate_Filter_Type(string):
    """
    Validate a string as specifing either "column number" or "value".
    Return an int ENUM corresponding to the correct option if [string] is valid.
    Return a 0 if it is invalid.
    
    Validate_Filter_Type(str) -> int
    """
    if string in LIST__cv__col_no: return FILTER_TYPE.COL
    if string in LIST__cv__value: return FILTER_TYPE.VAL
    return 0



def Validate_Operation(string):
    """
    Validates a string as specifing an operation to calculate a new value using
    existing data.
    Return an int ENUM corresponding to the correct option if [string] is valid.
    Return a 0 if it is invalid.
    
    Validate_Operation(str) -> int
    """
    if string in LIST__add: return OPERATION.ADD
    if string in LIST__sum: return OPERATION.SUM
    if string in LIST__sub: return OPERATION.SUB
    if string in LIST__mul: return OPERATION.MUL
    if string in LIST__pro: return OPERATION.PRO
    if string in LIST__div: return OPERATION.DIV
    if string in LIST__avg: return OPERATION.AVG
    if string in LIST__cat: return OPERATION.CAT
    if string in LIST__dif: return OPERATION.DIF
    if string in LIST__geo: return OPERATION.GEO
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


