RAWDATA_DIR ='/home/cmb-06/as/skchoudh/rna/Feb_02_2019_Kadosh_Film_Planktonic/mapped_mRNA_only_collapsed/bams'
OUT_DIR ='/staging/as/skchoudh/rna/Feb_02_2019_Kadosh_Film_Planktonic_riboraptor_longest_feb2019'
GENOME_FASTA = '/home/cmb-06/as/skchoudh/genomes/C_albicans_SC5314/Assembly22/fasta/C_albicans_SC5314_version_A22-s07-m01-r27_chromosomes.fasta'
CHROM_SIZES = '/home/cmb-06/as/skchoudh/genomes/C_albicans_SC5314/Assembly22/fasta/C_albicans_SC5314_version_A22-s07-m01-r27_chromosomes.sizes'
STAR_INDEX = '/home/cmb-06/as/skchoudh/genomes/C_albicans_SC5314/Assembly22/star_mrna_index'
GTF = '/home/cmb-06/as/skchoudh/genomes/C_albicans_SC5314/Assembly22' + '/annotation/' + 'C_albicans_SC5314_version_A22-s07-m01-r27_features.gtf'
GENE_BED = '/home/cmb-06/as/skchoudh/genomes/C_albicans_SC5314/Assembly22/annotation/C_albicans_SC5314_version_A22-s07-m01-r27_features.bed12'
STAR_CODON_BED = '/home/cmb-06/as/skchoudh/genomes/C_albicans_SC5314/Assembly22/annotation/C_albicans_SC5314_version_A22-s07-m01-r50_features.encode.gffutils.start_codon.bed'
STOP_CODON_BED = '/home/cmb-06/as/skchoudh/genomes/C_albicans_SC5314/Assembly22/annotation/C_albicans_SC5314_version_A22-s07-m01-r50_features.encode.gffutils.stop_codon.bed'
CDS_BED = '/home/cmb-06/as/skchoudh/genomes/C_albicans_SC5314/Assembly22' + '/annotation/' + '/C_albicans_SC5314_version_A22-s07-m01-r27_features.gtfTogenePred.genePredToBed6'
UTR5_BED = '/home/cmb-06/as/skchoudh/github_projects/C_albicans_project/Bruno_et_al_2014_data/Bruno_et_al_UTR5.A21toA22_hapAB_merged.collapsed.named_uniquehits.bed'
UTR3_BED = '/home/cmb-06/as/skchoudh/github_projects/C_albicans_project/Bruno_et_al_2014_data/Bruno_et_al_UTR3.A21toA22_hapAB_merged.collapsed.named_uniquehits.bed'
INTRON_BED = '/home/cmb-06/as/skchoudh/github_projects/C_albicans_project/Bruno_et_al_2014_data/Bruno_et_al_UTR5.A21toA22_hapAB_merged.collapsed.named_uniquehits.bed'
ORIENTATIONS = ['5prime', '3prime']
STRANDS = ['pos', 'neg', 'combined']
FRAGMENT_LENGTHS =  range(18, 39)
