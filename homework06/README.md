##HOMEWORK 06

DATA and Overview: 
Data link: https://storage.googleapis.com/public-download-files/hgnc/tsv/tsv/hgnc_complete_set.txt

How it was transferred into my code: wget https://storage.googleapis.com/public-download-files/hgnc/tsv/tsv/hgnc_complete_set.txt

The HGNC archive is the complete HGNC dataset file for each month and quarter. File is monthly and is produced at the 
start of every month. 


Routes + Outputs:

/data -->  'POST' route --> This route is meant to put the hgnc data into the Redis container. 
/data -->  'GET'  route --> This route is meant to output the data which have been put into Redis
/data -->  'DELETE' route --> This route is meant to delete the data which has already been put
into the redis. 

/genes --> route --->  Uses the 'GET' method to return json-formatted list of all hgnc_ids
/genes --> route ---> Uses the 'GET' method to return all data associated with that specific hgnc_id 
which has been used. 


Query commands + some expected outputs: 

1. for the /data routes: 

a. curl -X POST https://localhost:5000/data -->

output: "HGNC data loaded into Redis")

 
b.curl https://localhost:5000/data
output: {
    "hgnc_id": "HGNC:5",
    "symbol": "A1BG",
    "name": "alpha-1-B glycoprotein",
    "locus_group": "protein-coding gene",
    "locus_type": "gene with protein product",
    "status": "Approved",
    "location": "19q13.43",
    "location_sortable": "19q13.43",
    "entrez_id": "1",
    "ensembl_gene_id": "ENSG00000121410",
    "vega_id": "OTTHUMG00000183507",
    "ucsc_id": "uc002qsd.5",
    "refseq_accession": "NM_130786",
    "ccds_id": "CCDS12976",
    "uniprot_ids": "P04217",
    "pubmed_id": "2591067",
    "mgd_id": "MGI:2152878",
    "rgd_id": "RGD:69417",
    "omim_id": "138670",
    "agr": "HGNC:5",
    "mane_select": "ENST00000263100.8|NM_130786.4"
  }

and keeps going

c. curl -X DELETE https://localhost:5000/data

output: "ALL HGNC data deleted from Redis"


2. for the /genes routes: 

a. curl http://localhost:5000/genes

output will be all the HGNC numbers and their count of how many total are there

output: 

[
        "HGNC: 5",
        "HGNC: 37133", .....]
 


3. for the /genes/<hgnc_id>

a. curl http://localhost:5000/genes/HGNC:5

output: {
  "hgnc_id": "HGNC:5",
  "symbol": "A1BG",
  "name": "alpha-1-B glycoprotein",
  "locus_group": "protein-coding gene",
  "locus_type": "gene with protein product",
  "status": "Approved",
  "location": "19q13.43",
  "location_sortable": "19q13.43",
  "entrez_id": "1",
  "ensembl_gene_id": "ENSG00000121410",
  "vega_id": "OTTHUMG00000183507",
  "ucsc_id": "uc002qsd.5",
  "refseq_accession": "NM_130786",
  "ccds_id": "CCDS12976",
  "uniprot_ids": "P04217",
  "pubmed_id": "2591067",
  "mgd_id": "MGI:2152878",
  "rgd_id": "RGD:69417",
  "omim_id": "138670",
  "agr": "HGNC:5",
  "mane_select": "ENST00000263100.8|NM_130786.4"
}






 


