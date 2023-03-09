sed "s/\tlncRNA\t/\tncRNA\t/g" data/Schizosaccharomyces_pombe_all_chromosomes.gff3 > data/fixed.gff3
sed -i "s/\tsncRNA\t/\tncRNA\t/g" data/fixed.gff3
