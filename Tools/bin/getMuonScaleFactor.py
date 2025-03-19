import sys
import os

import correctionlib
import awkward as ak
import numpy as np

Run2022_postEE_ID_Path = "/uscms/home/amalbert/nobackup/CMSSW_14_1_0_pre4/src/RazorCommon/Tools/data/Run3/muonefficiencies/Run3/2022_EE/2022_Z/ScaleFactors_Muon_Z_ID_ISO_2022_EE_schemaV2.json"

Run2023_bPix_ID_Path = "/uscms/home/amalbert/nobackup/CMSSW_14_1_0_pre4/src/RazorCommon/Tools/data/Run3/muonefficiencies/Run3/2023_BPix/2023_Z/ScaleFactors_Muon_Z_ID_ISO_2023_BPix_schemaV2.json"
Run2023_bPix_HLT_Path = "/uscms/home/amalbert/nobackup/CMSSW_14_1_0_pre4/src/RazorCommon/Tools/data/Run3/muonefficiencies/Run3/2023_BPix/2023_Z/HLT/json/ScaleFactors_Muon_Z_HLT_2023_BPix_abseta_pt_schemaV2.json"

Run2023_ID_Path = "/uscms/home/amalbert/nobackup/CMSSW_14_1_0_pre4/src/RazorCommon/Tools/data/Run3/muonefficiencies/Run3/2023/2023_Z/ScaleFactors_Muon_Z_ID_ISO_2023_schemaV2.json"
Run2023_HLT_Path = "/uscms/home/amalbert/nobackup/CMSSW_14_1_0_pre4/src/RazorCommon/Tools/data/Run3/muonefficiencies/Run3/2023/2023_Z/HLT/json/ScaleFactors_Muon_Z_HLT_2023_abseta_pt_schemaV2.json"

def getLooseIDEff_EE(muonPt: float, muonEta: float):
    correctionsData = correctionlib.CorrectionSet.from_file(Run2022_postEE_ID_Path)
    return correctionsData["NUM_LooseID_DEN_TrackerMuons"].evaluate(abs(muonEta), muonPt, "nominal")
   

def getLooseIDEffArr_BPix(muonPt, muonEta):
    correctionsData = correctionlib.CorrectionSet.from_file(Run2023_bPix_ID_Path)
    return correctionsData["NUM_LooseID_DEN_TrackerMuons"].evaluate(abs(muonEta), muonPt, "nominal")

def getLooseISOEffArr_BPix(muonPt, muonEta):
    correctionsData = correctionlib.CorrectionSet.from_file(Run2023_bPix_ID_Path)
    return correctionsData["NUM_LoosePFIso_DEN_LooseID"].evaluate(abs(muonEta), muonPt, "nominal")

def getTightIDEffArr_BPix(muonPt, muonEta):
    correctionsData = correctionlib.CorrectionSet.from_file(Run2023_bPix_ID_Path)
    return correctionsData["NUM_TightID_DEN_TrackerMuons"].evaluate(abs(muonEta), muonPt, "nominal")

def getTightISOEffArr_BPix(muonPt, muonEta):
    correctionsData = correctionlib.CorrectionSet.from_file(Run2023_bPix_ID_Path)
    return correctionsData["NUM_TightPFIso_DEN_TightID"].evaluate(abs(muonEta), muonPt, "nominal")

def getHLTEffArr_BPix(muonPt, muonEta):
    correctionsData = correctionlib.CorrectionSet.from_file(Run2023_bPix_HLT_Path)
    #muonPt = ak.mask(muonPt, muonPt>26)
    #if muonPt<26:
    #    return 1
    return correctionsData["NUM_IsoMu24_DEN_CutBasedIdTight_and_PFIsoTight"].evaluate(abs(muonEta), abs(muonPt), "nominal")

def getLooseIDEffArr_preBPix(muonPt, muonEta):
    correctionsData = correctionlib.CorrectionSet.from_file(Run2023_ID_Path)
    return correctionsData["NUM_LooseID_DEN_TrackerMuons"].evaluate(abs(muonEta), muonPt, "nominal")

def getLooseISOEffArr_preBPix(muonPt, muonEta):
    correctionsData = correctionlib.CorrectionSet.from_file(Run2023_ID_Path)
    return correctionsData["NUM_LoosePFIso_DEN_LooseID"].evaluate(abs(muonEta), muonPt, "nominal")

def getTightIDEffArr_preBPix(muonPt, muonEta):
    correctionsData = correctionlib.CorrectionSet.from_file(Run2023_ID_Path)
    return correctionsData["NUM_TightID_DEN_TrackerMuons"].evaluate(abs(muonEta), muonPt, "nominal")

def getTightISOEffArr_preBPix(muonPt, muonEta):
    correctionsData = correctionlib.CorrectionSet.from_file(Run2023_ID_Path)
    return correctionsData["NUM_TightPFIso_DEN_TightID"].evaluate(abs(muonEta), muonPt, "nominal")

def getHLTEffArr_preBPix(muonPt, muonEta):
    correctionsData = correctionlib.CorrectionSet.from_file(Run2023_HLT_Path)
    #muonPt = ak.mask(muonPt, muonPt>26)
    #if muonPt<26:
    #    return 1
    return correctionsData["NUM_IsoMu24_DEN_CutBasedIdTight_and_PFIsoTight"].evaluate(abs(muonEta), abs(muonPt), "nominal")

if __name__ == '__main__':
    import argparse

    parser= argparse.ArgumentParser()
    parser.add_argument("--SF_type", type=str, default=None)
    parser.add_argument("--pTs", type=float, default=None)
    parser.add_argument("--etas", type=float, default=None)
    parser.add_argument("--correction_set", type=str, default=None)

    args = parser.parse_args()
    #if args.SF_type == "Muon_LooseID":
    #    print(getLooseIDEff(args.pTs, args.etas, args.correction_set))
