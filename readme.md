quick and dirty proof of concept for extracting citation data from downloaded hein files

basically just takes the first page of the pdf and extracts bits of citation data from that big list of cites that hein offers, based on what format is most convenient for a given piece of data

currently just extracts list of authors, pages, and publication date.  

TODO: extract the rest of the main citation data (journal name, article title, volume, issue) and dump into some convenient zotero readable format (ris, bibtex, etc.)
secondary TODO: put in a decent cli interface to just loop over a folder of PDFs, pick out the hein ones, and do it
tertiary TODO: hook into zotero API to directly add to library
quarternary TODO: rewrite in javascript (I think that's the language they're in?) and offer as PR to their automated article parser, which currently fails at handling hein files most of the time


