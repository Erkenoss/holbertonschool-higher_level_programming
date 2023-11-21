-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
SELECT tv_genres.name AS name
FROM tv_show
INNER JOIN tv_shows ON tv_show_genres.show.id = tv_show.id
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
WHERE tv_show.title = 'Dexter'
ORDER BY tv_genres.name;