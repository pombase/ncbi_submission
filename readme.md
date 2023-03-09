* Bioproject: https://www.ncbi.nlm.nih.gov/bioproject/PRJNA13836
* Programme to convert https://www.ncbi.nlm.nih.gov/genbank/table2asn/
* Create submission file template: https://submit.ncbi.nlm.nih.gov/genbank/template/submission/
* Submission with GFF: https://www.ncbi.nlm.nih.gov/genbank/genomes_gff/

run the container:

```
docker build -t ncbi_submission .
docker run -d --name ncbi_submission_container -v $PWD:/work ncbi_submission tail -f /dev/null
docker exec -it ncbi_submission_container /bin/bash
```

Some useful stuff:

```bash
# Print pseudogenes
grep pseudogenic_transcript data/fixed.gff3|cut -f9|cut -d"=" -f3|sort|uniq
```