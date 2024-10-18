import argparse 

parser = argparse.ArgumentParser(description="Generate a complementary and reverse complementary nucleotide sequence")
parser.add_argument('sequence', type=str, help='The nucleotide sequence should include A,T,G,C. Input like ATGC')

# parse command line arguments
args = parser.parse_args()

# get the input sequence
input = args.sequence.upper()

# complementary dict
complements = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

# create complement
complementary = ''.join(complements[nuc] for nuc in input if nuc in complements)

# reverse sequence
reverse = input[::-1]

# reverse complement
reverse_complement = ''.join(complements[nuc] for nuc in reverse if nuc in complements)

# Print results
print(f"Input Sequence: {input}")
print(f"Complement: {complementary}")
print(f"Reverse: {reverse}")
print(f"Reverse Complement: {reverse_complement}") 

