from Bio import SeqIO

# Open the DNA sequence file
seq_file = "C:/Users/kandu/OneDrive/Desktop/BCB/info2/hands_on_assignment3/assembly_spades/contigs.fasta"
seq_records = SeqIO.parse(seq_file, "fasta")

# Initialize variables to keep track of the largest contig,its length,number of contigs,total length
largest_contig_id = None
largest_contig_len = 0
no_of_contigs = 0
total_lenght = 0
contig_lengths = []

# Iterate over the sequence records and find the largest contig,number of contigs,total length
for seq_record in seq_records:
    no_of_contigs+=1
    total_lenght+= len(seq_record.seq)
    length = len(seq_record.seq)
    contig_lengths.append(length) #to keep track of contigs
    if len(seq_record.seq) > largest_contig_len:
        largest_contig_id = seq_record.id
        largest_contig_len = len(seq_record.seq)

# Sort the contig lengths in descending order
contig_lengths.sort(reverse=True)

# Calculate the N50
n50 = None
cumulative_length = 0
for length in contig_lengths:
    cumulative_length += length
    if cumulative_length >= total_lenght / 2:
        n50 = length
        break

# Print the number of contigs, total length of contigs, largest contig length, and N50
print("Number of Contigs:", no_of_contigs)
print("Total Contig Length:", total_lenght)
print("Largest Contig ID:", largest_contig_id)
print("Largest Contig Length:", largest_contig_len)
print("N50:", n50)
