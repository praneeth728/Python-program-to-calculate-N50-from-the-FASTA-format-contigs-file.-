from Bio import SeqIO

# Open the DNA sequence file
seq_file = "C:/Users/kandu/OneDrive/Desktop/BCB/info2/hands_on_assignment3/assembly_spades/contigs.fasta"
seq_records = SeqIO.parse(seq_file, "fasta")

# Initialize variables to keep track of the largest contig and its length
largest_contig_id = None
largest_contig_len = 0

# Iterate over the sequence records and find the largest contig
for seq_record in seq_records:
    if len(seq_record.seq) > largest_contig_len:
        largest_contig_id = seq_record.id
        largest_contig_len = len(seq_record.seq)

# Print the largest contig ID and length
print("Largest Contig ID:", largest_contig_id)
print("Largest Contig Length:", largest_contig_len)
