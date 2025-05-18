CREATE TABLE public.keyboards (
	id serial primary key,
	title text,
    manufacturer text,
    price real,
    description text,
    characteristics JSON,
    image_name text,
    form_factor text
);


CREATE TABLE public.switches (
	id serial primary key,
    short_title text,
	title text,
    manufacturer text,
    price real,
    description text,
    characteristics JSON,
    image_name text,
    switch_type text,
    actuation_force text
);

CREATE TABLE public.keycaps (
	id serial primary key,
	title text,
    manufacturer text,
    price real,
    description text,
    characteristics JSON,
    image_name text,
    material text
);

--
---- 1. Таблица производителей
--CREATE TABLE public.manufacturers (
--    id serial primary key,
--    name varchar(100) unique not null -- Производитель должен быть уникальным
--);
--
---- 2. Таблица категорий товаров
--CREATE TABLE public.product_categories (
--    id serial primary key,
--    name varchar(50) unique not null -- 'Keyboard', 'Switch', 'Keycap'
--);
--
---- Вставим базовые категории
--INSERT INTO public.product_categories (name) VALUES ('Keyboard'), ('Switch'), ('Keycap');
--
---- 3. Общая таблица товаров
--CREATE TABLE public.products (
--    id serial primary key,
--    category_id int not null references public.product_categories(id),
--    name varchar(100) not null,
--    manufacturer_id int references public.manufacturers(id), -- Ссылка на производителя
--    price real,
--    description text,
--    characteristics JSON, -- Оставляем JSON для прочих, неструктурированных характеристик
--    image_name varchar(50)
--    -- CONSTRAINT uq_product_name_manufacturer UNIQUE (name, manufacturer_id) -- Опционально: уникальность по названию и производителю
--);
--
---- 4. Таблицы-справочники для специфичных атрибутов
--
--CREATE TABLE public.keyboard_form_factors (
--    id serial primary key,
--    name varchar(50) unique not null -- 'Full-size', 'TKL', '75%', '60%', etc.
--);
--
--CREATE TABLE public.switch_types (
--    id serial primary key,
--    name varchar(100) unique not null -- 'Linear', 'Tactile', 'Clicky'
--);
--
--CREATE TABLE public.keycap_materials (
--    id serial primary key,
--    name varchar(50) unique not null -- 'ABS', 'PBT', 'POM'
--);
--
--
---- 5. Специфичные таблицы для каждого типа товара
--
--CREATE TABLE public.keyboards_specifics (
--    product_id int primary key references public.products(id) on delete cascade, -- Связь 1-к-1 с products, удаление каскадом
--    form_factor_id int references public.keyboard_form_factors(id)
--);
--
--CREATE TABLE public.switches_specifics (
--    product_id int primary key references public.products(id) on delete cascade,
--    switch_type_id int references public.switch_types(id),
--    actuation_force varchar(50) -- Например, '45g', '60cN'. Можно также вынести в справочник, если значения стандартизированы.
--);
--
--CREATE TABLE public.keycaps_specifics (
--    product_id int primary key references public.products(id) on delete cascade,
--    material_id int references public.keycap_materials(id)
--);
--
---- Индексы для улучшения производительности запросов
--CREATE INDEX idx_products_category_id ON public.products(category_id);
--CREATE INDEX idx_products_manufacturer_id ON public.products(manufacturer_id);
--CREATE INDEX idx_products_name ON public.products(name); -- Если часто ищете по имени
--
--CREATE INDEX idx_keyboards_form_factor_id ON public.keyboards_specifics(form_factor_id);
--CREATE INDEX idx_switches_switch_type_id ON public.switches_specifics(switch_type_id);
--CREATE INDEX idx_keycaps_material_id ON public.keycaps_specifics(material_id);
