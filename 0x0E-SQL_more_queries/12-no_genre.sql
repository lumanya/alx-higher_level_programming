-- script that lists all shows contained in hbtn_0d_tvshows without a
-- genre linked.
-- record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and
-- tv_show_genres.genre_id

SELECT s.title, s1.genre_id
	 FROM tv_shows AS s
LEFT JOIN tv_show_genres AS s1
	 ON s.id = s1.show_id
WHERE s1.genre_id IS NULL
	  ORDER BY s.title, s1.genre_id ASC;
