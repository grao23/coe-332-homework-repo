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

a. curl -X POST http://localhost:5000/data -->

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

a. curl -X GET http://localhost:5000/genes

output will be all the HGNC numbers and their count of how many total are there

output(end part of it): 

[""
  "HGNC:40277",
  "HGNC:14957",
  "HGNC:36205",
  "HGNC:44924",
  "HGNC:9402",
  "HGNC:7817",
  "HGNC:29945",
  "HGNC:46207",
  "HGNC:46366",
  "HGNC:44646",
  "HGNC:54619",
  "HGNC:39047",
  "HGNC:25292",
  "HGNC:29650",
  "HGNC:55592",
  "HGNC:33932",
  "HGNC:30660",
  "HGNC:6513",
  "HGNC:43479",
  "HGNC:44050",
  "HGNC:44287",
  "HGNC:15258",
  "HGNC:35325",
  "HGNC:55660",
  "HGNC:28584",
  "HGNC:53731",
  "HGNC:49585",
  "HGNC:43757",
  "HGNC:54986",
  "HGNC:7638",
  "HGNC:42215",
  "HGNC:32095",
  "HGNC:8554",
  "HGNC:53638",
  "HGNC:19172",
  "HGNC:18951",
  "HGNC:33844",
  "HGNC:53247",
  "HGNC:19834",
  "HGNC:33895",
  "HGNC:18455",
  "HGNC:56471",
  "HGNC:4701",
  "HGNC:17278",
  "HGNC:24600",
  "HGNC:39782",
  "HGNC:37807"
]
""]


3. for the /genes/<hgnc_id>

a. curl -X GET http://localhost:5000/genes/HGNC:5

output: 


{
  "agr": "HGNC:5",
  "ccds_id": [
    "CCDS12976"
  ],
  "date_approved_reserved": "1989-06-30",
  "date_modified": "2023-01-20",
  "ensembl_gene_id": "ENSG00000121410",
  "entrez_id": "1",
  "gene_group": [
    "Immunoglobulin like domain containing"
  ],
  "gene_group_id": [
    594
  ],
  "hgnc_id": "HGNC:5",
  "location": "19q13.43",
  "location_sortable": "19q13.43",
  "locus_group": "protein-coding gene",
  "locus_type": "gene with protein product",
  "mane_select": [
    "ENST00000263100.8",
    "NM_130786.4"
  ],
  "merops": "I43.950",
  "mgd_id": [
    "MGI:2152878"
  ],
  "name": "alpha-1-B glycoprotein",
  "omim_id": [
    "138670"
  ],
  "pubmed_id": [
    2591067
  ],
  "refseq_accession": [
    "NM_130786"
  ],
  "rgd_id": [
    "RGD:69417"
  ],
  "status": "Approved",
  "symbol": "A1BG",
  "ucsc_id": "uc002qsd.5",
  "uniprot_ids": [
    "P04217"
  ],
  "uuid": "8879c319-d846-4a65-84bf-511fdcccc3bb",
  "vega_id": "OTTHUMG00000183507"
}

 


