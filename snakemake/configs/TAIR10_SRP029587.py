RAWDATA_DIR = '/staging/as/skchoudh/re-ribo-datasets/TAIR10/SRP029587'
OUT_DIR = '/staging/as/skchoudh/re-ribo-analysis/TAIR10/SRP029587'
GENOME_FASTA = '/home/cmb-06/as/skchoudh/genomes/TAIR10/fasta/Arabidopsis_thaliana.TAIR10.dna.toplevel.fa'
CHROM_SIZES = '/home/cmb-06/as/skchoudh/genomes/TAIR10/fasta/Arabidopsis_thaliana.TAIR10.dna.toplevel.sizes'
STAR_INDEX = '/home/cmb-06/as/skchoudh/genomes/TAIR10/star_annotated_ribopod'
GTF_VERSION = 'v44'
GTF = '/home/cmb-06/as/skchoudh/genomes/TAIR10/annotation/Arabidopsis_thaliana.TAIR10.44.gtf'
GENE_BED = '/home/cmb-06/as/skchoudh/github_projects/riboraptor/riboraptor/annotation/TAIR10/v44/gene.bed.gz'
STAR_CODON_BED = '/home/cmb-06/as/skchoudh/github_projects/riboraptor/riboraptor/annotation/TAIR10/v44/start_codon.bed.gz'
STOP_CODON_BED = '/home/cmb-06/as/skchoudh/github_projects/riboraptor/riboraptor/annotation/TAIR10/v44/stop_codon.bed.gz'
CDS_BED = '/home/cmb-06/as/skchoudh/github_projects/riboraptor/riboraptor/annotation/TAIR10/v44/cds.bed.gz'
UTR5_BED = '/home/cmb-06/as/skchoudh/github_projects/riboraptor/riboraptor/annotation/TAIR10/v44/utr5.bed.gz'
UTR3_BED = '/home/cmb-06/as/skchoudh/github_projects/riboraptor/riboraptor/annotation/TAIR10/v44/utr3.bed.gz'
INTRON_BED = '/home/cmb-06/as/skchoudh/github_projects/riboraptor/riboraptor/annotation/TAIR10/v44/intron.bed.gz'
ORIENTATIONS = ['5prime', '3prime']
STRANDS = ['pos', 'neg', 'combined']
FRAGMENT_LENGTHS =  range(18, 39)
RIBOTRICER_ANNOTATION_PREFIX = '/home/cmb-06/as/skchoudh/genomes/TAIR10/ribotricer_v44_annotation_longest'
RIBO_ADAPTER = 'TCGTATGCCGTCTTCTGCTTG'
RNA_ADAPTER=  'TGGAATTCTCGGGTGCCAAGGAACTCCAGTCAC'
ADAPTER = {}
RIBO_SAMPLES = ['SRR966472', 'SRR966473', 'SRR966474', 'SRR966475', 'SRR966476', 'SRR966477']
RNA_SAMPLES = ['SRR966478', 'SRR966479', 'SRR966480', 'SRR966481', 'SRR966482', 'SRR966483', 'SRR966485']
for sample in RIBO_SAMPLES:
  ADAPTER[sample] = RIBO_ADAPTER 

for sample in RNA_SAMPLES:
  ADAPTER[sample] = RNA_ADAPTER 

