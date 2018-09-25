import os
from snakemake.shell import shell

shell(r'''cat {snakemake.input.dynamic_input} > {snakemake.output}''')
