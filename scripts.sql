CREATE TABLE public.client_projects
(
    id_client_projects integer NOT NULL DEFAULT 1,
    name text NOT NULL,
    is_active boolean DEFAULT TRUE,
    created_at timestamp without time zone DEFAULT now(),
    updated_at timestamp without time zone DEFAULT now(),
    CONSTRAINT client_projects_pkey PRIMARY KEY (id_client_projects)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.client_projects
    OWNER to postgres;

CREATE SEQUENCE public.client_projects_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.client_projects_id_seq
    OWNED BY public.client_projects.id_client_projects;

ALTER SEQUENCE public.client_projects_id_seq
    OWNER TO postgres;



ALTER TABLE IF EXISTS public.client_projects
    ALTER COLUMN id_client_projects SET DEFAULT nextval('client_projects_id_seq'::regclass);



--------------------------------------------------------------------------------------------------

CREATE TABLE public.reasons_mobilization
(
    id_reason integer NOT NULL DEFAULT 1,
    name text NOT NULL,
    is_active boolean DEFAULT TRUE,
    created_at timestamp without time zone DEFAULT now(),
    updated_at timestamp without time zone DEFAULT now(),
    CONSTRAINT reasons_mobilization_pkey PRIMARY KEY (id_reason)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.reasons_mobilization
    OWNER to postgres;



CREATE SEQUENCE public.reasons_mobilization_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.reasons_mobilization_id_seq
    OWNED BY public.reasons_mobilization.id_reason;

ALTER SEQUENCE public.reasons_mobilization_id_seq
    OWNER TO postgres;



ALTER TABLE IF EXISTS public.reasons_mobilization
    ALTER COLUMN id_reason SET DEFAULT nextval('reasons_mobilization_id_seq'::regclass);


------------------------------------------------------------------------------------------------


CREATE TABLE public.vehicle_license
(
    id_license integer NOT NULL DEFAULT 1,
    name text NOT NULL,
    is_active boolean DEFAULT TRUE,
    created_at timestamp without time zone DEFAULT now(),
    updated_at timestamp without time zone DEFAULT now(),
    CONSTRAINT vehicle_license_pkey PRIMARY KEY (id_license)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.vehicle_license
    OWNER to postgres;



CREATE SEQUENCE public.vehicle_license_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.vehicle_license_id_seq
    OWNED BY public.vehicle_license.id_license;

ALTER SEQUENCE public.vehicle_license_id_seq
    OWNER TO postgres;



ALTER TABLE IF EXISTS public.vehicle_license
    ALTER COLUMN id_license SET DEFAULT nextval('vehicle_license_id_seq'::regclass);


------------------------------------------------------------------------------------------------


CREATE TABLE public.level_gasoline
(
    id_level integer NOT NULL DEFAULT 1,
    name text NOT NULL,
    is_active boolean DEFAULT TRUE,
    created_at timestamp without time zone DEFAULT now(),
    updated_at timestamp without time zone DEFAULT now(),
    CONSTRAINT level_gasoline_pkey PRIMARY KEY (id_level)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.level_gasoline
    OWNER to postgres;



CREATE SEQUENCE public.level_gasoline_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.level_gasoline_id_seq
    OWNED BY public.level_gasoline.id_level;

ALTER SEQUENCE public.level_gasoline_id_seq
    OWNER TO postgres;



ALTER TABLE IF EXISTS public.level_gasoline
    ALTER COLUMN id_level SET DEFAULT nextval('level_gasoline_id_seq'::regclass);



------------------------------------------------------------------------------------------------


CREATE TABLE public.vehicle_driver
(
    id_driver integer NOT NULL DEFAULT 1,
    name text NOT NULL,
    is_active boolean DEFAULT TRUE,
    created_at timestamp without time zone DEFAULT now(),
    updated_at timestamp without time zone DEFAULT now(),
    CONSTRAINT vehicle_driver_pkey PRIMARY KEY (id_driver)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.vehicle_driver
    OWNER to postgres;



CREATE SEQUENCE public.vehicle_driver_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.vehicle_driver_id_seq
    OWNED BY public.vehicle_driver.id_driver;

ALTER SEQUENCE public.vehicle_driver_id_seq
    OWNER TO postgres;



ALTER TABLE IF EXISTS public.vehicle_driver
    ALTER COLUMN id_driver SET DEFAULT nextval('vehicle_driver_id_seq'::regclass);


------------------------------------------------------------------------------------------------


CREATE TABLE public.vehicle_copilot
(
    id_copilot integer NOT NULL DEFAULT 1,
    name text NOT NULL,
    is_active boolean DEFAULT TRUE,
    created_at timestamp without time zone DEFAULT now(),
    updated_at timestamp without time zone DEFAULT now(),
    CONSTRAINT vehicle_copilot_pkey PRIMARY KEY (id_copilot)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.vehicle_copilot
    OWNER to postgres;



CREATE SEQUENCE public.vehicle_copilot_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.vehicle_copilot_id_seq
    OWNED BY public.vehicle_copilot.id_copilot;

ALTER SEQUENCE public.vehicle_copilot_id_seq
    OWNER TO postgres;



ALTER TABLE IF EXISTS public.vehicle_copilot
    ALTER COLUMN id_copilot SET DEFAULT nextval('vehicle_copilot_id_seq'::regclass);



-----------------------------------------------------------------------------------------------------------------------

CREATE TABLE public.movilization_control
(
    id_movilization integer NOT NULL DEFAULT 1,
    exit_date time without time zone,
    arrival_date time without time zone DEFAULT now(),
    license text,
    initial_mileage text,
    final_mileage text,
    exit_gasoline text,
    arrival_gasoline text,
    destiny text,
    exit_point text,
    driver_id integer,
    observations text,
    created_at time without time zone DEFAULT now(),
    updated_at time without time zone DEFAULT now(),
    created_by text,
    updated_by text,
    CONSTRAINT movilization_control_pkey PRIMARY KEY (id_movilization),
    CONSTRAINT movilization_control_driver_id_fkey FOREIGN KEY (driver_id)
        REFERENCES public.vehicle_driver (id_driver) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.movilization_control
    OWNER to postgres;


CREATE SEQUENCE public.movilization_control_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE public.movilization_control_id_seq
    OWNED BY public.movilization_control.id_movilization;

ALTER SEQUENCE public.movilization_control_id_seq
    OWNER TO postgres;



ALTER TABLE IF EXISTS public.movilization_control
    ALTER COLUMN id_movilization SET DEFAULT nextval('movilization_control_id_seq'::regclass);
