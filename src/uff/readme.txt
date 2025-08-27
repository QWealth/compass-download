Information about installing and using the Correspondent Network's UFF File Converter software

The Correspondent Network's UFF File Converter is a utility designed to process ISM File Cabinet 
UFF formatted data files.  This distribution contains the following files:


filecab.odf	A sample output definition file which produces output for the typical File Cabinet export files
uff.bat		A batch file which simplifies running the converter utility by specifying common command line default parameters
uffconv.doc	Technical documentation which explains the structure of output definition files
uffconv.exe	The UFF converter utility
readme.txt	This readme file

INSTALLING THE SOFTWARE
To install the converter utility, simply copy the files to any arbitrary directory.  The uff.bat file is
set up to expect a path of c:\uff.  If you install the software to a different directory, simply edit 
uff.bat, changing "c:\uff" to the required value.  The batch file simplifies the command line required 
to call uffconv.exe by specifying certain command line switches in advance.  

RUNNING THE CONVERTER VIA THE SUPPLIED BATCH FILE
To run the converter simply enter "UFF" followed by the name (fully specified) of the source datafile.
For example, if the source datafile is called 19990430.sp100 and is located in c:\data, you would enter
the following command;	uff c:\data\19990430.sp100

The default command line supplied by uff.bat is as follows;

"C:\uff\uffconv.exe %1 /out c:\uff\out /odf c:\uff\FileCab.odf /csv /titles /summary >> c:\uff\run.log"

This command line will call the utility program ("c:\uff\uffconv.exe"), passing it the following switch arguments;
%1		- the UFF filename specified when you called uff.bat (for example "c:\data\19990430.sp100"
/out c:\uff\out - specifies the directory in which output files are to be written, in this case "c:\uff\out"
/odf c:\uff\FileCab.odf - specifies the name of the output definition file to use.  
/csv		- specifies that output records should be formatted using comma separated values
/titles		- specifies that the first record in each output file should contain field labels, as specified in the odf file
/summary	- specifies that the converter should generate a summary report of the process
>> c:\uff\run.log - redirects output from the screen to a log file.


RUNNING THE CONVERTER BY CALLING IT FROM ANOTHER PROGRAM
When you run uffconv via uff.bat you need only supply one command line argument, the UFF filename.  You can
also run uffconv dynamically from another program, supplying the necessary command line arguments as desired.  
Please consult uffconv.doc for more information about command line arguments.  

If you are calling uffconv from another program, please note that it sets errorlevel = 1 if any problems
are encountered during processing.
