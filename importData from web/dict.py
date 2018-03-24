dic={'Actors': 'Jesse Eisenberg, Rooney Mara, Bryan Barter, Dustin Fitzsimons',
 'Awards': 'Won 3 Oscars. Another 165 wins & 168 nominations.',
 'BoxOffice': '$96,400,000',
 'Country': 'USA',
 'DVD': '11 Jan 2011',
 'Director': 'David Fincher',
 'Genre': 'Biography, Drama',
 'Language': 'English, French',
 'Metascore': '95',
 'Plot': 'Harvard student Mark Zuckerberg creates the social networking site that would become known as Facebook, but is later sued by two brothers who claimed he stole their idea, and the co-founder who was later squeezed out of the business.',
 'Poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BMTM2ODk0NDAwMF5BMl5BanBnXkFtZTcwNTM1MDc2Mw@@._V1_SX300.jpg',
 'Production': 'Columbia Pictures',
 'Rated': 'PG-13',
 'Ratings': [{'Source': 'Internet Movie Database', 'Value': '7.7/10'},
  {'Source': 'Rotten Tomatoes', 'Value': '96%'},
  {'Source': 'Metacritic', 'Value': '95/100'}],
 'Released': '01 Oct 2010',
 'Response': 'True',
 'Runtime': '120 min',
 'Title': 'The Social Network',
 'Type': 'movie',
 'Website': 'http://www.thesocialnetwork-movie.com/',
 'Writer': 'Aaron Sorkin (screenplay), Ben Mezrich (book)',
 'Year': '2010',
 'imdbID': 'tt1285016',
 'imdbRating': '7.7',
 'imdbVotes': '534,436'}
import json
with open('json_3.json','w') as json_file:
    json.dump(dic,json_file)