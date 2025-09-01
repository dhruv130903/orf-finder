# ORF Finder Tool

# Define start and stop codons
START_CODON = "ATG"
STOP_CODONS = ["TAA", "TAG", "TGA"]

def find_orfs(sequence, min_length=100):
    """
    Finds all ORFs in a given DNA sequence.
    
    sequence: DNA sequence (string)
    min_length: minimum ORF length in nucleotides
    """
    sequence = sequence.upper()  # Ensure sequence is uppercase (standard)
    orfs = []  # List to store found ORFs
    
    # Go through sequence in all three reading frames
    for frame in range(3):
        i = frame
        while i < len(sequence):
            codon = sequence[i:i+3]
            # Check if codon is start codon
            if codon == START_CODON:
                # Found start, now look for stop codon
                for j in range(i+3, len(sequence), 3):
                    stop_codon = sequence[j:j+3]
                    if stop_codon in STOP_CODONS:
                        orf_seq = sequence[i:j+3]  # extract ORF
                        if len(orf_seq) >= min_length:
                            orfs.append((frame+1, i, j+3, orf_seq))
                        break
            i += 3
    return orfs

# Example DNA sequence
dna_seq="ATGAAATTTGGTAGATGCCCTGATGCTAA"

# Run ORF finder
results = find_orfs(dna_seq, min_length=9)

# Print results
for frame, start, end, seq in results:
    print(f"Frame: {frame}, Start: {start}, End: {end}, ORF: {seq}")