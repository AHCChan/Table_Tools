HELP_DOC = """
TALLY COLUMN
(version 2.1.1)
by Angelo Chan

This is a program for tallying the values in a column.

The results are outputted as a 2-column TSV.



USAGE:
    
    python27 Tally_Column.py <input_file> <input_format> <column_no>
            [-o <output_file>] [-s <separator>] [-m C|F|M|P|S|T|U]
            [-r A|D|N|R|O] [-p <placeholder_file> <placeholder_format>
            <placeholder_column_no>]



MANDATORY:
    
    input_file
        
        The filepath of the input BED file. No headers allowed.
    
    input_format
        
        The file format of the input file. Acceptable options are:
            tsv - Tab-separated values
            csv - Comma-separated values
            ssv - Space-separated values
    
    column_no
        
        The number of the column to be tallied. Uses an index-1 system. (The
        first column is column 1)

OPTIONAL:
    
    output_file
        
        (DEFAULT path generation available)
        
        The filepath of the output file which contains all of the contents of
        the original files.
    
    separator
        
        The separator used to separate the values within the column.
    
    (-m)
        
        (DEFAULT: M)
        
        How the program should treat the values in columns which contain
        multiple values. Acceptable options are:
            
            {C}ount    - Each value is counted the number of times it appears.
            {F}raction - Each row adds a total of 1. That "1" is split
                         proportionately between the values in that column.
            {M}ajority - When multiple values are present, only the value which
                         accounts for a clear majority is counted.
            {P}resent  - Any values which are present are counted, but only
                         once, no matter how many times they occur in that row.
            {S}ingle   - A value is only counted when it occurs only once, and
                         no other values are present in that row.
            {T}ied     - When multiple values are present, all values which
                         account for a clear majority are counted.
            {U}nique   - A value is counted only when no other values are
                         present. The same value occuring multiple times is
                         permitted.
    
    (-r)
        
        (DEFAULT: D)
        
        The results ordering method. Acceptable options are:
            
            {A}lphabetical
            {D}escending
            {N}umerical (Ascending)
            {R}eversed alphabetical
            {O}riginal order
    
    placefolder_file
        
        (DEFAULT: None)
        
        The filepath of the "placeholder" file. This is a table file which
        contains, in its first column, all values which must be included in the
        final tally, even if they have a count of 0.
    
    placeholder_format
        
        The file format of the placeholder file. Acceptable options are:
            tsv - Tab-separated values
            csv - Comma-separated values
            ssv - Space-separated values
    
    placeholder_column_no
        
        The number of the column containing the placeholder values. Uses an
        index-1 system. (The first column is column 1)



EXAMPLES EXPLANATION:
    
    1:
    Basic use case. Tally the 3rd column.
    
    2:
    Tally 4th column, which contains values separated by semicolons. Use the
    fractional system when counting entries with multiple values per row.
    Specify an output file. Place highest counts at the top of the output file.

EXAMPLE:
    
    python27 Tally_Column.py data\data_file.tsv tsv 3
    
    python27 Tally_Column.py data\data_file.tsv tsv 4 -s ; -m F
            -o results\data_column_4_tallied.csv -r D

USAGE:
    
    python27 Tally_Column.py <input_file> <input_format> <column_no>
            [-o <output_file>] [-s <separator>] [-m C|F|M|P|S|T|U]
            [-r A|D|N|R|O] [-p <placeholder_file> <placeholder_format>
            <placeholder_column_no>]
"""

NAME = "Tally_Column.py"



# Configurations ###############################################################

AUTORUN = True

WRITE_PREVENT = False # Completely prevent overwritting existing files
WRITE_CONFIRM = True # Check to confirm overwritting existing files

PRINT_ERRORS = True
PRINT_PROGRESS = True
PRINT_METRICS = True



# Minor Configurations #########################################################

FILEMOD = "__TALLY_c_{N}.tsv"



# Defaults #####################################################################
"NOTE: altering these will not alter the values displayed in the HELP DOC"

DEFAULT__mode = 3 # Count
DEFAULT__order = 3 # Descending (numerical)


# Imported Modules #############################################################

import _Controlled_Print as PRINT
from _Command_Line_Parser import *

from Table_File_Reader import *



# Enums ########################################################################

class MODE:
    COUNT=1
    FRACTION=2
    MAJORITY=3
    PRESENT=4
    SINGLE=5
    TIED=6
    UNIQUE=7

class ORDER:
    ALPHABETICAL=1
    DESCENDING=2
    NUMERICAL_ASCENDING=3
    REVERSED_ALPHABETICAL=4
    ORIGINAL=5



# Strings ######################################################################

STR__use_help = "\nUse the -h option for help:\n\t python "\
"Tally_Column.py -h"



STR__invalid_column_no = """
ERROR: Invalid column number: {s}
Please specify a positive integer.
"""

STR__column_not_found = """
ERROR: Column not found: {s}
   AT:              Row: {r}
"""

STR__invalid_mode = """
ERROR: Invalid mode specified: {s}
Please specify one of the following:
    COUNT
    FRACTION
    MAJORITY
    PRESENT
    SINGLE
    TIED
    UNIQUE
"""

STR__invalid_order = """
ERROR: Invalid results ordering method specified: {s}
Please specify one of the following:
    ALPHABETICAL
    REVERSED
    ASCENDING
    DESCENDING
"""



STR__failed_placeholder = """
ERROR: A problem occured when getting values from the placeholder file.
"""

STR__no_values = """
WARNING: No rows or valid values detected in the specified file.
"""

STR__metrics = """
                         Rows of data: {A}
    Number of different unique values: {B}
    
                        TALLYING MODE: {C}
    
             Number of values counted: {D}
       Average count per unique value: {E}"""



STR__tally_begin = "\nRunning Tally_Column..."

STR__tally_complete = "\nTally_Column successfully finished."



# Lists ########################################################################

LIST__count = ["C", "c", "COUNT", "Count", "count"]
LIST__fraction = ["F", "f", "FRACTION", "Fraction", "fraction"]
LIST__majority = ["M", "m", "MAJORITY", "Majority", "majority"]
LIST__present = ["P", "p", "PRESENT", "Present", "present"]
LIST__single = ["S", "s", "SINGLE", "Single", "single"]
LIST__tied = ["T", "t", "TIED", "Tied", "tied"]
LIST__unique = ["U", "u", "UNIQUE", "Unique", "unique"]

LIST__alphabetical = ["A", "a", "ALPHABETICAL", "Alphabetical", "alphabetical"]
LIST__reversed = ["R", "r", "REVERSED", "Reversed", "reversed"]
LIST__ascending = ["N", "n", "NUMERICAL", "Numerical", "numerical", "ASCENDING",
        "Ascending", "ascending"]
LIST__descending = ["D", "d", "DESCENDING", "Descending", "descending"]
LIST__original = ["O", "o", "ORIGINAL", "Original", "original"]



# Dictionaries #################################################################

DICT__mode = {}
for i in LIST__count: DICT__mode[i] = MODE.COUNT
for i in LIST__fraction: DICT__mode[i] = MODE.FRACTION
for i in LIST__majority: DICT__mode[i] = MODE.MAJORITY
for i in LIST__present: DICT__mode[i] = MODE.PRESENT
for i in LIST__single: DICT__mode[i] = MODE.SINGLE
for i in LIST__tied: DICT__mode[i] = MODE.TIED
for i in LIST__unique: DICT__mode[i] = MODE.UNIQUE

DICT__mode_str = {
    MODE.COUNT: "Count",
    MODE.FRACTION: "Fraction",
    MODE.MAJORITY: "Majority",
    MODE.PRESENT: "Present",
    MODE.SINGLE: "Single",
    MODE.TIED: "Tied",
    MODE.UNIQUE: "Unique"}

DICT__order = {}
for i in LIST__alphabetical: DICT__order[i] = ORDER.ALPHABETICAL
for i in LIST__reversed: DICT__order[i] = ORDER.REVERSED_ALPHABETICAL
for i in LIST__ascending: DICT__order[i] = ORDER.NUMERICAL_ASCENDING
for i in LIST__descending: DICT__order[i] = ORDER.DESCENDING
for i in LIST__original: DICT__order[i] = ORDER.ORIGINAL



# Apply Globals ################################################################

PRINT.PRINT_ERRORS = PRINT_ERRORS
PRINT.PRINT_PROGRESS = PRINT_PROGRESS
PRINT.PRINT_METRICS = PRINT_METRICS



# Functions ####################################################################

def Tally_Column(path_in, delim, col_no, path_out, separator, mode, order,
            path_placeholder, delim_placeholder, col_no_placeholder):
    """
    Generate a series of FASTA files each containing a synthetic chromosome.
    
    @path_in
            (str - filepath)
            The filepath of the input file.
    @delim
            (str)
            The delimiter use by the input file.
    @col_no
            (int)
            The index number of the column to be tallied.
    @path_out
            (str - filepath)
            The filepath of the output file.
    @separator
            (str)
            The separator used for separating multiple values in a single
            column.
    @mode
            (int) - Pseudo ENUM
            How the program should treat the values within columns which contain
            multiple values. Acceptable options are:
                1:  Count - Each value is counted the number of times it
                    appears.
                2:  Fraction - Each row adds a total of 1. That "1" is split
                    proportionately between the values in that column.
                3:  Majority - When multiple values are present, only the value
                    which accounts for a clear majority is counted.
                4:  Present - Any values which are present are counted, but only
                    once, no matter how many times they occur in that row.
                5:  Single - A value is counted only when no other values are
                    present. The same value occuring multiple times is
                    permitted.
                6:  Tied - When multiple values are present, all values which
                    account for a clear majority are counted.
                7:  Unique - A value is only counted when it occurs only once,
                    and no other values are present in that row.
    @order
            (int) - Pseudo ENUM
            How the results should be ordered. Acceptable options are:
                1:  Alphabetical (A-Z)
                2:  Reversed alphabetical (Z-A)
                3:  Ascending numerical order
                4:  Descending numerical order
                5:  Retain the order in which the result appeared in the
                    original data file.
    @path_placeholder
            (str - filepath)
            The filepath of the "placeholder" file. This is a table file which
            contains, in its first column, all values which must be included in
            the final tally, even if they have a count of 0.
    @delim_placeholder
            (str)
            The delimiter use by the placeholder file.
    @col_no_placeholder
            (int)
            The index number of the column in the placeholder file to use as a
            placeholder.
    
    Return a value of 0 if the function runs successfully.
    Return a value of 1 if there is a problem.
    
    Tally_Column(str, str, int, str, str, int) -> int
    """
    
    PRINT.printP(STR__tally_begin)
    
    # Setup reporting
    total_rows = 0
    total_unique = 0
    total_counted = 0
    total_value = 0
    counts = {}
    
    # I/O setup
    f = Table_Reader()
    f.Set_New_Path(path_in)
    f.Set_Delimiter(delim)
    f.Open()
    f.Close()
    o = open(path_out, "w")
    
    # Original order
    original_order = []
    
    # Placeholders
    if path_placeholder:
        counts = Get_Placeholders(path_placeholder, delim_placeholder,
                col_no_placeholder)
        if not counts:
            PRINT.printE(STR__failed_placeholder)
            return 1
    
    # Main loop
    f.Open()
    while not f.EOF:
        f.Read()
        total_rows += 1
        columns = f.Get()
        # Get values
        if separator:
            values_raw = columns[col_no]
            values = values_raw.split(separator)
        else:
            values = [columns[col_no]]
        # Mode-dependant
        if mode == MODE.SINGLE: # Single
            if len(values) == 1:
                total_counted += 1
                total_value += 1
                value = values[0]
                if value not in counts:
                    counts[value] = 1
                    original_order.append(value)
                else:
                    counts[value] += 1
        elif mode == MODE.COUNT: # Count
            for value in values:
                total_counted += 1
                total_value += 1
                if value not in counts:
                    counts[value] = 1
                    original_order.append(value)
                else:
                    counts[value] += 1
        else: # Fraction/Present/Tied/Unique
            # Do mini count
            mini_count = {}
            mini_total = 0
            for value in values:
                mini_total += 1
                if value not in mini_count:
                    mini_count[value] = 1.0
                    original_order.append(value)
                else:
                    mini_count[value] += 1
            # Mode-dependant
            if mode == MODE.FRACTION: # Fraction
                total_value += 1
                for value in mini_count:
                    total_counted += 1
                    fraction_value = mini_count[value]/mini_total
                    if value not in counts:
                        counts[value] = fraction_value
                        original_order.append(value)
                    else:
                        counts[value] += fraction_value
            elif mode == MODE.MAJORITY: # Majority
                for value in mini_count:
                    temp_count = mini_count[value]
                    if temp_count*2 > mini_total:
                        total_counted += 1
                        total_value += 1
                        if value not in counts:
                            counts[value] = 1
                            original_order.append(value)
                        else:
                            counts[value] += 1
            elif mode == MODE.PRESENT: # Present
                for value in mini_count:
                    total_counted += 1
                    total_value += 1
                    if value not in counts:
                        counts[value] = 1
                        original_order.append(value)
                    else:
                        counts[value] += 1
            elif mode == MODE.TIED: # Tied
                highest = 0
                for value in mini_count:
                    if mini_count[value] > highest:
                        highest = mini_count[value]
                for value in mini_count:
                    if mini_count[value] == highest:
                        total_counted += 1
                        total_value += 1
                        if value not in counts:
                            counts[value] = 1
                            original_order.append(value)
                        else:
                            counts[value] += 1
            elif mode == MODE.UNIQUE: # Unique
                if len(mini_count) == 1:
                    for value in mini_count:
                        total_counted += 1
                        total_value += 1
                        if value not in counts:
                            counts[value] = 1
                            original_order.append(value)
                        else:
                            counts[value] += 1
            else:
                f.Close()
                o.close()
                PRINT.printE(STR__unexpected_failure)
                return 2
    
    # Write
    if order == ORDER.ORIGINAL:
        keys = original_order
    else:
        keys = Get_Keys_Order(counts, order)
    for k in keys:
        sb = k + "\t" + str(counts[k]) + "\n"
        o.write(sb)
    
    # Finish
    f.Close()
    o.close()
    PRINT.printP(STR__tally_complete)
    
    # Reporting
    total_unique = len(counts)
    Report_Metrics(total_rows, total_unique, total_counted, total_value, mode)
    
    # Wrap up
    return 0



def Get_Placeholders(path_placeholder, delim_placeholder, col_no_placeholder):
    """
    Return a dictionary of empty counts for every value in the first column of
    [path_palceholder].
    
    @path_placeholder
            (str - filepath)
            The filepath of the "placeholder" file. This is a table file which
            contains, in its first column, all values which must be included in
            the final tally, even if they have a count of 0.
    @delim_placeholder
            (str)
            The delimiter use by the placeholder file.
    @col_no_placeholder
            (int)
            The index number of the column in the placeholder file to use as a
            placeholder.
    
    Get_Keys_Order(str, str, int) -> dict<str:int>
    """
    result = {}
    f = Table_Reader()
    f.Set_New_Path(path_placeholder)
    f.Set_Delimiter(delim_placeholder)
    f.Open()
    while not f.EOF:
        f.Read()
        try:
            gene = f[col_no_placeholder]
        except:
            return {}
        result[gene] = 0
    f.Close()
    return result

def Get_Keys_Order(data, order):
    """
    Return the keys of the dictionary in the order indicated by [order].
    
    @data
            (dict<str:int/float>)
            The data. The keys are the strings being tallied, while the values
            (of this dictionary) are the counts/count-values of those strings.
    @order
            (int) - Pseudo ENUM
            How the results should be ordered. Acceptable options are:
                1:  Alphabetical (A-Z)
                2:  Reversed alphabetical (Z-A)
                3:  Ascending numerical order
                4:  Descending numerical order
    
    Get_Keys_Order(dict, int) -> list<str>
    """
    keys = data.keys()
    if order == ORDER.ALPHABETICAL:
        keys = sorted(keys)
        return keys
    elif order == ORDER.REVERSED_ALPHABETICAL:
        keys = sorted(keys, reverse=True)
        return keys
    else:
        temp = {}
        keys = data.keys()
        # First sort numerically
        for k in keys:
            count = data[k]
            if count in temp:
                temp[count].append(k)
            else:
                temp[count] = [k]
        # Finalize while sorting sublists
        result = []
        keys = temp.keys()
        if order == ORDER.DESCENDING:
            keys = sorted(keys, reverse=True)
        elif order == ORDER.NUMERICAL_ASCENDING:
            keys = sorted(keys)
        for k in keys:
            values = temp[k]
            values = sorted(values)
            for v in values:
                result.append(v)
        # Return
        return result



def Report_Metrics(rows, unique, counted, value, mode):
    """
    Print a report into the command line interface of the metrics of the
    operation.
    
    @rows
            (int)
            The number of rows in the original file.
    @unique
            (int)
            The number of unique values found.
    @counted
            (int)
            The number of values counted.
    @value
            (int)
            The total value of all "counts".
    @mode
            (int) - Pseudo ENUM
            How the program should treat the values within columns which contain
            multiple values. Acceptable options are:
                1:  Count
                2:  Fraction
                3:  Majority
                4:  Present
                5:  Single
                6:  Tied
                7:  Unique
    
    Report_Metrics(int, int, int, int) -> None
    """
    # Empty
    if unique == 0:
        PRINT.printM(STR__no_values)
        return
    # Calculations
    avg_count = float(value)/unique
    # Strings
    rows = str(rows) + "   "
    unique = str(unique) + "   "
    counted = str(counted) + "   "
    value = str(value) + "   "
    avg_count = Trim_Percentage_Str(str(avg_count), 2)
    # Strings, non-numerical
    mode = DICT__mode_str.get(mode) + "   "
    # Pad
    max_size = Get_Max_Len([rows, unique, mode, counted, value, avg_count])
    rows = Pad_Str(rows, max_size, " ", 0)
    unique = Pad_Str(unique, max_size, " ", 0)
    mode = Pad_Str(mode, max_size, " ", 0)
    counted = Pad_Str(counted, max_size, " ", 0)
    value = Pad_Str(value, max_size, " ", 0)
    avg_count = Pad_Str(avg_count, max_size, " ", 0)
    # Print
    PRINT.printM(STR__metrics.format(A = rows, B = unique, C = mode,
            D = counted, E = avg_count))



# Command Line Parsing #########################################################

def Parse_Command_Line_Input__Tally_Column(raw_command_line_input):
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
    if len(inputs) < 3:
        PRINT.printE(STR__insufficient_inputs)
        PRINT.printE(STR__use_help)
        return 1
    
    # Setup mandatory inputs
    path_in = inputs.pop(0)
    input_format = inputs.pop(0)
    col_no_str = inputs.pop(0)
    
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
    col_no = Validate_Int_Positive(col_no_str)
    if col_no == -1:
        PRINT.printE(STR__invalid_column_no.format(s = col_no_str))
        PRINT.printE(STR__use_help)
        return 1
    col_no = col_no - 1
    
    # Set up rest of the parsing
    path_out = Generate_Default_Output_File_Path_Tally_C(path_in, FILEMOD,
            col_no) 
    separator = None
    mode = DEFAULT__mode
    order = DEFAULT__order
    path_placeholder = None
    delim_placeholder = None
    col_no_placeholder = 1
    
    # Validate optional inputs (except output path)
    while inputs:
        arg = inputs.pop(0)
        flag = 0
        try: # Following arguments
            if arg in ["-o", "-s", "-m", "-r"]:
                arg2 = inputs.pop(0)
            elif arg in ["-p"]:
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
        elif arg == "-s":
            separator = arg2
        elif arg == "-m":
            mode = DICT__mode.get(arg2, None)
            if not mode:
                PRINT.printE(STR__invalid_mode.format(s = arg2))
                PRINT.printE(STR__use_help)
                return 1
        elif arg == "-r":
            order = DICT__order.get(arg2, None)
            if not order:
                PRINT.printE(STR__invalid_order.format(s = arg))
                PRINT.printE(STR__use_help)
                return 1
        else: # arg == "-p"
            path_placeholder = arg2
            valid = Validate_Read_Path(path_placeholder)
            if valid == 1:
                PRINT.printE(STR__IO_error_read.format(f = path_placeholder))
                PRINT.printE(STR__use_help)
                return 1
            delim_placeholder = Validate_Table_File_Format(arg3)
            if not delim_placeholder:
                PRINT.printE(STR__invalid_table_format.format(
                        f = delim_placeholder))
                PRINT.printE(STR__use_help)
                return 1
            col_no_placeholder = Validate_Int_Positive(arg4)
            if valid == 1:
                PRINT.printE(STR__invalid_table_format.format(f = arg4))
                PRINT.printE(STR__use_help)
                return 1
            col_no_placeholder = col_no_placeholder - 1
    
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
    exit_state = Tally_Column(path_in, delim, col_no, path_out, separator, mode,
            order, path_placeholder, delim_placeholder, col_no_placeholder)
    
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



def Generate_Default_Output_File_Path_Tally_C(path_in, filemod, col_no):
    """
    Generate output folder path based on the provided input filepath.

    Generate_Default_Output_File_Path_Tally_C(str, str, int) -> str
    """
    index = Find_Period_Index(path_in)
    if index == -1: return path_in + filemod.format(N = col_no+1)
    else: return path_in[:index] + filemod.format(N = col_no+1)



# Main Loop ####################################################################

if AUTORUN and (__name__ == "__main__"):
    exit_code = Parse_Command_Line_Input__Tally_Column(sys.argv)



