import os

version = 'v12'
golden_json_path = "/storage/af/user/christiw/login-1/christiw/LLP/Run3/CMSSW_9_4_4/src/RazorCommon/Tools/data/Run3/"
samples = {
        #'2022':"Muon_Run2022G_PromptReco-v1",
        '2023':"Muon1_Run2023D_PromptReco-v2",
}
json = {
        '2022':'/uscms/home/amalbert/nobackup/CMSSW_14_1_0_pre4/src/RazorCommon/Tools/data/Run3/Cert_Collisions2022_355100_362760_Golden.json',
        '2023':'/uscms/home/amalbert/nobackup/CMSSW_14_1_0_pre4/src/RazorCommon/Tools/data/Run3/Cert_Collisions2023_366442_370790_Golden.json'
}
for year, sample in samples.items():
    directory="root://cmseos.fnal.gov//store/group/lpclonglived/amalbert/Data_MC_Comp_TnP/results_from_cache_noSkim/Data_noiseFilters_fixed/2023_Merged/"
    print(sample)
    cert = json[year]

    input_file = sample + '.root'
    output_file = sample + '_goodLumi.root'
    os.system("sed -i \"/JSONfile =/c\JSONfile = \'{}\'\" ../python/loadJson.py".format(cert))
    os.system("FWLiteGoodLumi ../python/loadJson.py {} {}".format(directory + input_file, output_file))
    os.system("xrdcp {} {}/{}".format(output_file, directory, output_file))
    if os.path.isfile(directory + output_file):
            print("SUCCESS") 
            os.system("rm {}".format(output_file))
    else: print("SOMETHING WENT WRONG")
    os.system("rm {}".format(output_file))
