from string import Template
from pathlib import Path
import string
import config as tc
import os

BASEDIR = os.path.dirname(__file__)
ORDERER = os.path.join(BASEDIR, "../crypto-config/ordererOrganizations")
PEER = os.path.join(BASEDIR, "../crypto-config/peerOrganizations")

#generateNamespacePod generate the yaml file to create the namespace for k8s, and return a set of paths which indicate the location of org files  

def generateNamespacePod(DIR):
	orgs = []
	for org in os.listdir(DIR):
		orgDIR = os.path.join(DIR, org)
		## generate namespace first.
		tc.configORGS(org, orgDIR)
		orgs.append(orgDIR)
		#orgs.append(orgDIR + "/" + DIR.lower())
	
	#print(orgs)	
	return orgs


def generateDeploymentPod(orgs):
	for org in orgs:

		if org.find("peer") != -1: #whether it create orderer pod or peer pod 
			suffix = "/peers"
		else:
			suffix = "/orderers"

		members = os.listdir(org + suffix)
		for member in members:
			#print(member)
			memberDIR = os.path.join(org + suffix, member)
			#print(memberDIR)
			#print(os.listdir(memberDIR))
			tc.generateYaml(member,memberDIR, suffix)


#TODO kafa nodes and zookeeper nodes don't have dir to store their certificate, must use anotherway to create pod yaml.

def allInOne():
	peerOrgs = generateNamespacePod(PEER)
	generateDeploymentPod(peerOrgs)

	ordererOrgs = generateNamespacePod(ORDERER)
	generateDeploymentPod(ordererOrgs)


if __name__ == "__main__" :
	allInOne()
	
