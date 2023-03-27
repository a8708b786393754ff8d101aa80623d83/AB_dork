# AB_dork

Python script that automates dork searches on different search engines: 
 - google 
 - bing 
 - duckduckgo

The script runs on the command line.

## Arguments

There are different arguments, first we have the search engine, then the dork operators: 
- filetype
- intext
- inalltext
- map
- film
- inanchor
- blog-url
- loc 
- site 
- extension

It is possible not to use the operators and perform a simple search with the argument ```-c ```. 


## Use

```py
./dork --bing -c "element"
./dork --google --file-type 'pdf' --in-all-text "dorking"
./dork --duckduckgo --site 'linkedin.com' --in-all-text "dorking"
```