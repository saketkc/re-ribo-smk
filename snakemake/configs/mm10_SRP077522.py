## Absolute location where all raw files are
RAWDATA_DIR = '/staging/as/skchoudh/re-ribo-datasets/mus_musculus/SRP077522'

## Output directory
OUT_DIR = '/staging/as/skchoudh/re-ribo-analysis_orig/mm10/SRP077522'

## Genome fasta location
GENOME_FASTA = '/home/qcb-panasas/skchoudh/genomes/mm10/fasta/mm10.fa'

## Chromosome sizes location
CHROM_SIZES = '/home/qcb-panasas/skchoudh/genomes/mm10/fasta/mm10.chrom.sizes'

## Path to STAR index (will be generated if does not exist)
STAR_INDEX = '/home/qcb-panasas/skchoudh/genomes/mm10/star_annotated'

## GTF path
GTF = '/home/qcb-panasas/skchoudh/genomes/mm10/annotation/gencode.vM11.annotation.gtf'

## GenePred bed downloaded from UCSC
## (this is used for inferring the type of experiment i.e stranded/non-stranded
## and hence is not required)
GENE_BED = '/home/qcb-panasas/skchoudh/genomes/mm10/annotation/gencode.vM11.genes.bed'

## Path to bed file with start codon coordinates
START_CODON_BED = '/home/qcb-panasas/skchoudh/genomes/mm10/annotation/gencode.vM11.gffutils.start_codon.bed'

## Path to bed file with stop codon coordinates
STOP_CODON_BED = '/home/qcb-panasas/skchoudh/genomes/mm10/annotation/gencode.vM11.gffutils.stop_codon.bed'

## Path to bed file containing CDS coordinates
CDS_BED = '/home/qcb-panasas/skchoudh/genomes/mm10/annotation/gencode.vM11.gffutils.cds.bed'

# We don't have these so just use CDs bed to get the pipeline running
UTR5_BED = '/home/qcb-panasas/skchoudh/genomes/mm10/annotation/gencode.vM11.gffutils.UTR5.bed'

UTR3_BED = '/home/qcb-panasas/skchoudh/genomes/mm10/annotation/gencode.vM11.gffutils.UTR3.bed'

INTRON_BED = '/home/qcb-panasas/skchoudh/genomes/mm10/annotation/gencode.vM11.gffutils.intron.bed'

ORIENTATIONS = ['5prime', '3prime']

STRANDS = ['pos', 'neg', 'combined']

FRAGMENT_LENGTHS = range(20, 39)
