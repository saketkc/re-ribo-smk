
RAWDATA_DIR = '/staging/as/skchoudh/re-ribo-datasets/BDGP6/SRP028243'
OUT_DIR = '/staging/as/skchoudh/re-ribo-analysis/BDGP6/SRP028243_fixed_adapters'
GENOME_FASTA = '/home/cmb-06/as/skchoudh/genomes/drosophila_melanogaster_BDGP6/fasta/Drosophila_melanogaster.BDGP6.dna.toplevel.fa'
CHROM_SIZES = '/home/cmb-06/as/skchoudh/genomes/drosophila_melanogaster_BDGP6/fasta/Drosophila_melanogaster.BDGP6.dna.toplevel.sizes'
STAR_INDEX = '/home/cmb-06/as/skchoudh/genomes/drosophila_melanogaster_BDGP6/star_annotated'
GTF = '/home/cmb-06/as/skchoudh/genomes/drosophila_melanogaster_BDGP6/annotation/Drosophila_melanogaster.BDGP6.91.gtf'
GENE_BED = '/home/cmb-06/as/skchoudh/github_projects/riboraptor/riboraptor/annotation/BDGP6/v91/gene.bed.gz'
STAR_CODON_BED = '/home/cmb-06/as/skchoudh/github_projects/riboraptor/riboraptor/annotation/BDGP6/v91/start_codon.bed.gz'
STOP_CODON_BED = '/home/cmb-06/as/skchoudh/github_projects/riboraptor/riboraptor/annotation/BDGP6/v91/stop_codon.bed.gz'
CDS_BED = '/home/cmb-06/as/skchoudh/github_projects/riboraptor/riboraptor/annotation/BDGP6/v91/cds.bed.gz'
UTR5_BED = '/home/cmb-06/as/skchoudh/github_projects/riboraptor/riboraptor/annotation/BDGP6/v91/utr5.bed.gz'
UTR3_BED = '/home/cmb-06/as/skchoudh/github_projects/riboraptor/riboraptor/annotation/BDGP6/v91/utr3.bed.gz'
INTRON_BED = '/home/cmb-06/as/skchoudh/github_projects/riboraptor/riboraptor/annotation/BDGP6/v91/intron.bed.gz'
ORIENTATIONS = ['5prime', '3prime']
STRANDS = ['pos', 'neg', 'combined']
FRAGMENT_LENGTHS =  range(18, 39)
