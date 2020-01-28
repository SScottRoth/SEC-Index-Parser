drop table filing;

create table filing (
    cik text,
    name text,
    form_type text,
    filing_date date,
    form_text_url text,
    form_html_url text
);

.mode list
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/1993-QTR1.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/1993-QTR2.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/1993-QTR3.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/1993-QTR4.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/1994-QTR1.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/1994-QTR2.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/1994-QTR3.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/1994-QTR4.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/1995-QTR1.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/1995-QTR2.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/1995-QTR3.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/1995-QTR4.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/1996-QTR1.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/1996-QTR2.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/1996-QTR3.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/1996-QTR4.tsv" filing

