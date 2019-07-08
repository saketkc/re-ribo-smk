from collections import defaultdict
from collections import OrderedDict
import os
from tqdm import tqdm
import glob
import pandas as pd
from riboraptor.utils import mkdir_p
from riboraptor.helpers import path_leaf

def summarize_ribotrocer_orf_project(rootdir):
    srp = path_leaf(rootdir)
    srp = path_leaf(rootdir)
    samples = glob.glob("{}/ribotricer_results/*_translating_ORFs.tsv".format(rootdir))
    summarized_orf_data = []
    summarized_phase_scores_df = pd.DataFrame()
    for sample_index, sample in enumerate(samples):
      srx = path_leaf(sample).replace("_translating_ORFs.tsv", "")
      ribotricer_df = pd.read_csv(
          sample,
          sep="\t",
          usecols=[
            "ORF_ID",
            "ORF_type",
            "status",
            "phase_score",
            "start_codon",
            "phase_score",
            ],
          )
      ribotricer_df = ribotricer_df.loc[ribotricer_df.start_codon == "ATG"]
      if sample_index == 0:
          summarized_phase_scores_df = ribotricer_df[
              ["ORF_ID", "phase_score"]
          ]  # .set_index('ORF_ID')
          summarized_phase_scores_df.columns = ["ORF_ID", srx]
      else:
          phase_score_df = ribotricer_df[["phase_score"]].rename(
              columns={"phase_score": srx}
          )
          summarized_phase_scores_df = pd.concat(
              [summarized_phase_scores_df, phase_score_df], axis=1
          )
      ribotricer_df_grouped = ribotricer_df.groupby(["ORF_type", "status"])
      for group, df in ribotricer_df_grouped:
        summarized_orf_data.append((srx, group[0], group[1], df.shape[0]))

    summarized_orf_data = pd.DataFrame(
        summarized_orf_data,
        columns=["experiment_accession", "ORF_type", "status", "count"],
    )
    return summarized_orf_data, summarized_phase_scores_df


if __name__ == "__main__":

    ROOT_DIRS = ["/staging/as/skchoudh/re-ribo-analysis"]

    __ASSEMBLIES__ = [os.listdir(dirname) for dirname in ROOT_DIRS]
    __ASSEMBLIES__ = list(
        sorted(set([item for sublist in __ASSEMBLIES__ for item in sublist]))
    )
    __ASSEMBLY_WISE_SRP__ = defaultdict(list)
    __SRP_TO_ROOT_DIR_MAP__ = defaultdict(dict)

    for root_dir in ROOT_DIRS:
        for assembly_build in os.listdir(root_dir):
            for srp_dir in filter(
                os.path.isdir, glob.glob(os.path.join(root_dir, assembly_build, "*"))
            ):
                srp = os.path.basename(srp_dir)
                __ASSEMBLY_WISE_SRP__[assembly_build].append(srp)
                __SRP_TO_ROOT_DIR_MAP__[srp][assembly_build] = os.path.join(
                    root_dir, assembly_build, srp
                )

    SUMMARY_ROOT_DIR = "/staging/as/skchoudh/re-ribo-analysis-summary-tables/"
    for species, sample_list in __ASSEMBLY_WISE_SRP__.items():
        mkdir_p(
            "/staging/as/skchoudh/re-ribo-analysis-summary-tables/{}".format(species)
        )
        for srp in tqdm(sample_list):
            basedir = os.path.dirname(
                os.path.dirname(__SRP_TO_ROOT_DIR_MAP__[srp][species])
            )
            project_filepath = "{}/{}/{}".format(basedir, species, srp)
            print(project_filepath)
            summarized_orf_filepath = "{}/{}/{}_summarized_orfs.tsv".format(
                SUMMARY_ROOT_DIR, species, srp
            )
            summarized_phase_score_filepath = "{}/{}/{}_summarized_phase_scores.tsv".format(
                SUMMARY_ROOT_DIR, species, srp
            )
            summarized_orf_data, summarized_phase_scores_df = summarize_ribotrocer_orf_project(
                project_filepath
            )
            if summarized_orf_data.shape[0]:
              summarized_orf_data.to_csv(
                  summarized_orf_filepath, index=False, header=True, sep="\t"
                  )
              summarized_phase_scores_df.to_csv(
                  summarized_phase_scores_df, index=False, header=True, sep="\t"
                  )
