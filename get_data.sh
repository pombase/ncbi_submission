set -e

mkdir -p bin
mkdir -p data

# Download the bins of table2asn
# curl -k https://ftp.ncbi.nlm.nih.gov/asn1-converters/by_program/table2asn/linux64.table2asn.gz --output bin/table2asn.gz
# gzip -fd bin/table2asn.gz
# chmod +x bin/table2asn

# Download the pombase genome sequence as fasta and the features as gff

# curl -k https://www.pombase.org/data/genome_sequence_and_features/genome_sequence/Schizosaccharomyces_pombe_all_chromosomes.fa.gz --output data/Schizosaccharomyces_pombe_all_chromosomes.fa.gz
# gzip -fd data/Schizosaccharomyces_pombe_all_chromosomes.fa.gz
# curl -k https://www.pombase.org/data/genome_sequence_and_features/gff3/Schizosaccharomyces_pombe_all_chromosomes.gff3.gz --output data/Schizosaccharomyces_pombe_all_chromosomes.gff3.gz
# gzip -fd data/Schizosaccharomyces_pombe_all_chromosomes.gff3.gz

# Download PomBase systematic ids list
curl -k https://www.pombase.org/data/names_and_identifiers/gene_IDs_names.tsv --output data/gene_IDs_names.tsv

bin/table2asn -M n -J -c w -euk -t template.sbt -gaps-min 10 -l paired-ends -j "[organism=Schizosaccharomyces pombe] [isolate=972h-]" -i data/Schizosaccharomyces_pombe_all_chromosomes.fa -f data/fixed.gff3 -o output_file.sqn -Z -V b