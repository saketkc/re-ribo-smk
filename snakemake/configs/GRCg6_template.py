RAWDATA_DIR = '/staging/as/skchoudh/re-ribo-datasets/GRCg6/'
OUT_DIR = '/staging/as/skchoudh/re-ribo-analysis/GRCg6/'
GENOME_FASTA = '/home/cmb-panasas2/skchoudh/genomes/GRCg6/fasta/Gallus_gallus.GRCg6a.dna.toplevel.fa'
CHROM_SIZES = '/home/cmb-panasas2/skchoudh/genomes/GRCg6/fasta/Gallus_gallus.GRCg6a.dna.toplevel.sizes'
STAR_INDEX = '/home/cmb-panasas2/skchoudh/genomes/GRCg6/star_annotated_ribopod'
GTF_VERSION = 'v96'
GTF = '/home/cmb-panasas2/skchoudh/genomes/GRCg6/annotation/Gallus_gallus.GRCg6a.96.chr.gtf'
GENE_BED = '/home/cmb-panasas2/skchoudh/github_projects/riboraptor/riboraptor/annotation/GRCg6/v96/gene.bed.gz'
STAR_CODON_BED = '/home/cmb-panasas2/skchoudh/github_projects/riboraptor/riboraptor/annotation/GRCg6/v96/start_codon.bed.gz'
STOP_CODON_BED = '/home/cmb-panasas2/skchoudh/github_projects/riboraptor/riboraptor/annotation/GRCg6/v96/stop_codon.bed.gz'
CDS_BED = '/home/cmb-panasas2/skchoudh/github_projects/riboraptor/riboraptor/annotation/GRCg6/v96/cds.bed.gz'
UTR5_BED = '/home/cmb-panasas2/skchoudh/github_projects/riboraptor/riboraptor/annotation/GRCg6/v96/utr5.bed.gz'
UTR3_BED = '/home/cmb-panasas2/skchoudh/github_projects/riboraptor/riboraptor/annotation/GRCg6/v96/utr3.bed.gz'
INTRON_BED = '/home/cmb-panasas2/skchoudh/github_projects/riboraptor/riboraptor/annotation/GRCg6/v96/intron.bed.gz'
ORIENTATIONS = ['5prime', '3prime']
STRANDS = ['pos', 'neg', 'combined']
FRAGMENT_LENGTHS =  range(18, 39)
RIBOTRICER_ANNOTATION_PREFIX = '/home/cmb-06/as/skchoudh/genomes/GRCg6/ribotricer_v96_annotation_longest'