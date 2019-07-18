-- lists all genres from hbtn_0d_tvshows
SELECT tv.genres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_shows
FROM tv_genres INNER JOIN tv_show_genres 
WHERE tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name ORDER BY number_shows DESC;
