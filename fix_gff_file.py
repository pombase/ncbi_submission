import pandas
import re

accepted_feature_types = [
'gene',
'CDS',
'mRNA',
'exon',
'five_prime_UTR',
'three_prime_UTR',
'rRNA',
'tRNA',
'ncRNA',
'tmRNA',
'transcript',
'mobile_genetic_element',
'origin_of_replication',
'promoter',
'repeat_region',
]

gff_cols = ['seqid', 'source', 'type', 'start', 'end', 'score', 'strand', 'phase', 'attributes']

data = pandas.read_csv('data/Schizosaccharomyces_pombe_all_chromosomes.gff3', sep='\t', na_filter=False, names=gff_cols, skiprows=1)

# Annotate pseudogenes
def format_regex(x):
    # Function to make a regex that matches the attributes of any pseudogene
    transcript_id, gene_id = re.search("ID=(.+?);Parent=(.+)", x).groups()
    # The gene itself, the transcript itself, any children of the transcript (exons and introns)
    return f'ID={gene_id}(;|$)|ID={transcript_id}(;|$)|Parent={transcript_id}(;|$)'

pseudogene_regex = '|'.join(data.loc[data.type == 'pseudogenic_transcript', 'attributes'].apply(format_regex))
pseudo = data.attributes.str.contains(pseudogene_regex)

#TODO: change the qualifier type
data.loc[pseudo, 'attributes'] = data.loc[pseudo, 'attributes'].apply(lambda x: x + ';pseudogene=unknown')

feature_mappings = pandas.read_csv('mappings/mappings.tsv', sep='\t', na_filter=False)
mappings_dict = dict(zip(feature_mappings.feature, feature_mappings.replace_by))
data['type'] = data['type'].apply(lambda x: mappings_dict[x] if x in mappings_dict else x)

# Drop the lines without type
data = data.loc[data.type != '', :].copy()

valid_systematic_ids = set(pandas.read_csv('data/gene_IDs_names.tsv', sep='\t', na_filter=False, skiprows=1)['gene_systematic_id'])
# Set locus_tag qualifier
def get_locus_tag(x):
    match = re.match('ID=(.+?)(;|$)', x)
    if match and match.groups()[0] in valid_systematic_ids:
        return match.groups()[0]

    match = re.match('ID=(.+?\..+?)(?=\.)', x)
    if match and match.groups()[0] in valid_systematic_ids:
        return match.groups()[0]

    print((f'Cannot assign locus to {x}'))

data.to_csv('data/fixed.gff3', sep='\t', index=False, header=False)

data.loc[:, 'attributes'] = data.loc[:, 'attributes'].apply(lambda x: f'{x};{get_locus_tag(x)}')


