--  uses the hbtn_0d_tvshows database to lists all genres 
ON tv_show_genres.genre_id = tv_genres.id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id WHERE tv_shows.title = 'Dexter'
ORDER by tv_genres.name;
