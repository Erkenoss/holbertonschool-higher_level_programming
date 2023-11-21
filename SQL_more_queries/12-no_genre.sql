-- script that lists all shows contained in hbtn_0d_tvshows without a genre linked
SELECT tv_shows.title,
CASE WHEN tv_show_genres.genre_id IS NULL
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;