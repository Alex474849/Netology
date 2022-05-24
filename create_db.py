create table artist (id serial primary key, alias varchar(50))
select * from artist


create table album (id integer primary key, artist_id integer references artist(id), name_album varchar(50) not null, year integer)
select * from album


create table track (id integer primary key, albums_id integer references album(id), track_name varchar(50) not null, year_track integer)
select * from track