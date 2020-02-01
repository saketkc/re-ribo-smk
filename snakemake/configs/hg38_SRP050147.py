RAWDATA_DIR = '/staging/as/skchoudh/re-ribo-datasets/hg38/SRP050147'
OUT_DIR = '/staging/as/skchoudh/re-ribo-analysis/hg38/SRP050147'
GENOME_FASTA = '/home/cmb-06/as/skchoudh/genomes/hg38/fasta/Homo_sapiens.GRCh38.dna_sm.primary_assembly.fa'
CHROM_SIZES = '/home/cmb-06/as/skchoudh/genomes/hg38/fasta/Homo_sapiens.GRCh38.dna_sm.primary_assembly.sizes'
STAR_INDEX = '/home/cmb-06/as/skchoudh/genomes/hg38/star_annotated_ribopod'
GTF_VERSION = 'v96'
GTF = '/home/cmb-06/as/skchoudh/genomes/hg38/annotation/Homo_sapiens.GRCh38.96.gtf'
GENE_BED = '/home/cmb-06/as/skchoudh/github_projects/riboraptor/riboraptor/annotation/hg38/v96/gene.bed.gz'
STAR_CODON_BED = '/home/cmb-06/as/skchoudh/github_projects/riboraptor/riboraptor/annotation/hg38/v96/start_codon.bed.gz'
STOP_CODON_BED = '/home/cmb-06/as/skchoudh/github_projects/riboraptor/riboraptor/annotation/hg38/v96/stop_codon.bed.gz'
CDS_BED = '/home/cmb-06/as/skchoudh/github_projects/riboraptor/riboraptor/annotation/hg38/v96/cds.bed.gz'
UTR5_BED = '/home/cmb-06/as/skchoudh/github_projects/riboraptor/riboraptor/annotation/hg38/v96/utr5.bed.gz'
UTR3_BED = '/home/cmb-06/as/skchoudh/github_projects/riboraptor/riboraptor/annotation/hg38/v96/utr3.bed.gz'
INTRON_BED = '/home/cmb-06/as/skchoudh/github_projects/riboraptor/riboraptor/annotation/hg38/v96/intron.bed.gz'
ORIENTATIONS = ['5prime', '3prime']
STRANDS = ['pos', 'neg', 'combined']
FRAGMENT_LENGTHS =  range(18, 39)
RIBOTRICER_ANNOTATION_PREFIX = '/home/cmb-06/as/skchoudh/genomes/hg38/ribotricer_v96_annotation_longest'
