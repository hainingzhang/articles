import os

BASEDIR = os.path.dirname(__file__)
ORDERER = os.path.join(BASEDIR, "../crypto-config/ordererOrganizations") # it must point to the ordererOrgnaizations dir
PEER = os.path.join(BASEDIR, "../crypto-config/peerOrganizations") # it must point to the peerOrgnaizations dir
### order of run ###

#### orderer
##### namespace(org)
###### single orderer

#### peer
##### namespace(org)
###### ca
####### single peer

def deleteOrderers(path):
	orgs = os.listdir(path)
	for org in orgs:
		orgPath = os.path.join(path, org)
		namespaceYaml = os.path.join(orgPath, org + "-namespace.yaml" ) #orgYaml namespace.yaml
		
		for orderer in os.listdir(orgPath + "/orderers"):
			ordererPath = os.path.join(orgPath + "/orderers", orderer)
			ordererYaml = os.path.join(ordererPath, orderer + ".yaml")
			checkAndDelete(ordererYaml)


		checkAndDelete(namespaceYaml)




def deletePeers(path):
	orgs = os.listdir(path)
	for org in orgs:
		orgPath = os.path.join(path, org)

		namespaceYaml = os.path.join(orgPath, org + "-namespace.yaml" ) # namespace.yaml
		caYaml = os.path.join(orgPath, org + "-ca.yaml" ) # ca.yaml
		cliYaml = os.path.join(orgPath, org + "-cli.yaml" ) # cli.yaml  

		for peer in os.listdir(orgPath + "/peers"):
			peerPath = os.path.join(orgPath + "/peers", peer)
			peerYaml = os.path.join(peerPath, peer + ".yaml")
			checkAndDelete(peerYaml)	
		
		checkAndDelete(cliYaml) 
		checkAndDelete(caYaml)
		checkAndDelete(namespaceYaml)
		

def checkAndDelete(f):
	if os.path.isfile(f):
		os.system("kubectl delete -f " + f)

if __name__ == "__main__":
	deleteOrderers(ORDERER)
	deletePeers(PEER)
