# AB_dork

Python script that automates silly searches on different search engines:
- Google
- Bing
- DuckDuckGo
- Yahoo (not implemented)

The script runs on the command line.

## Arguments

There are different arguments, first we have the search engine, then the idiot operators:
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

It is possible not to use the operators and to perform a simple search with the ```-c ``` argument.


## Use

```py
./dork --bing -c "element"
./dork --google --file-type 'pdf' --in-all-text "dorking"
./dork --duckduckgo --site 'linkedin.com' --in-all-text "dorking"
```