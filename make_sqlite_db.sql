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
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/1997-QTR1.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/1997-QTR2.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/1997-QTR3.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/1997-QTR4.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/1998-QTR1.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/1998-QTR2.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/1998-QTR3.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/1998-QTR4.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/1999-QTR1.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/1999-QTR2.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/1999-QTR3.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/1999-QTR4.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2000-QTR1.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2000-QTR2.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2000-QTR3.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2000-QTR4.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2001-QTR1.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2001-QTR2.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2001-QTR3.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2001-QTR4.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2002-QTR1.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2002-QTR2.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2002-QTR3.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2002-QTR4.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2003-QTR1.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2003-QTR2.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2003-QTR3.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2003-QTR4.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2004-QTR1.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2004-QTR2.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2004-QTR3.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2004-QTR4.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2005-QTR1.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2005-QTR2.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2005-QTR3.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2005-QTR4.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2006-QTR1.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2006-QTR2.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2006-QTR3.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2006-QTR4.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2007-QTR1.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2007-QTR2.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2007-QTR3.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2007-QTR4.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2008-QTR1.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2008-QTR2.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2008-QTR3.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2008-QTR4.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2009-QTR1.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2009-QTR2.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2009-QTR3.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2009-QTR4.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2010-QTR1.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2010-QTR2.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2010-QTR3.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2010-QTR4.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2011-QTR1.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2011-QTR2.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2011-QTR3.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2011-QTR4.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2012-QTR1.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2012-QTR2.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2012-QTR3.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2012-QTR4.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2013-QTR1.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2013-QTR2.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2013-QTR3.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2013-QTR4.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2014-QTR1.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2014-QTR2.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2014-QTR3.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2014-QTR4.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2015-QTR1.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2015-QTR2.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2015-QTR3.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2015-QTR4.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2016-QTR1.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2016-QTR2.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2016-QTR3.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2016-QTR4.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2017-QTR1.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2017-QTR2.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2017-QTR3.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2017-QTR4.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2018-QTR1.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2018-QTR2.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2018-QTR3.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2018-QTR4.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2019-QTR1.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2019-QTR2.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2019-QTR3.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2019-QTR4.tsv" filing
.import "/Users/david/Dropbox/Python/Input/Edgar\ Index\ Files/2020-QTR1.tsv" filing

