import sys
import os


input_year=sys.argv[1]
input_sample=sys.argv[2]
directory=sys.argv[3]

version = 'v12'
golden_json_path = os.environ["CMSSW_BASE"]+"/src/RazorCommon/Tools/data/Run3/"
samples = {
        #'2022':"Muon_Run2022E_PromptReco-v1",
        #'2023':"Muon1_Run2023C_PromptReco-v2",
        input_year:input_sample,
}
json = {
        '2022':os.environ["CMSSW_BASE"]+'/src/RazorCommon/Tools/data/Run3/Cert_Collisions2022_355100_362760_Golden.json',
        '2023':os.environ["CMSSW_BASE"]+'/src/RazorCommon/Tools/data/Run3/Cert_Collisions2023_366442_370790_Golden.json',
        '2024':os.environ["CMSSW_BASE"]+'/src/RazorCommon/Tools/data/Run3/Cert_Collisions2024_378981_386951_Golden.json'
}
for year, sample in samples.items():
    #directory="root://cmseos.fnal.gov//store/group/lpclonglived/amalbert/Data_MC_Comp_TnP/results_from_cache_noSkim/Data_noClusters_fixed/2024_Merged/"
    print(sample)
    cert = json[year]

    input_file = sample + '.root'
    output_file = sample + '_goodLumi.root'
    os.system("sed -i \"/JSONfile =/c\JSONfile = \'{}\'\" ../python/loadJson.py".format(cert))
    os.system("FWLiteGoodLumi ../python/loadJson.py {} {}".format(input_file, output_file))
    os.system("xrdcp {} {}/{}".format(output_file, directory, output_file))
    #if os.path.isfile(directory + output_file):
    #        print("SUCCESS")
    #        os.system("rm {}".format(output_file))
    #else: print("SOMETHING WENT WRONG")
    os.system("rm {}".format(input_file))
    os.system("rm {}".format(output_file))
