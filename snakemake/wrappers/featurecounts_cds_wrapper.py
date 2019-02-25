import os
import h5py
from snakemake.shell import shell
from collections import defaultdict
import pandas as pd
from riboraptor.infer_protocol import infer_protocol

protocols = defaultdict(list)
for bam in snakemake.input['bams']:
    protocol, forward_mapped, reverse_mapped, total = infer_protocol(
        bam, snakemake.input['bed'])
    protocols[protocol].append(bam)
outputs = []
for protocol, bams in protocols.items():
    if protocol == 'forward':
        count_strat = '-s 1'
    elif protocol == 'reverse':
        count_strat = '-s 2'
    elif protocol == 'unstranded':
        count_strat = ''
    else:
        raise ValueError('Unknown protocol: {}'.formatpro(tocol))
    bams = sorted(bams)
    output = os.path.abspath(str(snakemake.output)) + '-' + protocol
    outputs.append(output)
    shell(
        r'''featureCounts {count_strat} -a {snakemake.params.annotation} -o {output} -t CDS -g gene_id -Q 4 -T {snakemake.threads} {bams}'''
    )
df = pd.read_table(outputs[0], skiprows=[0])
if len(outputs) > 1:
    for f in outputs[1:]:
        temp_df = pd.read_table(f, skiprows=[0])
        temp_df = temp_df.drop(
            columns=['Geneid', 'Chr', 'Start', 'End', 'Strand', 'Length'])
        df = pd.concat([df, temp_df], axis=1)

df.to_csv(str(snakemake.output), sep='\t', index=False, header=True)
