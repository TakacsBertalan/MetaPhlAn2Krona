# MetaPhlAn2Krona
Creating a Krona output from Metaphlan

Requirements: Python3, [KronaTools](https://github.com/marbl/Krona/wiki/KronaTools) and a browser for opening the krona html file


How to run:

    python metaphlan2krona.py

Options:

    -h, --help            show this help message and exit
  
    -p PROFILE, --profile=PROFILE
  
                        Name of the MetaPhLan3 taxonomic output file.
                        Alternatively you can specify a folder path and a
                        search string
                        
    -k KRONA, --krona=KRONA
  
                        the Krona output file name [krona.out]
                        
    -s SEARCH, --search-string=SEARCH
  
                        Search string for multiple samples. Generates a single
                        Krona output
                        
    -f FOLDER, --folder-path=FOLDER
  
                        Folder path for input files [./]
                        
    -t TEMPORARY, --temporary-tag=TEMPORARY
  
                        Tag for the temporary files, it will be added to the end of the file name. Temp files are removed at the end of the analysis. [.m2k.temp]
                        

For example inputs and outputs, see the included two metaphlan outputs and the krona.out html file


![image](https://github.com/user-attachments/assets/b79d8a8f-e6a9-46d7-b114-6211be9bbcf2)

