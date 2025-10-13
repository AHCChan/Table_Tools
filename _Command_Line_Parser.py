"""
COMMAND LINE PARSER
(version 2.7)
by Angelo Chan

This is a library of functions useful for parsing command line inputs and
verifying them.
"""



# Configurations ###############################################################

# Minor Configurations #########################################################

# Defaults #####################################################################

# Imported Modules #############################################################

import sys
import os



# Enums ########################################################################

class NSK:
    NONE=1
    SKIP=2
    KEEP=3
    
class KSR:
    SKIP=2
    KEEP=3
    REAR=4

class INC_EXC:
    INCLUDE=1
    EXCLUDE=2



# Strings ######################################################################

STR__no_inputs = "\nERROR: No inputs were given."
STR__insufficient_inputs = "\nERROR: Not enough inputs were given."
STR__insufficient_inputs_arg = """
ERROR: Not enough inputs were given for the flag: {s}"""

STR__IO_error_read = "\nERROR: Input file does not exist or could not be "\
        "opened."

STR__IO_error_read_folder = "\nERROR: Input folder does not exist or could not"\
        " be read."

STR__read_folder_no_substring = "\nERROR: Input folder:\n\t{f}\n...contains "\
        "no files containing the substring:\n\t{s}"

STR__IO_error_write_forbid = """
ERROR: You specified an output file which already exists and the administrator
for this program has forbidden all overwrites. Please specify a different
output file, move the currently existing file, or configure the underlying
File Writer module."""
STR__IO_error_write_unable = """
ERROR: Unable to write to the specified output file."""

STR__IO_error_write_folder_nonexistent = """
ERROR: You specified an output folder which does not exist and cannot be
created. Please specify a different output folder."""
STR__IO_error_write_folder_cannot = """
ERROR: You specified an output folder which you do not have the authorization
to write into. Please specify a different output folder."""
STR__IO_error_write_folder_forbid = """
ERROR: You specified an output folder which already exists and the administrator
for this program has forbidden all overwrites. Please specify a different
output folder, move the currently existing folder, or configure the default
options in program."""
STR__IO_error_write_unexpected = """
ERROR: An unexpected error occured with the specified output path. Contact the
developers because this error should never be triggered from normal usage of
this software."""

STR__overwrite_confirm = "\nFile already exists:\n\t{f}\nDo you wish to "\
        "overwrite it? (y/n): "

STR__overwrite_accept = "\nWARNING: Existing files will be overwritten."
STR__overwrite_decline = "\nThe user has opted not to overwrite existing "\
        "files.\nThe program will now terminate."

STR__invalid_int = """
ERROR: Invalid integer: {s}
Please specify an integer.
"""

STR__invalid_enclosed_str = """
ERROR: Invalid enclosed string: {s}
Please begin and end the string with matching inverted commas.
"""

STR__invalid_width = """
ERROR: Invalid width: {s}
Please specify a positive integer.
"""

STR__invalid_column = """
ERROR: Invalid column number: {s}
Please specify a positive integer.
"""

STR__invalid_columns = """
ERROR: Invalid column number(s): {s}
Please specify at least one positive integer.
If specifying multiple integers, please separate them with {d}.
Do not add whitespaces between {d} and integers.
"""

STR__invalid_bool = """
ERROR: Invalid boolean: {s}
Please specify one of the following:
    Yes
    No
    True
    False"""

STR__invalid_arg_for_flag = "\nERROR: Invalid argument supplied for the flag "\
"\"{s}\""



STR__invalid_table_type = "\nERROR: Invalid table type specified:\n\t{s}" # OLD
STR__invalid_table_format = """
ERROR: Invalid table format specified: {s}

Please specify one of:
    tsv
    csv
    ssv"""



STR__invalid_N_C = """
ERROR: Invalid type specified: {s}
Please specify one of the following:
    Num
    Char
"""



STR__invalid_int_dec = """\nERROR: Invalid indicator for integer/decimal: {s}

Please specify one of:
    Integer
    Decimal"""



STR__invalid_ksr = """
ERROR: Invalid behaviour specified: {s}

Please specify one of:
    Keep
    Skip
    Rearrange"""

STR__invalid_inc_exc = """
ERROR: Invalid behaviour specified: {s}

Please specify one of:
    Include
    Exclude"""



STR__invalid_argument = "\nERROR: Invalid argument: {s}"

STR__parsing_args = "\nParsing arguments..."



STR__unexpected_failure = "\nProgram exited with an unexpected error."



# OS Strings ###################################################################

if sys.platform[:3] == "win":
    directory_spacer = "\\"
else:
    directory_spacer = "/"



# Lists ########################################################################

LIST__help = ["-h", "-H", "-help", "-Help", "-HELP"]

LIST__yes = ["Y", "y", "YES", "Yes", "yes", "T", "t", "TRUE", "True", "true"]
LIST__no = ["N", "n", "NO", "No", "no", "F", "f", "FALSE", "False", "false"]

LIST__all = ["A", "a", "ALL", "All", "all"]

LIST__FASTA = ["FA", "fa", "FASTA", "Fasta", "fasta"] # File extensions
LIST__VCF = ["VCF", "Vcf", "vcf"]
LIST__CSV = ["CSV", "Csv", "csv"]
LIST__TSV = ["TSV", "Tsv", "tsv"]
LIST__TSV_ = ["TSV", "Tsv", "tsv", "TAB", "Tab", "tab"]
LIST__SSV = ["SSV", "Ssv", "ssb"]

LIST__num = ["NUMBER", "Number", "number", "NUM", "Num", "num", "N", "n"]
LIST__char = ["CHARACTER", "Character", "character", "CHAR", "Char", "char",
        "C", "c"]

LIST__integer = ["INTEGERS", "Integers", "integers", "INTEGER", "Integer",
        "integer", "INT", "Int", "int", "I", "i"]
LIST__decimal = ["DECIMALS", "Decimals", "decimals", "DECIMAL", "Decimal",
        "decimal", "DEC", "Dec", "dec", "D", "d"]
LIST__SSV = ["SSV", "Ssv", "ssb"]

LIST__none = ["N", "n", "NONE", "None", "none"]
LIST__skip = ["S", "s", "SKIP", "Skip", "skip"]
LIST__keep = ["K", "k", "KEEP", "Keep", "keep"]
LIST__rear = ["R", "r", "REAR", "Rear", "rear", "REARRANGE", "Rearrange",
        "rearrange"]

LIST__include = ["I", "i", "INC", "Inc", "inc", "INCLUDE", "Include", "include"]
LIST__exclude = ["E", "e", "EXC", "Exc", "exc", "EXCLUDE", "Exclude", "exclude"]



# Dictionaries #################################################################

DICT__table_delim_to_ext = {"\t": "tsv", ",": "csv", " ": "ssv"}



DICT__table_ext_to_delim = {}
DICT__table_ext_to_delim_ = {}

for ext in LIST__CSV: DICT__table_ext_to_delim[ext] = ","
for ext in LIST__TSV: DICT__table_ext_to_delim[ext] = "\t"
for ext in LIST__SSV: DICT__table_ext_to_delim[ext] = " "

DICT__table_ext_to_delim_ = dict(DICT__table_ext_to_delim)
for ext in LIST__TSV: DICT__table_ext_to_delim_[ext] = "\t"



DICT__delim = {}
for i in LIST__TSV: DICT__delim[i] = "\t"
for i in LIST__CSV: DICT__delim[i] = ","
for i in LIST__SSV: DICT__delim[i] = " "



DICT__none_skip_keep = {}
for i in LIST__none: DICT__none_skip_keep[i] = NSK.NONE
for i in LIST__skip: DICT__none_skip_keep[i] = NSK.SKIP
for i in LIST__keep: DICT__none_skip_keep[i] = NSK.KEEP

DICT__keep_skip_rear = {}
for i in LIST__keep: DICT__keep_skip_rear[i] = KSR.KEEP
for i in LIST__skip: DICT__keep_skip_rear[i] = KSR.SKIP
for i in LIST__rear: DICT__keep_skip_rear[i] = KSR.REAR




# Command Interface Supporting Functions #######################################

def All_Cases(strings, separator="_"):
    """
    Return all uppercase, capitalized, and lowercase string permutations of
    every string contained within [strings].
    
    The purpose is to allow mutiple arguments to achieve the same outcome.
    
    All_Cases(list<str>) -> list<str>
    """
    results = []
    for string in strings:
        words = string.split(separator)
        upper = []
        capped = []
        lower = []
        for word in words:
            upper.append(word.upper())
            capped.append(word.capitalize())
            lower.append(word.lower())
        s_upper = separator.join(upper)
        s_capped = separator.join(capped)
        s_lower = separator.join(lower)
        results.append(s_upper)
        results.append(s_capped)
        results.append(s_lower)
    return results



# Communications and Metrics ###################################################

def Get_Max_Len(strings):
    """
    Return the length of the longest string in a list of strings.
    
    @strings
            (list<str>)
            The list of the strings.
    
    Get_Max_Len(list<str>) -> int
    """
    maximum = 0
    for string in strings:
        length = len(string)
        if length > maximum: maximum = length
    return maximum



def Pad_Column(list_, minimum=0, extra=0, char=" ", side=0):
    """
    Return a list of padded strings.
    All strings will be padded until they are the same length.
    
    @list_
            (str)
            The list of strings to be padded.
    @minimum
            (int)
            The minimum width of the post-padding column.
            Note that if @extra is not zero, @minimum will effectively be
            @minimum+@extra.
            (DEFAULT: 0)
    @extra
            (int)
            The amount of extra padding on top.
            Note that if @extra is not zero, @minimum will effectively be
            @minimum+@extra.
            (DEFAULT: 0)
    @char   
            (str)
            The character used to pad the strings.
            (DEFAULT: whitespace)
    @side
            (int)
            An integer indicating which side the padding is to be added.
            0 for the padding to be added to the left.
            Any other integer for the padding to be added to the right.
            (DEFAULT: left)
    
    Pad_Str(list<str>, int, int, str, int) -> list<str>
    """
    # Get minimum
    for string in list_:
        length = len(string)
        if length > minimum: minimum = length
    # Extra
    if extra > 0: minimum += extra
    # Pad
    results = []
    for string in list_:
        padded_string = Pad_Str(string, minimum, char, side)
        results.append(padded_string)
    # Return
    return results



def Pad_Column_MixedNums(list_, dec_places=2, minimum=0, extra=0, char=" "):
    """
    Return a list of padded strings. The strings are assumed to be a mix of
    integers and floats and will be padded in such a way that the place values
    of all the numbers lined up.
    All strings will be padded until they are the same length.
    
    @list_
            (str)
            The list of numbers to be converted into strings and padded.
    @dec_places
            (int)
            The number of decimal places used for floats.
            (DEFAULT: 2)
    @minimum
            (int)
            The minimum width of the post-padding column.
            Note that if @extra is not zero, @minimum will effectively be
            @minimum+@extra.
            (DEFAULT: 0)
    @extra
            (int)
            The amount of extra padding on top.
            Note that if @extra is not zero, @minimum will effectively be
            @minimum+@extra.
            (DEFAULT: 0)
    @char   
            (str)
            The character used to pad the strings.
            (DEFAULT: whitespace)
    
    Pad_Str(list<str>, int, int, str, int) -> list<str>
    """
    # Float presence
    flag = False
    for num in list_:
        if type(num) == float:
            flag = True
    # Convert
    int_padder = " " * (dec_places + 1)
    float_padder = "0" * dec_places
    temp = []
    if flag:
        for num in list_:
            if type(num) == int:
                string = str(num) + int_padder
            else: # float
                string = str(num) + float_padder
                string = Trim_Percentage_Str(string, 6)
            temp.append(string)
    else:
        for num in list_:
            string = str(num)
            temp.append(string)
    list_ = temp
    # Get minimum
    for string in list_:
        length = len(string)
        if length > minimum: minimum = length
    # Extra
    if extra > 0: minimum += extra
    # Pad
    results = []
    for string in list_:
        padded_string = Pad_Str(string, minimum, char, 0) # 0 for left-padding
        results.append(padded_string)
    # Return
    return results



def Pad_Str(string, size, char=" ", side=0):
    """
    Return a padded version of a string.
    Return the original string if the desired string length is smaller than the
    length of the original string.
    
    @string
            (str)
            The string to be padded.
    @size
            (int)
            The length of the final string.
    @char   
            (str)
            The character used to pad the string.
            (DEFAULT: whitespace)
    @side
            (int)
            An integer indicating which side the padding is to be added.
            0 for the padding to be added to the left.
            Any other integer for the padding to be added to the right.
            (DEFAULT: left)
    
    Pad_Str(str, int, str, int) -> str
    """
    length = len(string)
    difference = size - length
    if difference < 0: return string
    padding = difference * char
    if side == 0: return padding+string
    return string+padding

def Trim_Percentage_Str(string, max_decimal_places):
    """
    Return a trimmed version of a string containing a percentage.
    
    @string
            (str)
            The string to be trimmed.
    @max_decimal_places
            (int)
            The maximum number of decimal places the resulting string will
            contain.
    
    Trim_Percentage_Str(str, int) -> str
    """
    string = string + max_decimal_places * "0"
    index = string.index(".") + max_decimal_places + 1
    string = string[:index]
    return string



# Validate Paths ###############################################################

def Validate_Read_Path(filepath):
    """
    Validates the filepath of the input file.
    Return 0 if the filepath is valid.
    Return 1 otherwise.
    
    Validate_Read_Path(str) -> int
    """
    try:
        f = open(filepath, "U")
        f.close()
        return 0
    except:
        return 1

def Validate_Read_Folder(dirpath):
    """
    Validates the dirpath of the folder.
    Return 0 if the filepath is valid.
    Return 1 otherwise.
    
    Validate_Read_Path(str) -> int
    """
    try:
        os.listdir(dirpath)
        return 0
    except:
        return 1



def Generate_Default_Output_Folder_Path(path_in):
    """
    Generate output folder path based on the provided input filepaths.

    Generate_Default_Output_Paths(str) -> str
    """
    index = Find_Period_Index(path_in)
    if index == -1: return path_in
    else: return path_in[:index]
    
def Generate_Default_Output_File_Path_From_File(path_in, mod,
            keep_extension=False):
    """
    Generate output filepath based on the provided input filepath. The original
    file extension can be retained or discarded depending on the users'
    preference.
    
    Assumes [path_in] is a valid filepath.

    Generate_Default_Output_File_Path_From_File(str, str, bool) -> str
    """
    index = Find_Period_Index(path_in)
    if index == -1: return path_in + mod
    if keep_extension: return path_in[:index] + mod + path_in[index:]
    return path_in[:index] + mod
    
def Generate_Default_Output_File_Path_From_Folder(path_in, mod):
    """
    Generate output filepath based on the provided input dirpaths.
    
    Assumes [path_in] is a valid dirpath.

    Generate_Default_Output_File_Path_From_Folder(str, str) -> str
    """
    return path_in + mod

def Get_File_Name_Ext(filepath):
    """
    Return the name of the file, and the file extension, for the file specified
    by [filepath].
    
    If the file has no extension, return the file name and an empty string.
    
    Assumes [filepath] is the filepath for a file. If a directory path is
    supplied, an empty string will also be returned.
    
    Get_Name(str) -> [str, str]
    """
    # Slash and backslash
    index_slash = filepath.rfind("/")
    index_bslash = filepath.rfind("\\")
    if index_slash == index_bslash == -1: pass # Simple path
    else: # Complex path
        right_most = max(index_slash, index_bslash)
        filepath = filepath[right_most+1:]
    # Find period
    index_period = filepath.rfind(".")
    if index_period == -1: return [filepath, ""]
    return [filepath[:index_period], filepath[index_period+1:]]

def Get_File_Name(filepath):
    """
    Return the name of the file, minus the file extension, for the file
    specified by [filepath].
    
    Assumes [filepath] is the filepath for a file. If a directory path is
    supplied, an empty string will also be returned.
    
    Get_Name(str) -> str
    """
    # Slash and backslash
    index_slash = filepath.rfind("/")
    index_bslash = filepath.rfind("\\")
    if index_slash == index_bslash == -1: pass # Simple path
    else: # Complex path
        right_most = max(index_slash, index_bslash)
        filepath = filepath[right_most+1:]
    # Find period
    index_period = filepath.rfind(".")
    if index_period == -1: return filepath
    return filepath[:index_period]

def Find_Period_Index(filepath):
    """
    Return the index of a filepath's file extension string. (The index of the
    period.)
    
    Return -1 if the file name has no file extension.
    
    Find_Period_Index(str) -> int
    """
    # Find period
    index_period = filepath.rfind(".")
    if index_period == -1: return -1 # No period
    # Slash and backslash
    index_slash = filepath.rfind("/")
    index_bslash = filepath.rfind("\\")
    if index_slash == index_bslash == -1: return index_period # Simple path
    # Complex path
    right_most = max(index_slash, index_bslash)
    if right_most > index_period: return -1 # Period in folder name only
    return index_period

def Get_Extension(filepath):
    """
    Return the file extension for the file specified by [filepath].
    
    Return an empty string if the file has no extension.
    
    Assumes [filepath] is the filepath for a file. If a directory path is
    supplied, an empty string will also be returned.
    
    Get_Extension(str) -> str
    """
    index_period = Find_Period_Index(filepath)
    if index_period == -1: return ""
    return filepath[index_period+1:]

def Get_Files_W_Extensions(dirpath, extensions):
    """
    Return a list of the full filepaths of every file in [dirpath] which have
    a file extension in [extensions].
    Return an empty list if there are any issues.
    
    @path_in
            (str - dirpath)
            The filepath of the folder of interest.
    @extensions
            (list<str>)
            A list of all acceptable file extensions.
    
    Get_Files_W_Extensions(str, list<str>) -> list<str>
    """
    results = []
    try:
        files = os.listdir(dirpath)
    except:
        return results
    for file_ in files:
        extension = Get_Extension(file_)
        if extension in extensions:
            full_path = dirpath + directory_spacer + file_
            results.append(full_path)
    return results

def Get_Files_W_Substring(dirpath, substring):
    """
    Return a list of the full filepaths of every file in [dirpath] with names
    which contain [substring].
    Return None if there are any issues.
    
    @path_in
            (str - dirpath)
            The filepath of the folder of interest.
    @substring
            (str)
            The target substring
    
    Get_Files_W_Extensions(str, str) -> list<str>
    """
    results = []
    try:
        files = os.listdir(dirpath)
    except:
        return None
    for file_ in files:
        if substring in file_:
            full_path = dirpath + directory_spacer + file_
            results.append(full_path)
    return results

def Validate_Table_File_Format(string):
    """
    Validates the file format specified.
    Return the appropriate delimiter.
    Return an empty string if the file format is invalid.
    
    Validate_File_Format(str) -> str
    """
    return DICT__delim.get(string, "")



# Validate Values ##############################################################

def Validate_Bool(string):
    """
    Validates and returns the boolean specified. Accepts variants of Yes, No,
    True, and False.
    Return a boolean if the string is valid.
    Return None if the string is invalid.
    
    @string
        (str)
        A string denoting a boolean. (Includes Yes/No)
    
    Validate_Bool(str) -> bool
    Validate_Bool(str) -> None
    """
    if string in LIST__yes: return True
    elif string in LIST__no: return False
    else: return None



def Validate_Number(string):
    """
    Validates and returns the number specified.
    Return an integer if possible.
    Return a float if a non-integer number is specified.
    Return None if the input is invalid.
    
    @string
        (str)
        A string denoting a number.
        
    Validate_Number(str) -> int
    Validate_Number(str) -> float
    Validate_Number(str) -> None
    """
    try:
        n = int(string)
    except:
        try:
            n = float(string)
        except:
            return None
    return n

def Validate_Numbers(strings):
    """
    Validates and returns the numbers specified.
    Return as an integer if possible, and a float otherwise.
    Return an empty list if the input is invalid.
    
    @strings
        (list<str>)
        A list of strings denoting numbers.
        
    Validate_Numbers(list<str>) -> list<int/float>
    """
    result = []
    for string in strings: 
        try:
            try:
                n = int(string)
            except:
                n = float(string)
            result.append(n)
        except:
            return []
    return result

def Validate_Int_Positive(string):
    """
    Validates and returns the positive integer specified.
    Return -1 if the input is invalid.
    
    @string
        (str)
        A string denoting a positive integer.
        
    Validate_Int_Positive(str) -> int
    """
    try:
        n = int(string)
    except:
        return -1
    if n < 1: return -1
    return n

def Validate_Ints_Positive(strings):
    """
    Validates and returns the positive integers specified.
    Return an empty list if the input is invalid.
    
    @strings
        (list<str>)
        A list of strings denoting positive integers.
        
    Validate_Ints_Positive(list<str>) -> list<int>
    """
    result = []
    for string in strings: 
        try:
            n = int(string)
            result.append(n)
            if n < 1: return []
        except:
            return []
    return result

def Validate_Int_NonNeg(string):
    """
    Validates and returns the non-negative integer specified.
    Return -1 if the input is invalid.
    
    @string
        (str)
        A string denoting a non-negative integer.
        
    Validate_Int_NonNeg(str) -> int
    """
    try:
        n = int(string)
    except:
        return -1
    if n < 0: return -1
    return n

def Validate_Ints_NonNeg(strings):
    """
    Validates and returns the non-negative integers specified.
    Return an empty list if the input is invalid.
    
    @strings
        (list<str>)
        A list of strings denoting non-negative integers.
        
    Validate_Ints_NonNeg(list<str>) -> list<int>
    """
    result = []
    for string in strings: 
        try:
            n = int(string)
            result.append(n)
            if n < 0: return []
        except:
            return []
    return result

def Validate_Int_Max(string, threshold):
    """
    Validates and returns the integer specified if it does not exceed
    [threshold].
    Return None otherwise.
    
    @string
        (str)
        A string denoting an integer integer.
    @threshold
        (int)
        The maximum permissible value for the numbers in [string].
    
    Validate_Int_Max(str) -> int
    Validate_Int_Max(str) -> None
    """
    try:
        n = int(string)
        if n <= threshold: return n
    except:
        return None
    return None

def Validate_Ints_Max(strings, threshold):
    """
    Validates and returns the integers specified if none exceed [threshold].
    Return an empty list otherwise.
    
    @strings
        (list<str>)
        A list of strings denoting non-negative integers.
    @threshold
        (int)
        The maximum permissible value for the numbers in [string].
        
    Validate_Ints_Max(list<str>) -> list<int>
    """
    result = []
    for string in strings: 
        try:
            n = int(string)
            result.append(n)
            if n > threshold: return []
        except:
            return []
    return result

def Validate_Int_Min(string, threshold):
    """
    Validates and returns the integer specified if none are below [threshold].
    Return None otherwise.
    
    @string
        (str)
        A string denoting an integer integer.
    @threshold
        (int)
        The minimum permissible value for the numbers in [string].
    
    Validate_Int_Min(str) -> int
    Validate_Int_Min(str) -> None
    """
    try:
        n = int(string)
        if n >= threshold: return n
    except:
        return None
    return None

def Validate_Ints_Min(strings, threshold):
    """
    Validates and returns the integers specified if none are below [threshold].
    Return an empty list otherwise.
    
    @strings
        (list<str>)
        A list of strings denoting non-negative integers.
    @threshold
        (int)
        The minimum permissible value for the numbers in [string].
        
    Validate_Ints_Min(list<str>) -> list<int>
    """
    result = []
    for string in strings: 
        try:
            n = int(string)
            result.append(n)
            if n < threshold: return []
        except:
            return []
    return result

def Validate_Float_Positive(string):
    """
    Validates and returns the positive float specified.
    Return -1 if the input is invalid.
    
    @string
        (str)
        A string denoting a positive float.
        
    Validate_Float_Positive(str) -> float
    """
    try:
        n = float(string)
    except:
        return -1
    if n <= 0: return -1
    return n

def Validate_Floats_Positive(strings):
    """
    Validates and returns the positive floats specified.
    Return an empty list if the input is invalid.
    
    @strings
        (list<str>)
        A list of strings denoting positive floats.
        
    Validate_Floats(list<str>) -> list<float>
    """
    result = []
    for string in strings: 
        try:
            n = float(string)
            result.append(n)
            if n < 1: return []
        except:
            return []
    return result

def Validate_Float_NonNeg(string):
    """
    Validates and returns the non-negative float specified.
    Return -1 if the input is invalid.
    
    @string
        (str)
        A string denoting a non-negative float.
        
    Validate_Float_NonNeg(str) -> float
    """
    try:
        n = float(string)
    except:
        return -1
    if n < 0: return -1
    return n

def Validate_Floats_NonNeg(strings):
    """
    Validates and returns the non-negative floats specified.
    Return an empty list if the input is invalid.
    
    @strings
        (list<str>)
        A list of strings denoting non-negative floats.
        
    Validate_Floats(list<str>) -> list<float>
    """
    result = []
    for string in strings: 
        try:
            n = float(string)
            result.append(n)
            if n < 0: return []
        except:
            return []
    return result

def Validate_Float_NonZero(string):
    """
    Validates and returns the non-zero float specified.
    Return -1 if the input is invalid.
    
    @string
        (str)
        A string denoting a non-zero float.
        
    Validate_Float_NonZero(str) -> float
    """
    try:
        n = float(string)
    except:
        return -1
    if n == 0: return -1
    return n

def Validate_Floats_NonZero(string):
    """
    Validates and returns the non-zero floats specified.
    Return an empty list if the input is invalid.
    
    @string
        (str)
        A string denoting a non-zero float.
        
    Validate_Float_NonZero(str) -> float
    """
    result = []
    for string in strings: 
        try:
            n = float(string)
            result.append(n)
            if n == 0: return []
        except:
            return []
    return result

def Validate_Table_Type(string):
    """
    Validates a table file type and returns the delimiter char for that table
    type.
    Return an empty string if the input is invalid.
    
    @string
        (str)
        A string denoting the file type. Acceptable options are:
            tsv - Tab-separated values
            csv - Comma-separated values
            ssv - Space-separated values
    
    Validate_Table_Type(str) -> str
    """
    return DICT__table_ext_to_delim_.get(string, "")

def Validate_Enclosed_String(string):
    """
    Confirms that the string has matching inverted commas at the start and end,
    and return string with those inverted commas removed.
    Return None if the input is invalid.
    
    @string
        (str)
        The string to be processed.
    
    Validate_Enclosed_String(str) -> str
    Validate_Enclosed_String(str) -> None
    """
    if len(string) < 2: return None
    if (string[0] == string[-1] == "\"") or (string[0] == string[-1] == "'"):
        return string[1:-1]
    return None

def Validate_Inc_Exc(string):
    """
    Confirms that the string specifies either include or exclude, and return the
    corresponding ENUM if valid.
    Return None if the input is invalid.
    
    @string
        (str)
        The string to be processed.
    
    Validate_Inc_Exc(str) -> str
    Validate_Inc_Exc(str) -> None
    """
    if string in LIST__include: return INC_EXC.INCLUDE
    if string in LIST__exclude: return INC_EXC.EXCLUDE
    return None



# Validate Advanced ############################################################

def Validate_List_Of_Ints(string, delimiter):
    """
    Validates a string containing multiple integers and returns the integers as
    a list.
    Return an empty list if the input is invalid.
    
    @string
        (str)
        A string containing the list of numbers.
    @delimiter
        (str)
        The delimiter separating the numbers from each other
    
    Validate_List_Of_Ints(str, str) -> list<int>
    """
    values = string.split(delimiter)
    result = []
    for value in values:
        try:
            v = int(value)
            result.append(v)
        except:
            return []
    return result

def Validate_List_Of_Ints_NonNeg(string, delimiter):
    """
    Validates a string containing multiple non-negative integers and returns the
    integers as a list.
    Return an empty list if the input is invalid.
    
    @string
        (str)
        A string containing the list of numbers.
    @delimiter
        (str)
        The delimiter separating the numbers from each other
    
    Validate_List_Of_Ints(str, str) -> list<int>
    """
    values = string.split(delimiter)
    result = []
    for value in values:
        try:
            v = int(value)
            if v < 0: return []
            result.append(v)
        except:
            return []
    return result

def Validate_List_Of_Ints_Positive(string, delimiter):
    """
    Validates a string containing multiple positive integers and returns the
    integers as a list.
    Return an empty list if the input is invalid.
    
    @string
        (str)
        A string containing the list of numbers.
    @delimiter
        (str)
        The delimiter separating the numbers from each other
    
    Validate_List_Of_Ints(str, str) -> list<int>
    """
    values = string.split(delimiter)
    result = []
    for value in values:
        try:
            v = int(value)
            if v < 1: return []
            result.append(v)
        except:
            return []
    return result



# Command Line Parsing (Main) ##################################################

def Strip_Non_Inputs(list1, name):
    """
    Remove the runtime environment variable and program name from the inputs.
    Assumes this module was called and the name of this module is in the list of
    command line inputs.

    @list1
        (list<str>)
        The raw inputs from the command line. (sys.argv)

    @name
        (str)
        The name of the main Python file. Ex. if the name of the program is:
            
            Test.py
        
        ..., and the program was called in Command Line using:
            
            C:\Python27\python.exe Test.py
        
        ..., then @name should be "Test" or "Test.py".
    
    Strip_Non_Inputs(list<str>) -> list<str>
    """
    if name in list1[0]: return list1[1:]
    return list1[2:]



# String Processing ############################################################

def Strip_X(string):
    """
    Strips leading and trailing inverted commans or brackets if a matching pair
    are flanking the string.
    
    Strip_X(str) -> str
    """
    if (    (string[0] == string[-1] == "\"") or
            (string[0] == string[-1] == "\'") or
            (string[0] == "(" and string[-1] == ")") or
            (string[0] == "{" and string[-1] == "}") or
            (string[0] == "[" and string[-1] == "]") or
            (string[0] == "<" and string[-1] == ">")
            ):
        return string[1:-1]
    return string


