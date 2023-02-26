from Bio import SeqIO

# Open the DNA sequence file
seq_file = "C:/Users/kandu/OneDrive/Desktop/BCB/info2/hands_on_assignment3/assembly_spades/contigs.fasta"
seq_records = SeqIO.parse(seq_file, "fasta")

# Initialize variables to keep track of the largest contig,its length,number of contigs,total length
largest_contig_id = None
largest_contig_len = 0
no_of_contigs=0
total_lenght=0
#iterating through records

# Iterate over the sequence records and find the largest contig,number of contigs,total length
for seq_record in seq_records:
    no_of_contigs+=1
    total_lenght+= len(seq_record.seq)
    if len(seq_record.seq) > largest_contig_len:
        largest_contig_id = seq_record.id
        largest_contig_len = len(seq_record.seq)

# Print the largest contig ID,length,number of contigs,total length
print("Number of Contigs:", no_of_contigs)
print("Total Contig Length:", total_lenght)
print("Largest Contig ID:", largest_contig_id)
print("Largest Contig Length:", largest_contig_len)
