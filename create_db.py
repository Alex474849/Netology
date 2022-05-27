create table artist (id serial primary key, alias varchar(50))
select * from artist

create table relation1 (id_artist integer references artist(id), id_album integer references album(id),
						constraint pk primary key (id_artist, id_album))

create table album (id integer primary key, artist_id integer, name_album varchar(50) not null, year integer)
select * from album


create table track (id integer primary key, albums_id integer references album(id), track_name varchar(50) not null, year_track integer)
select * from track


alter table track add column duration integer not null

create table ralation2 (id integer primary key, id_track integer references track(id), id_collection integer references collection(id))

create table collection (id integer primary key, 
		name varchar(40) not null, 
		year varchar(40) not null
		) 
select * from collection