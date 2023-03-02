# Python-program-to-calculate-N50-from-the-FASTA-format-contigs-file.
Python Program to Calculate N50 from the FASTA Format Contigs File
This program uses the BioPython library to read a FASTA format file and extract details such as the number of contigs, total contig length, largest contig ID, largest contig length, and N50 of the contigs. The results are validated using a contigs.fa file with predefined QUAST results.

# Requirements
This program requires the BioPython library to be installed in Python. You can install it using pip:

pip install biopython

# Program Execution
To run the program, execute the n50_tool.sh Bash script and pass the path to your FASTA format file as an argument. The output will be saved in a file named <file_name>.n50.txt in the same directory.

# Implementation Details
The Python program reads the FASTA format file using the BioPython library and iterates over the sequence records to find the largest contig, number of contigs, and total length of contigs. The contig lengths are sorted in descending order and saved in a predefined contig list. The program iterates through the contig list and saves the N50 value when it reaches half of the total length of the contigs.

The n50_tool.sh Bash script uses command-line arguments to get the file path and displays error messages if the argument is not valid. The location of the Bash script is saved to the environmental path to allow for easy execution from any directory.

# Repository Links
GitHub Repository: https://github.com/praneeth728/Python-program-to-calculate-N50-from-the-FASTA-format-contigs-file.
GitHub Pages: https://praneeth728.github.io/Python-program-to-calculate-N50-from-the-FASTA-format-contigs-file.-/git
