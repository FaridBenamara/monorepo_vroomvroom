-- Database initialization script

BEGIN;

CREATE TABLE IF NOT EXISTS public.vehicle
(
    id serial NOT NULL,
    name character varying(120) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT vehicle_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.race
(
    id serial NOT NULL,
    vehicle_id integer NOT NULL,
    name character varying(120) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT race_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.sensor_data
(
    id serial NOT NULL,
    race_id integer NOT NULL,
    distance double precision NOT NULL,
    speed double precision NOT NULL,
    date timestamp with time zone NOT NULL DEFAULT CURRENT_TIMESTAMP,
    battery double precision NOT NULL,
    track double precision NOT NULL,
    CONSTRAINT sensor_data_pkey PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS public.stats_race
(
    id serial NOT NULL,
    race_id integer NOT NULL,
    distance double precision NOT NULL,
    speed_max double precision NOT NULL,
    speed_average double precision NOT NULL,
    battery_max integer NOT NULL,
    battery_min integer NOT NULL,
    "time" integer NOT NULL,
    date timestamp with time zone NOT NULL DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT stats_race_pkey PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS public.race
    ADD CONSTRAINT race_vehicle_id_fkey FOREIGN KEY (vehicle_id)
    REFERENCES public.vehicle (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE CASCADE;

ALTER TABLE IF EXISTS public.sensor_data
    ADD CONSTRAINT sensor_data_race_id_fkey FOREIGN KEY (race_id)
    REFERENCES public.race (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE CASCADE;

ALTER TABLE IF EXISTS public.stats_race
    ADD CONSTRAINT stats_race_race_id_fkey FOREIGN KEY (race_id)
    REFERENCES public.race (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE CASCADE;

END;
