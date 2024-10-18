# Create a Python script that generates a random DNA sequence and saves it in FASTA format. Your script should:

# Generate a random DNA sequence of 1 million base pairs (using A, C, G, T).
# Format the sequence with 80 base pairs per line.
# Save the sequence in FASTA format in the "data" directory, with the filename "random_sequence.fasta".
# Tips:

# Use Python's random module to generate random DNA sequences.
# Remember to open the file in write mode when saving the FASTA data.
# Use string joining for efficient concatenation of large sequences.
# Use a for loop to count characters when adding each line of the sequence to the file.
# (optional, advanced) The textwrap module can help you format the sequence into 80-character lines.

import random 

# generate a random sequence
nucleotides = ''.join(random.choices('ATGC', k = 1_000_000))

# format the sequence with 80 base pairs per line 
format_nucleotides = '\n'.join(nucleotides[i:i+80] for i in range(0, len(nucleotides), 80))

# write to random_sequence.fasta 
with open('bioinformatics_project/data/random_sequence.fasta', 'w') as f:
    f.write(format_nucleotides)

print ("Random DNA sequence generated and saved to bioinformatics_project/data/random_sequence.fasta") 