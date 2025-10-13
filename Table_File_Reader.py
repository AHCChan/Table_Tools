"""
TABLE FILE READER
(version 2.1)
by Angelo Chan

This module contains a Class capable of reading and interpretting files which
contain data tables and returning the values of each row, line by line.
"""

# Imported Modules #############################################################

from File_Reader import *


# Enums ########################################################################

class KSR:
    KEEP=1
    SKIP=2
    REAR=3



# Lists ########################################################################

LIST__csv = ["CSV", "Csv", "csv"]
LIST__tsv = ["TSV", "Tsv", "tsv", "TAB", "Tab", "tab"]
LIST__ssv = ["SSV", "Ssv", "ssv"]

# LIST__newline
try:
    test = LIST__newline
except:
    LIST__newline = ["\n", "\r", "\n\r", "\r\n"]
    # Should already exist in imported modules



# Dictionaries #################################################################

DICT__delimiters = {}
for i in LIST__csv: DICT__delimiters[i] = ","
for i in LIST__tsv: DICT__delimiters[i] = "\t"
for i in LIST__ssv: DICT__delimiters[i] = " "



# Classes ######################################################################

class Table_Reader(File_Reader):
    """
    The Table Reader is a file reader designed specifically to work with CSV,
    TSV, or SSV files.
    
    The Table Reader acts as a two-phase buffer to store both the "current"
    row and the "next" row, not every row in the file.
    
    The Table Reader defaults to Tab Separated Format behaviour.
    
    Designed for the following use:
    
    f = Table_Reader()
    f.Set_New_Path("F:/Filepath.csv")
    f.Autodetect_Delimiter() # OR f.Set_Delimiter(",")
    f.Set_Enclosers(["\"", "'"])  # Optional
    f.Set_Keep_Enclosers(True)    # Optional
    f.Set_Header_Params(["#", 1]) # Optional
    #                               Skip:
    #                                   all rows starting with "#", THEN
    #                                   1 row
    f.Set_Adv_Header_Params([[KSR.KEEP, 1], [KSR.SKIP, "#"], [KSR.REAR, 1]])
    #                                   # Optional
    #                                   # Keep the first row
    #                                   # Skip all rows starting with "#"
    #                                   # Rearrange the contents of the next row
    f.Open() # Read_Header() is automatically called during Open()
    
    while not f.EOF:
        f.Read()
        # Your code - You may access buffered elements in f
    f.Close()
    """
    
    # Minor Configurations #####################################################
    
    empty_element = [""]
    
    # Minor Configurations #####################################################
    
    _CONFIG__print_errors = True
    _CONFIG__print_progress = False
    _CONFIG__print_metrics = True
    
    
    
    # Strings ##################################################################
    
    _MSG__object_type = "Table File Reader"
    _MSG__units_of_measure = "Rows"
    
    _MSG__no_delimiter = "No delimiter specified."
    _MSG__no_extension = "No file extension detected."
    
    _MSG__header_oob = "Header parameter out-of-bounds error."
    _MSG__header_adv_unkn = "Advanced header parsing, "\
            "unknown section type error."
    
    

    # Constructor & Destructor #################################################
    
    def __init__(self, file_path="", auto_open=False, delimiter="",
                enclosers=[], header_params=[], keep_enclosers=True):
        """
        Creates a File Reader object. The filepath will be tested if a
        filepath is supplied.
        """
        File_Reader.__init__(self, file_path)
        self.Set_Delimiter(delimiter)
        self.Set_Enclosers(enclosers)
        self.Set_Keep_Enclosers(keep_enclosers)
        self.Set_Header_Params(header_params)
        self.prev_raw = self.current_raw = self.next_raw = ""
        self.header_text = ""
    
    
    
    # Property Methods #########################################################
    
    def __getitem__(self, arg):
        """
        Access items using square brackets, the same way one would access items
        in a list.
        """
        try:
            return self.current_element[arg]
        except:
            if type(arg) != int:
                raise TypeError("list indices must be integers, not str")
            if arg > len(self.current_element):
                raise IndexError("list index out of range")
            raise Exception("Unknown error in Table_File_Reader.__getitem__")
    
    def Autodetect_Delimiter(self):
        """
        Automatically select a delimiter to use, based on the currently set
        file's file extension.
        """
        if not self.file_path:
            self.printE(self._MSG__unspecified_file_path)
            return
        delim = self.Detect_Delimiter()
        self.Set_Delimiter(delim)
    
    def Detect_Delimiter(self, file_path=""):
        """
        Return a delimiter based on the file name. Use the stored file name if
        no file path was specified.
        
        Return an empty string if no valid 
        """
        if not file_path: file_path = self.file_path
        if not file_path:
            self.printE(self._MSG__unspecified_file_path)
            return
        extension = self.Get_Extension(file_path)
        if not extension:
            self.printE(self._MSG__no_extension)
            return
        delim = DICT__delimiters.get(extension)
        return delim
    
    def Set_Delimiter(self, delimiter):
        """
        Set the delimiter to the input.
        """
        self.delimiter = delimiter
    
    def Set_Enclosers(self, enclosers):
        """
        Set the escape character set to the input.
        """
        self.enclosers = enclosers

    def Set_Keep_Enclosers(self, boolean):
        """
        Set whether or not to keep the enclosers as part of the final result.
        """
        self.keep_enclosers = boolean

    def Set_Header_Params(self, params):
        """
        Set the header params of the file.
        
        [params] is expected to be a list of integers and/or strings. For
        integers, that many rows will be added directly to the "header_text"
        variable. For strings, rows will be added directly to the "header_text"
        variable as long as those rows begin with the string specified.
        """
        self.header_params = params

    def Set_Adv_Header_Params(self, adv_params):
        """
        Set the advanced header params of the file. These control what is
        outputted by Get_Adv_Processed_Header_Text.
        
        Overrides the settings created by Set_Header_Params.
        
        [params] is a series of pairs. The first variable in the pair is an
        integer denoting the action to be taken:
            1:  Keep the lines being specified
            2:  Skip the lines being specified
            3:  Treat the contents of the next line as column headers
        The second variable specifies the line(s) to which the action is to be
        applied:
            (int)   A set number of lines.
            (str)   An unknown number of lines which begin with said string
        """
        self.adv_header_params = adv_params
        basic_params = []
        for pair in adv_params:
            action, specifier = pair
            if action == KSR.REAR:
                basic_params.append(1)
            else:
                basic_params.append(specifier)
        self.header_params = basic_params

    def Get_Header_Text(self):
        """
        Return the header text which does not constitute a main part of the data
        file.
        """
        return self.header_text

    def Get_Processed_Header_Text(self, params):
        """
        Return part of the header text as a list of lines.
        Return None if [params] go out-of-bounds.
        
        [adv_params] is to be a list of pairs. Each pair consists of a boolean
        and either an integer or a string. The boolean specifies whether to
        return the section being specified or not (True = keep), while the
        integers and/or strings specify a section of the header text.
        """
        lines = self.header_text.split("\n")
        if lines[-1] == "": lines = lines[:-1]
        results = []
        for section in params:
            keep, specifier = section
            if type(specifier) == int:
                while specifier > 0:
                    if not lines:
                        self.printE(self._MSG__header_oob)
                        return None
                    else:
                        line = lines.pop(0)
                        if keep:
                            results.append(line)
                    specifier = specifier - 1
            else: # char
                read_flag = True
                while read_flag:
                    if lines:
                        if lines[0].startswith(specifier):
                            line = lines.pop(0)
                            if keep:
                                results.append(line)
                        else:
                            read_flag = False
                    else:
                        read_flag = False
        return results

    def Adv_Process_Header_Text(self, adv_params=None):
        """
        Advanced method for processing header text.
        Return the text that is to be written directly into output file, and the
        column headers if column headers were specified (using KSR.REAR).
        If column headers were not specified, return an empty list.
        
        [adv_params] is to be a list of pairs. Each pair consists of a boolean
        and either an integer or a string. The boolean specifies whether to
        return the section being specified or not (True = keep), while the
        integers and/or strings specify a section of the header text.
        """
        # Advanced params
        if not adv_params: adv_params = self.adv_header_params
        # Setup
        sb = ""
        headers = []
        # Initial split
        lines = self.header_text.split("\n")
        if lines[-1] == "": lines = lines[:-1]
        # Loop
        for section in adv_params:
            ksr, specifier = section
            if ksr == KSR.REAR:
                if lines:
                    headers = lines[0].split(self.delimiter)
                    lines.pop(0)
            else:
                if type(specifier) == int:
                    while lines and specifier > 0:
                        line = lines.pop(0)
                        if ksr == KSR.KEEP:
                            sb += line + "\n"
                        specifier = specifier - 1
                elif type(specifier) == str:
                    while lines and lines[0].startswith(specifier):
                        line = lines.pop(0)
                        if ksr == KSR.KEEP:
                            sb += line + "\n"
                else:
                    self.printE(self._MSG__header_adv_unkn)
        # Finish and return
        return [sb, headers]
    
    def Copy_Element(self, element):
        """
        Return a copy of the current row, sanitized.
        """
        return list(element)
    
    def Get_Size(self):
        """
        Return the size of the table file.
        
        Return -1 if no filepath has been set.
        """
        if self.file_path:
            count = 0
            f = open(self.file_path, "U")
            line = f.readline()
            if self.header_params:
                for param in self.header_params:
                    if type(param) == int:
                        while param > 0:
                            line = self.file.readline()
                            param -= 0
                    if type(param) == str:
                        while line.find(param) == 0:
                            line = self.file.readline()
            while line:
                count += 1
                line = f.readline()
            f.close()
            return count
        return -1
    
    def Get_Raw(self):
        """
        Return the raw text of the current line.
        """
        return self.prev_raw        
    
    
    
    # File I/O Methods #########################################################
    
    def Open(self, new_path=""):
        """
        Attempts to open a file. If a file path is not specified, the stored
        file path will be used instead.
        
        Requires at least one delimiter to be set.
        """
        if self.delimiter:
            File_Reader.Open(self, new_path)
        else:
            self.printE(self._MSG__no_delimiter)
            return
    
    
    
    # File Reading Methods #####################################################
    
    def Read_Header(self):
        """
        Read in the header rows of the file and store them separately according
        to the params specified.
        
        [params] is expected to be a list of integers and/or strings. For
        integers, that many rows will be added directly to the "header_text"
        variable. For strings, rows will be added directly to the "header_text"
        variable as long as those rows begin with the string specified.
        """
        params = self.header_params
        sb = ""
        line = self.file.readline()
        for param in params:
            if type(param) == int:
                while param > 0:
                    sb += line
                    line = self.file.readline()
                    param -= 1
            if type(param) == str:
                while line.find(param) == 0:
                    sb += line
                    line = self.file.readline()
        self.next_raw = line
        self.header_text = sb
    
    def _get_next_element(self):
        """
        Read in the next row and process it.
        
        Return an empty string if the end of the file has been reached.
        """
        self.prev_raw = self.current_raw
        self.current_raw = self.next_raw
        self.next_raw = self.file.readline()
        if self.enclosers:
            return self._process_raw(self.current_raw, self.delimiter,
                    self.enclosers, self.keep_enclosers)
        return self._process_raw__SIMPLE(self.current_raw, self.delimiter)
    
    def _process_raw(self, raw_str, delim, enclosers, keep_enclosers):
        """
        Process a line of raw text from the table file into a list of strings.
        
        Delimiters enclosed within [enclosers] chars are not treated delimiters.
        """
        flag = False
        active_encloser = ""
        sb = ""
        results = []
        for c in raw_str:
            if flag:
                if c == active_encloser:
                    if keep_enclosers: sb += c
                    flag = False
                else:
                    sb += c
            else:
                if c in enclosers:
                    if keep_enclosers: sb += c
                    flag = True
                    active_encloser = c
                elif c == delim:
                    results.append(sb)
                    sb = ""
                else:
                    sb += c
        if sb and sb[-1] in LIST__newline: sb = sb[:-1]
        results.append(sb)
        return results
    
    def _process_raw__SIMPLE(self, raw_str, delim):
        """
        Process a line of raw text from the table file into a list of strings.
        
        This is the simple version of the function for when there are no
        enclosers.
        """
        sb = ""
        results = []
        for c in raw_str:
            if c == delim:
                results.append(sb)
                sb = ""
            else:
                sb += c
        if sb and sb[-1] in LIST__newline: sb = sb[:-1]
        results.append(sb)
        return results
    
    def Is_Empty_Element(self, element):
        """
        Return True if [element] is an "empty" element, that is to say, an empty
        string.
        
        Return False otherwise.
        """
        if element == self.empty_element:
            return True
        return False



# Functions ####################################################################

def Col_No_To_Set(files, file_format, col_no=0):
    """
    Return a set of all the values found in column number [col_no] of the files
    in [files].
    
    @files
            (list<str - dirpath>)
            A list of the files to be scanned.
    @file_format
            (str)
            The file format of the input file. Acceptable options are:
                tsv - Tab-separated values
                csv - Comma-separated values
                ssv - Space-separated values
    @col_no
            (int)
            The column number to be looked at.
            This function uses a 0-indexing system. (i.e., the first column is
            0)
    
    Col_No_To_Set(list<str>, str, int) -> set<str>
    """
    # Setup - Results
    result = set([])
    
    # Setup - Readers
    f = Table_Reader()
    delim = DICT__delimiters[file_format]
    f.Set_Delimiter(delim)
    
    # Read
    for file_ in files:
        f.Set_New_Path(file_)
        f.Open()    
        while not f.EOF:
            f.Read()
            item = f[col_no]
            result.add(item)
        f.Close()
    
    # Return
    return result









