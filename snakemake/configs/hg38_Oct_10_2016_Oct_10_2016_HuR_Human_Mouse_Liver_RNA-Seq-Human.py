
RAWDATA_DIR = '/home/cmb-06/as/skchoudh/dna/Oct_10_2016_HuR_Human_Mouse_Liver/rna-seq/Penalva_L_08182016/human'
OUT_DIR = '/staging/as/skchoudh/rna/Oct_10_2016_HuR_Human_Mouse_Liver_ribocop_run_Jan2019/RNA-Seq-Human'
GENOME_FASTA = '/home/cmb-panasas2/skchoudh/genomes/hg38/fasta/hg38.fa'
CHROM_SIZES = '/home/cmb-panasas2/skchoudh/genomes/hg38/fasta/hg38.chrom.sizes'
STAR_INDEX = '/home/cmb-panasas2/skchoudh/genomes/hg38/star_annotated'
GTF = '/home/cmb-panasas2/skchoudh/genomes/hg38/annotation/gencode.v25.annotation.gtf'
GENE_BED = '/home/cmb-panasas2/skchoudh/github_projects/riboraptor/riboraptor/annotation/hg38/v25/gene.bed.gz'
STAR_CODON_BED = '/home/cmb-panasas2/skchoudh/github_projects/riboraptor/riboraptor/annotation/hg38/v25/start_codon.bed.gz'
STOP_CODON_BED = '/home/cmb-panasas2/skchoudh/github_projects/riboraptor/riboraptor/annotation/hg38/v25/stop_codon.bed.gz'
CDS_BED = '/home/cmb-panasas2/skchoudh/github_projects/riboraptor/riboraptor/annotation/hg38/v25/cds.bed.gz'
UTR5_BED = '/home/cmb-panasas2/skchoudh/github_projects/riboraptor/riboraptor/annotation/hg38/v25/utr5.bed.gz'
UTR3_BED = '/home/cmb-panasas2/skchoudh/github_projects/riboraptor/riboraptor/annotation/hg38/v25/utr3.bed.gz'
INTRON_BED = '/home/cmb-panasas2/skchoudh/github_projects/riboraptor/riboraptor/annotation/hg38/v25/intron.bed.gz'
ORIENTATIONS = ['5prime', '3prime']
STRANDS = ['pos', 'neg', 'combined']
FRAGMENT_LENGTHS =  range(18, 39)
