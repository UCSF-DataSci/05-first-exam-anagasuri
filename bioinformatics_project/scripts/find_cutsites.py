# Accept two arguments: the FASTA file path (data/random_sequence.fasta) and a cut site sequence (e.g., "G|GATCC")
# Read the FASTA file and save the DNA sequence to a variable omitting whitespace.
# Find all occurrences of the cut site (specified below) in the DNA sequence.
# Find all pairs of cut site locations that are 80,000-120,000 base pairs (80-120 kbp) apart.
# Print the total number of cut site pairs found and the positions of the first 5 pairs.
# Save a summary of the results (example below) in the results directory as "cutsite_summary.txt".

import re
import argparse

# read in fasta file
def read_fasta(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
        dna_sequence = ''.join(lines).replace('\n', '') # concatenates all lines in the fasta file by joining and getting rid of new lines
    return dna_sequence


# Find all occurrences of the cut site in the DNA sequence. "G|GATCC"
def cutSites(fastaFile, cut_site):
    cutSiteStarts = [] # empty array to store starting indices of cutsite 
    cut_site = cut_site.replace('|', '') # removes the | from "G|GATCC"
    for m in re.finditer(cut_site, fastaFile): # m is every occurance of "G|GATCC" in fastaFile
        cutSiteStarts.append(m.start()) # everytime there is an occurance of "G|GATCC", its starting index gets added to cutSiteStarts[] arry 
    return cutSiteStarts # returns the array of starting indices of every occurance of "G|GATCC"


# Find all pairs of cut site locations that are 80,000-120,000 base pairs (80-120 kbp) apart.
def CutSiteSearch(cutSiteStarts, min_distance=80000, max_distance=120000):
    cutSitePairs = [] # empty array storing tuples of 2 starting indices that satisfy the 80-120 kb boundaries 
    for startCut in range(len(cutSiteStarts)): # for each starting index in the array of starting indices 
        for nextCut in range(startCut + 1, len(cutSiteStarts)): # for each NEXT starting index in the array of starting indices
            distance = cutSiteStarts[nextCut] - cutSiteStarts[startCut] # subtract the first starting index from the NEXT starting index
            if min_distance <= distance <= max_distance: # compare that value to 80 and 120 kb
                cutSitePairs.append((cutSiteStarts[startCut], cutSiteStarts[nextCut])) # if the value falls between the boundaries, append to cutSiteParis
            elif distance > max_distance: # if value goes beyond 120kb, break out of nested loop, and iterate to the next startCut value
                break
    return cutSitePairs # return array of tuples of starting indices that satisfy the 80-120 kb boundaries 

def Summary(cutSitePairs, cutSiteStarts, output): 
    with open(output, 'w') as f:
        f.write(f"Analzying cutsite: ""G|GATCC""\n") 
        f.write(f"Total cut sites in sequence: {len(cutSiteStarts)}\n") 
        f.write(f"Total number of cut site pairs: {len(cutSitePairs)}\n")
        f.write("Positions of first 5 pairs:\n")
        for i, (start, end) in enumerate(cutSitePairs[:5]):
            f.write(f"{i+1}. {start}-{end}\n") 


def main():

    # take command line arguments 
    parser = argparse.ArgumentParser(description="Find pairs of cutsites for 'G|GATCC' in the given FASTA file.")
    parser.add_argument('fasta_file', type=str, help="Path to the FASTA file.")

    parser.add_argument('cut_site', type=str, help="The cut site sequence: 'G|GATCC'.")

    args = parser.parse_args()

    # call functions
    fastaFile = read_fasta('../data/random_sequence.fasta')
    cutSiteStarts = cutSites(fastaFile, "G|GATCC")
    result = CutSiteSearch(cutSiteStarts)


    # print results 
    print("Analzying cutsite: ""G|GATCC"" ")
    print("Total cut sites in sequence:", len(cutSiteStarts))
    print("Total cut site pairs found:", len(result)) 
    # format the first 5 pair of cutsite indices in a numbered list 
    for i, (start, end) in enumerate(result[:5]):
            print(f"{i+1}. {start:,}–{end:,}")

    output = "../results/cutsite_summary.txt"
    Summary(result, cutSiteStarts, output) 

if __name__ == "__main__":
    main()
