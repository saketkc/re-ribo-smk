from snakemake.shell import shell
from riboraptor.kmer import fastq_kmer_histogram
import operator

def get_top_kmer(kmer_series_dict):
    """Return a kmer if it's percentage exceed 30%"""
    # Start from the longest kmer and stop
    # at where this criterion is met
    for kmer_length, kmer_series in sorted(kmer_series_dict.items(), key=operator.itemgetter(0), reverse=True):
        over_represented = kmer_series[kmer_series>=30]
        if len(over_represented)>=1:
            return over_represented.index.tolist()[0]
    return None


params = snakemake.params
pass1_dir = snakemake.params.pass1_dir
pass2_dir = snakemake.params.pass2_dir
output_1 = snakemake.output.pass1_fq
output_2 = snakemake.output.pass2_fq
output_2_report = output_2 + '_trimming_report.txt'

# Do first pass
shell(r'''trim_galore -o {pass1_dir} --length {params.min_length} \
      -q {params.phred_cutoff} {snakemake.input.R1}''')


# Are there any  over-represented sequences?
# If yes, do a second pass
histogram = fastq_kmer_histogram(output_1)
adapter = get_top_kmer(histogram)
if adapter is None:
    shell(r'''cp -r {output_1} {output_2}''')
    shell(r'''echo "No adapter found in second pass" > {output_2_report}''')
else:
    # Else just copy
    shell(r'''trim_galore -o {pass2_dir} --length {params.min_length} \
        -a {adapter} \
        -q {params.phred_cutoff} {output_1}''')
