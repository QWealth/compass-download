@echo off
rem     Startup defaults for FMSL UFF Converter
rem     Usage: uffconv <filename> <switches>
rem     Where: <filename> is the name of the UFF format data file to expand.
rem     Swithes:
rem		/ODF <odf_file_name>  	The path and filename of the Output Definition file
rem		/OUT <output_dir>	The path and name of the directory for output
rem		/TITLES		Causes field labels to be included as first record of output file
rem		/SUMMARY		Summarizes the contents of the UFF source file
rem		/CSV			Formats output as comma separated values 
rem		/TSV			Format output as tab separated values
rem		/LASTSEP		Enable separator after last field
rem		/NOLASTSEP		Prevent separator after last field <default>
rem		/NOWARND		Inhibit data value warnings
rem		/DQUOTES		Surround data fields with double quotes <default>
rem		/NOQUOTES		Do not surround data fields with double quotes <default>
rem		/FNUL			Special file format NUL terminated text
rem		/FDAS1		Special file format DAS1
rem		/FDAS4		Special file format DAS4
rem		/FAP			Special file format AP
rem		/SD			Use in order to browse data in UFF source file
rem		/SE			Show UFF internal extra trailing characters
rem		/SG			Show UFF internal group and field names
rem		/SR			Show UFF raw internal data
rem		/SS			Use in order to browse UFF data file structure
rem
rem     This batch file passes the most common command line parameters to uffconv.exe

 if %1.==. goto :nofile
 if not exist %1 goto :nofile
rem CHANGE THE PATH TO AGREE WITH YOUR INSTALLATION
c:\uff\uffconv.exe %1 /fnul /out c:\uff\out /odf c:\uff\FileCab.odf /csv /titles /summary >> c:\uff\run.log
 if errorlevel 1 goto :problem
 goto :end
:problem
 echo A problem was encountered. Consult your system administrator.
 goto :end
:nofile
 echo Please specify a valid input file
 goto :end
:end
