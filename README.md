# exercise-recordly

Overview:
The overall instructions to do an MVP turned into a little bit more; I built a basic functional product that performs login, listing of artists/albums/songs, can filter by favorite, and does ajax searching. I incorporated traditional CGI for login and ajax for all the rest of the operations.

I used Bootstrap to make the design minimally clean, Angular to drive the client operations, and a quasi-REST interface to talk to the Django python server, which is running off a SQLite database for the storage of all the information.

Comments and Future Work:

QA:
- unit testing on both angular code and server python code

Security:
- authenication and handling of situations like accessing the Recordly page while logged out

Performance:
- the search functionality is very basic. I implemented a basic throttling function so that the code would query results as the user is typing, but would throttle the querying so that it didn't pound the server with search queries. On the server side, basic search of songs was implemented. We could aggregate the results from all the tables and combine them for a global search feature, but really the right thing to do is integrate a search technology like Lucene or Sphinx to index the database results and have search be both performant and fast.
- the basic retrieval behavior of the page is not performant. We go out and grab all the data as soon as the page loads, and in the future it would be more sensible to just grab data as the user opens the relevant tabbed section for the information s/he wants.

Polish:
- the UI is quite basic and could use a lot more love.
- for such a simple application, we might just create a more consistent SPA experience by removing the CGI and having everything be ajax, so the user feels like its an app rather than a series of webpages

Architecture:
- as far as code architecture, there's some repetition in the code that should be cleaned up.

Misc:
- the REST-ful api is not true REST. I adhered to the basics of doing GETs for simple objects, but I took some liberties with some of it, such as the filtering option 'favorites'. Future work would include cleaning this up.

Back End:
- for simplicity, all SQL tables have references to the user table so we could have album, artist, and song entries belong specifically to a user. This is a bit of redundancy and the tables could be normalized.
