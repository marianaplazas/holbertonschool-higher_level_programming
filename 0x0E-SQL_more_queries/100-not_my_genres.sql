-- uses the hbtn_0d_tvshows database to list all genres
SELECT tv_genres.name 
FROM tv_genres
WHERE tv_genres.id NOT IN (SELECT DISTINCT tv_genres.id FROM tv_show_genres
INNER JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_shows.title = 'Dexter') ORDER BY name ASC;
