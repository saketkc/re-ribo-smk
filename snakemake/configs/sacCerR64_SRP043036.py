
RAWDATA_DIR = '/staging/as/skchoudh/re-ribo-datasets/sacCerR64/SRP043036'
OUT_DIR = '/staging/as/skchoudh/re-ribo-analysis/sacCerR64/SRP043036'
GENOME_FASTA = '/home/cmb-panasas2/skchoudh/genomes/sacCerR64/fasta/Saccharomyces_cerevisiae.R64-1-1.dna.toplevel.fa'
CHROM_SIZES = '/home/cmb-panasas2/skchoudh/genomes/sacCerR64/fasta/Saccharomyces_cerevisiae.R64-1-1.dna.toplevel.sizes'
STAR_INDEX = '/home/cmb-panasas2/skchoudh/genomes/sacCerR64/star_annotated'
GTF = '/home/cmb-panasas2/skchoudh/genomes/sacCerR64/annotation/Saccharomyces_cerevisiae.R64-1-1.91.gtf'
GENE_BED = '/home/cmb-panasas2/skchoudh/github_projects/riboraptor/riboraptor/annotation/sacCerR64/v91/gene.bed.gz'
STAR_CODON_BED = '/home/cmb-panasas2/skchoudh/github_projects/riboraptor/riboraptor/annotation/sacCerR64/v91/start_codon.bed.gz'
STOP_CODON_BED = '/home/cmb-panasas2/skchoudh/github_projects/riboraptor/riboraptor/annotation/sacCerR64/v91/stop_codon.bed.gz'
CDS_BED = '/home/cmb-panasas2/skchoudh/github_projects/riboraptor/riboraptor/annotation/sacCerR64/v91/cds.bed.gz'
UTR5_BED = '/home/cmb-panasas2/skchoudh/github_projects/riboraptor/riboraptor/annotation/sacCerR64/v91/utr5.bed.gz'
UTR3_BED = '/home/cmb-panasas2/skchoudh/github_projects/riboraptor/riboraptor/annotation/sacCerR64/v91/utr3.bed.gz'
INTRON_BED = '/home/cmb-panasas2/skchoudh/github_projects/riboraptor/riboraptor/annotation/sacCerR64/v91/intron.bed.gz'
ORIENTATIONS = ['5prime', '3prime']
STRANDS = ['pos', 'neg', 'combined']
FRAGMENT_LENGTHS =  range(18, 39)
ADAPTER = 'CTGTAGGCACCATCAAT'
