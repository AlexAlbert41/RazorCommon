#!/bin/bash
sample_list=("Muon0-Run2024B-PromptReco-v1" "Muon0-Run2024C-PromptReco-v1" "Muon0-Run2024D-PromptReco-v1" "Muon0-Run2024E-PromptReco-v1" "Muon0-Run2024E-PromptReco-v2" "Muon0-Run2024F-PromptReco-v1" "Muon0-Run2024G-PromptReco-v1" "Muon0-Run2024H-PromptReco-v1" "Muon0-Run2024I-PromptReco-v1" "Muon0-Run2024I-PromptReco-v2" "Muon1-Run2024B-PromptReco-v1" "Muon1-Run2024C-PromptReco-v1" "Muon1-Run2024D-PromptReco-v1" "Muon1-Run2024E-PromptReco-v1" "Muon1-Run2024E-PromptReco-v2" "Muon1-Run2024F-PromptReco-v1" "Muon1-Run2024G-PromptReco-v1" "Muon1-Run2024H-PromptReco-v1" "Muon1-Run2024I-PromptReco-v1" "Muon1-Run2024I-PromptReco-v2")

#sample_list=("Muon1-Run2024D-PromptReco-v1")


output_directory="root://cmseos.fnal.gov//store/group/lpclonglived/amalbert/HNL_Tau_Search/2024_Data_tauh_analyzer_update_042926/"

#source /cvmfs/cms.cern.ch/el8_amd64_gcc12/lcg/root/6.30.09-12b7f37c839e665e5ed498257af80796/bin/thisroot.sh #source a random el8 version of root
for sample in ${sample_list[@]}; do
        echo $sample
        if [[ $sample == *"2022"* ]]; then
                year="2022"
        fi
        if [[ $sample == *"2023"* ]]; then
                year="2023"
        fi
        if [[ $sample == *"2024"* ]]; then
                year="2024"
        fi
        xrdcp $output_directory/$sample/normalized/$sample.root .
        python3 commands_run3_forLPCFiles.py $year $sample $output_directory/$sample/normalized
done

#re-source the el9 root version used in the rest of the repo
#source cvmfs/cms.cern.ch/el9_amd64_gcc12/lcg/root/6.30.07-024df6516c17fd2edef848a927a788f1/bin/thisroot.sh
