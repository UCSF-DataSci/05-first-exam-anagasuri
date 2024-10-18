# create project directory and also subdirectories
mkdir -p bioinformatics_project/{data,scripts,results}

# python files within scripts subdirectory
touch bioinformatics_project/scripts/{generate_fasta.py,dna_operations.py,find_cutsites.py}

# cutsite_summary.txt empty file within results subdirectory
touch bioinformatics_project/results/cutsite_summary.txt

# random_sequency.fasta empty file within data subdirectory
touch bioinformatics_project/data/random_sequence.fasta

# README.md file in main project directory with description 
echo "# Bioinformatics Project" > bioinformatics_project/README.md
echo "## This project includes 3 subdirectories: data, scripts, and results" >> bioinformatics_project/README.md
echo "## The results subdirectory contains the empty textfile cutsite_summary.txt" >> bioinformatics_project/README.md
echo "## The data subdirectory contains the empty text fasta file random_sequence.fasta" >> bioinformatics_project/README.md

echo "Project directory structure created successfully:" 
tree bioinformatics_project
