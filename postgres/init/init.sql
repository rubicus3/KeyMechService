CREATE TABLE public.keyboards (
	id serial primary key,
    name varchar(100),
    price real,
    form_factor varchar(50),
    manufacturer varchar(50),
    description text,
    characteristics JSON,
    image_name varchar(50)
);
