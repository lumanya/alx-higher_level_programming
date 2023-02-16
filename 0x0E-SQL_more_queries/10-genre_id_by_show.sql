-- script that lists all shows contained in hbtn_0d_tvshows that have at least
-- one genre linked.
-- record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and
-- tv_show_genres.genre_id
-- The database name will be passed as an argument of the mysql command

SELECT s.title, s1.genre_id
	   FROM tv_shows AS s, tv_show_genres AS s1
WHERE s.id=s1.show_id AND s1.genre_id IS NOT NULL
	  ORDER BY s.title, s1.genre_id ASC;
