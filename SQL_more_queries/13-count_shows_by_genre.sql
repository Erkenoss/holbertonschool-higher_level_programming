--  a script that lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_show_genres.genre AS genre, COUNT(tv_shows.id) AS number_of_shows
FROM tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
GROUP BY tv_show_genres.genre
WHERE COUNT(number_of_shows) > 0
ORDER BY number_of_shows DESC;