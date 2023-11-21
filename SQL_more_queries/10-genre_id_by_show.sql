-- script that llist all show coontained in hbtn_0d_tvshows with at least one genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_show_genres.genre_id