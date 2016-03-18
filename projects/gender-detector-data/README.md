#Introduction
This dataset contains information on all 540 members of the United States
Congress in 2016. I found, that Congress is only 21.46% female, 29% of
which are republican and 71% democrat. The males in Congress are 63%
republican and 35% democrat (1% independent).


#Methodology and Caveats
The dataset comes from the [Sunlight Foundation website](http://unitedstates.sunlightfoundation.com/legislators/legislators.csv), an organization
which aims to make government and politics more transparent. There are
roughly 1,000 entries in the original data set, which will be trimmed
down to only include the 540 members of the current Congress.

I used the gender detector I created in the gender detector assignment to
decide whether a name was male or female. This gender detector takes baby
name data from the Social Security Administration from 1950 to 2014, and
decides whether a name is male or female based on total counts. Since
'first name' was a field in the dataset, it was not hard to extract the
first name. However, I ran into some problems with names that had accents
and names that were simply abbreviations of their first name (i.e. J. for
John). I wasn't able to resolve these, because this would require manual
entry of name data.


#Past Research and Articles
There have been countless studies and articles written about gender
inequality in leadership positions across the United States, in terms of 
the gender breakdown of CEOs, politicians, and especially in the bay area,
tech positions.

[This article](http://www.huffingtonpost.com/lili-gil/women-in-congress_b_1374030.html) from the Huffington Post shows that not only is there a very
prominent gender disparity among those that are elected to Congress, but
there is also significant disparity in female candidacy, meaning that
qualified women are often not running for positions in Congress. 

[This article](http://money.cnn.com/2013/10/24/news/economy/gender-equality/) from CNN highlights another interesting fact about gender
equality in the United States Congress: that we are even worse off than most
countries around the world. This is fairly surprising coming from a highly
developed country with a relatively strong following of the feminist movement.

#How to Use it
From the gender-detector-data folder, simply run the scripts in this order:

1. fetch_gender_data.py - this script retrieves the gender data from the
   Social Security Administration.
2. wrangle_gender_data.py - this script compiles all of the babynames from
   every 5 years from 1990 to 2014 inclusive, classifies them by gender,
   and provides a ratio estimate of the likelihood a certain name is that
   gender.
3. fetch_data.py - this script retrieves the raw Congress data from the
   Sunlight Foundation website.
4. wrangle_data.py - this script shortens the list to only include active
   members of the Congress, and only inclues information about the member
   of Congress' name, age, and party.
5. classify.py - this script takes the wrangled data and adds gender
   information, as far as the best guess of the gender detector goes, to
   create a new classified data file.
6. analyze.py - this script reads the classified data file and comes up
   with the conclusions that are printed out on the screen.



#Analysis
The conclusion that I draw from this dataset, unshockingly, provides
evidence for what all of the research and articles suggest: that for the
most part, Congress really is made up of old, republican males.

According to my analysis, Congress is only 21% female. Though this was not
an entirely surprising outcome, I was surprised by the gender breakdown of
each party. 71% of females are democrats versus 29% republican, whereas
only 36% of males are democrat versus 63% republican. While it is also not
very surprising that the men were typically republicans, what surprised me
was how drastic the differences were between men and women as far as party
goes.

I was also rather surprised that the females tended to be older than males.
However, while females averaged roughly 62 years old and males roughly 59
years old, the difference of 3 years is not extremely significant.