CREATE TABLE technical.client_projects
(
    id_client_projects integer NOT NULL DEFAULT 1,
    name text NOT NULL,
    is_active boolean DEFAULT TRUE,
    created_at timestamp without time zone DEFAULT now(),
    updated_at timestamp without time zone DEFAULT now(),
    CONSTRAINT client_projects_pkey PRIMARY KEY (id_client_projects)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS technical.client_projects
    OWNER to n8n_user;

CREATE SEQUENCE technical.client_projects_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE technical.client_projects_id_seq
    OWNED BY technical.client_projects.id_client_projects;

ALTER SEQUENCE technical.client_projects_id_seq
    OWNER TO n8n_user;



ALTER TABLE IF EXISTS technical.client_projects
    ALTER COLUMN id_client_projects SET DEFAULT nextval('client_projects_id_seq'::regclass);



--------------------------------------------------------------------------------------------------

CREATE TABLE technical.reasons_movilization
(
    id_reason integer NOT NULL DEFAULT 1,
    name text NOT NULL,
    is_active boolean DEFAULT TRUE,
    created_at timestamp without time zone DEFAULT now(),
    updated_at timestamp without time zone DEFAULT now(),
    CONSTRAINT reasons_movilization_pkey PRIMARY KEY (id_reason)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS technical.reasons_movilization
    OWNER to n8n_user;



CREATE SEQUENCE technical.reasons_movilization_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE technical.reasons_movilization_id_seq
    OWNED BY technical.reasons_movilization.id_reason;

ALTER SEQUENCE technical.reasons_movilization_id_seq
    OWNER TO n8n_user;



ALTER TABLE IF EXISTS technical.reasons_movilization
    ALTER COLUMN id_reason SET DEFAULT nextval('technical.reasons_movilization_id_seq'::regclass);


------------------------------------------------------------------------------------------------


CREATE TABLE technical.vehicle_license
(
    id_license integer NOT NULL DEFAULT 1,
    name text NOT NULL,
    is_active boolean DEFAULT TRUE,
    created_at timestamp without time zone DEFAULT now(),
    updated_at timestamp without time zone DEFAULT now(),
    CONSTRAINT vehicle_license_pkey PRIMARY KEY (id_license)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS technical.vehicle_license
    OWNER to n8n_user;



CREATE SEQUENCE technical.vehicle_license_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE technical.vehicle_license_id_seq
    OWNED BY technical.vehicle_license.id_license;

ALTER SEQUENCE technical.vehicle_license_id_seq
    OWNER TO n8n_user;



ALTER TABLE IF EXISTS technical.vehicle_license
    ALTER COLUMN id_license SET DEFAULT nextval('vehicle_license_id_seq'::regclass);


------------------------------------------------------------------------------------------------


CREATE TABLE technical.level_gasoline
(
    id_level integer NOT NULL DEFAULT 1,
    name text NOT NULL,
    is_active boolean DEFAULT TRUE,
    created_at timestamp without time zone DEFAULT now(),
    updated_at timestamp without time zone DEFAULT now(),
    CONSTRAINT level_gasoline_pkey PRIMARY KEY (id_level)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS technical.level_gasoline
    OWNER to n8n_user;



CREATE SEQUENCE technical.level_gasoline_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE technical.level_gasoline_id_seq
    OWNED BY technical.level_gasoline.id_level;

ALTER SEQUENCE technical.level_gasoline_id_seq
    OWNER TO n8n_user;



ALTER TABLE IF EXISTS technical.level_gasoline
    ALTER COLUMN id_level SET DEFAULT nextval('level_gasoline_id_seq'::regclass);



------------------------------------------------------------------------------------------------


CREATE TABLE technical.vehicle_driver
(
    id_driver integer NOT NULL DEFAULT 1,
    name text NOT NULL,
    is_active boolean DEFAULT TRUE,
    created_at timestamp without time zone DEFAULT now(),
    updated_at timestamp without time zone DEFAULT now(),
    CONSTRAINT vehicle_driver_pkey PRIMARY KEY (id_driver)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS technical.vehicle_driver
    OWNER to n8n_user;



CREATE SEQUENCE technical.vehicle_driver_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE technical.vehicle_driver_id_seq
    OWNED BY technical.vehicle_driver.id_driver;

ALTER SEQUENCE technical.vehicle_driver_id_seq
    OWNER TO n8n_user;



ALTER TABLE IF EXISTS technical.vehicle_driver
    ALTER COLUMN id_driver SET DEFAULT nextval('vehicle_driver_id_seq'::regclass);


------------------------------------------------------------------------------------------------


CREATE TABLE technical.vehicle_copilot
(
    id_copilot integer NOT NULL DEFAULT 1,
    name text NOT NULL,
    is_active boolean DEFAULT TRUE,
    created_at timestamp without time zone DEFAULT now(),
    updated_at timestamp without time zone DEFAULT now(),
    CONSTRAINT vehicle_copilot_pkey PRIMARY KEY (id_copilot)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS technical.vehicle_copilot
    OWNER to n8n_user;



CREATE SEQUENCE technical.vehicle_copilot_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE technical.vehicle_copilot_id_seq
    OWNED BY technical.vehicle_copilot.id_copilot;

ALTER SEQUENCE technical.vehicle_copilot_id_seq
    OWNER TO n8n_user;



ALTER TABLE IF EXISTS technical.vehicle_copilot
    ALTER COLUMN id_copilot SET DEFAULT nextval('vehicle_copilot_id_seq'::regclass);



-----------------------------------------------------------------------------------------------------------------------

CREATE TABLE technical.movilization_control
(
    id_movilization integer NOT NULL DEFAULT 1,
    exit_date time without time zone,
    arrival_date time without time zone DEFAULT now(),
    license_id integer,
    initial_km text,
    final_km text,
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
        REFERENCES technical.vehicle_driver (id_driver) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
    CONSTRAINT movilization_control_license_id_fkey FOREIGN KEY (license_id)
        REFERENCES technical.vehicle_license (id_license) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS technical.movilization_control
    OWNER to n8n_user;


CREATE SEQUENCE technical.movilization_control_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE technical.movilization_control_id_seq
    OWNED BY technical.movilization_control.id_movilization;

ALTER SEQUENCE technical.movilization_control_id_seq
    OWNER TO n8n_user;



ALTER TABLE IF EXISTS technical.movilization_control
    ALTER COLUMN id_movilization SET DEFAULT nextval('movilization_control_id_seq'::regclass);


------------------------------------------------------------------------------------------------


CREATE TABLE technical.movilization_images
(
    id_image integer NOT NULL DEFAULT 1,
    movilization_id integer NOT NULL,
    image_path text,
    type text,
    created_at timestamp without time zone DEFAULT now(),
    CONSTRAINT movilization_images_pkey PRIMARY KEY (id_image),
    CONSTRAINT movilization_control_id_fkey FOREIGN KEY (movilization_id)
        REFERENCES technical.movilization_control (id_movilization) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS technical.movilization_images
    OWNER to n8n_user;



CREATE SEQUENCE technical.movilization_images_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE technical.movilization_images_id_seq
    OWNED BY technical.movilization_images.id_image;

ALTER SEQUENCE technical.movilization_images_id_seq
    OWNER TO n8n_user;



ALTER TABLE IF EXISTS technical.movilization_images
    ALTER COLUMN id_image SET DEFAULT nextval('technical.movilization_images_id_seq'::regclass);


------------------------------------------------------------------------------------------------


CREATE TABLE technical.movilization_client
(
    id_movilization_client integer NOT NULL DEFAULT 1,
    movilization_id integer NOT NULL,
    client_project_id integer NOT NULL,
    created_at timestamp without time zone DEFAULT now(),
    CONSTRAINT movilization_client_pkey PRIMARY KEY (id_movilization_client),
    CONSTRAINT movilization_control_id_fkey FOREIGN KEY (movilization_id)
        REFERENCES technical.movilization_control (id_movilization) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT client_project_id_fkey FOREIGN KEY (client_project_id)
        REFERENCES technical.client_projects (id_client_projects) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS technical.movilization_client
    OWNER to n8n_user;


CREATE SEQUENCE technical.movilization_client_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE technical.movilization_client_id_seq
    OWNED BY technical.movilization_client.id_movilization_client;

ALTER SEQUENCE technical.movilization_client_id_seq
    OWNER TO n8n_user;



ALTER TABLE IF EXISTS technical.movilization_client
    ALTER COLUMN id_movilization_client SET DEFAULT nextval('technical.movilization_client_id_seq'::regclass);


------------------------------------------------------------------------------------------------


CREATE TABLE technical.movilization_reason
(
    id_movilization_reason integer NOT NULL DEFAULT 1,
    movilization_id integer NOT NULL,
    reason_id integer NOT NULL,
    created_at timestamp without time zone DEFAULT now(),
    CONSTRAINT movilization_reason_pkey PRIMARY KEY (id_movilization_reason),
    CONSTRAINT movilization_control_id_fkey FOREIGN KEY (movilization_id)
        REFERENCES technical.movilization_control (id_movilization) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT reason_id_fkey FOREIGN KEY (reason_id)
        REFERENCES technical.reasons_movilization (id_reason) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS technical.movilization_reason
    OWNER to n8n_user;


CREATE SEQUENCE technical.movilization_reason_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE technical.movilization_reason_id_seq
    OWNED BY technical.movilization_reason.id_movilization_reason;

ALTER SEQUENCE technical.movilization_reason_id_seq
    OWNER TO n8n_user;



ALTER TABLE IF EXISTS technical.movilization_reason
    ALTER COLUMN id_movilization_reason SET DEFAULT nextval('technical.movilization_reason_id_seq'::regclass);

