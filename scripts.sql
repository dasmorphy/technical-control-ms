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
    exit_date timestamp without time zone,
    arrival_date timestamp without time zone DEFAULT now(),
    license_id integer,
    initial_km text,
    final_km text,
    final_gasoline_id integer,
    initial_gasoline_id integer,
    destiny text,
    detail_incident text,
    have_incident boolean DEFAULT FALSE,
    exit_point text,
    driver_id integer,
    observations text,
    created_at timestamp without time zone DEFAULT now(),
    updated_at timestamp without time zone DEFAULT now(),
    created_by text,
    updated_by text,
    status integer,
    CONSTRAINT movilization_control_pkey PRIMARY KEY (id_movilization),
    CONSTRAINT movilization_control_driver_id_fkey FOREIGN KEY (driver_id)
        REFERENCES technical.vehicle_driver (id_driver) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT movilization_control_license_id_fkey FOREIGN KEY (license_id)
        REFERENCES technical.vehicle_license (id_license) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT movilization_control_final_gasoline_id_fkey FOREIGN KEY (id_level)
        REFERENCES technical.level_gasoline (id_level) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT movilization_control_initial_gasoline_id_fkey FOREIGN KEY (id_level)
        REFERENCES technical.level_gasoline (id_level) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT movilization_control_status_id_fkey FOREIGN KEY (id_status)
        REFERENCES technical.movilization_status (id_status) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
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


--------------------------------------------------------------------------------------------------------------------------


CREATE TABLE technical.movilization_copilot
(
    id_movilization_copilot integer NOT NULL DEFAULT 1,
    movilization_id integer NOT NULL,
    copilot_id integer NOT NULL,
    created_at timestamp without time zone DEFAULT now(),
    CONSTRAINT movilization_copilot_pkey PRIMARY KEY (id_movilization_copilot),
    CONSTRAINT movilization_control_id_fkey FOREIGN KEY (movilization_id)
        REFERENCES technical.movilization_control (id_movilization) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT copilot_id_fkey FOREIGN KEY (copilot_id)
        REFERENCES technical.vehicle_copilot (id_copilot) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS technical.movilization_copilot
    OWNER to n8n_user;


CREATE SEQUENCE technical.movilization_copilot_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE technical.movilization_copilot_id_seq
    OWNED BY technical.movilization_copilot.id_movilization_copilot;

ALTER SEQUENCE technical.movilization_copilot_id_seq
    OWNER TO n8n_user;



ALTER TABLE IF EXISTS technical.movilization_copilot
    ALTER COLUMN id_movilization_copilot SET DEFAULT nextval('technical.movilization_copilot_id_seq'::regclass);


---------------------------------------------------------------------------------------------------------------

CREATE TABLE technical.movilization_status
(
    id_status integer NOT NULL DEFAULT 1,
    name integer NOT NULL,
    created_at timestamp without time zone DEFAULT now(),
    updated_at timestamp without time zone DEFAULT now(),
    created_by text,
    updated_by text,
    CONSTRAINT movilization_status_pkey PRIMARY KEY (id_status)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS technical.movilization_status
    OWNER to n8n_user;


CREATE SEQUENCE technical.movilization_status_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE technical.movilization_status_id_seq
    OWNED BY technical.movilization_status.id_status;

ALTER SEQUENCE technical.movilization_status_id_seq
    OWNER TO n8n_user;

ALTER TABLE IF EXISTS technical.movilization_status
    ALTER COLUMN id_status SET DEFAULT nextval('technical.movilization_status_id_seq'::regclass);



---------------------------------------------------------------------------------------------------------


CREATE TABLE technical.clients
(
    id_client integer NOT NULL,
    name text,
    created_at timestamp without time zone DEFAULT now(),
    updated_at timestamp without time zone DEFAULT now(),
    created_by text,
    updated_by text,
    CONSTRAINT client_pkey PRIMARY KEY (id_client)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS technical.clients
    OWNER to nextgen;


CREATE SEQUENCE technical.clients_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE technical.clients_id_seq
    OWNED BY technical.clients.id_client;

ALTER SEQUENCE technical.clients_id_seq
    OWNER TO nextgen;

ALTER TABLE IF EXISTS technical.clients
    ALTER COLUMN id_client SET DEFAULT nextval('technical.clients_id_seq'::regclass);


-------------------------------------------------------------------------------------------------------------------

-- Table: technical.clients_location

-- DROP TABLE IF EXISTS technical.clients_location;

CREATE TABLE IF NOT EXISTS technical.clients_location
(
    id_location integer NOT NULL DEFAULT nextval('technical.clients_location_id_seq'::regclass),
    name text COLLATE pg_catalog."default",
    address text COLLATE pg_catalog."default",
    "long" text COLLATE pg_catalog."default",
    lat text COLLATE pg_catalog."default",
    created_at timestamp without time zone DEFAULT now(),
    updated_at timestamp without time zone DEFAULT now(),
    created_by text COLLATE pg_catalog."default",
    updated_by text COLLATE pg_catalog."default",
    client_id integer,
    CONSTRAINT clients_location_pkey PRIMARY KEY (id_location),
    CONSTRAINT client_id_fkey FOREIGN KEY (client_id)
        REFERENCES technical.clients (id_client) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS technical.clients_location
    OWNER to nextgen;
-- Index: fki_client_id_fkey

-- DROP INDEX IF EXISTS technical.fki_client_id_fkey;

CREATE INDEX IF NOT EXISTS fki_client_id_fkey
    ON technical.clients_location USING btree
    (client_id ASC NULLS LAST)
    WITH (fillfactor=100, deduplicate_items=True)
    TABLESPACE pg_default;


CREATE SEQUENCE technical.clients_location_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE technical.clients_location_id_seq
    OWNED BY technical.clients_location.id_location;

ALTER SEQUENCE technical.clients_location_id_seq
    OWNER TO nextgen;

ALTER TABLE IF EXISTS technical.clients_location
    ALTER COLUMN id_location SET DEFAULT nextval('technical.clients_location_id_seq'::regclass);


---------------------------------------------------------------------------------------------------------------------------

CREATE TABLE technical.task_technical
(
    id_task integer NOT NULL,
    name text,
    description text,
    code text,
    status text;
    created_at timestamp without time zone DEFAULT now(),
    updated_at timestamp without time zone DEFAULT now(),
    created_by text,
    updated_by text,
    CONSTRAINT task_pkey PRIMARY KEY (id_task)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS technical.task_technical
    OWNER to nextgen;


CREATE SEQUENCE technical.task_technical_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE technical.task_technical_id_seq
    OWNED BY technical.task_technical.id_task;

ALTER SEQUENCE technical.task_technical_id_seq
    OWNER TO nextgen;

ALTER TABLE IF EXISTS technical.task_technical
    ALTER COLUMN id_task SET DEFAULT nextval('technical.task_technical_id_seq'::regclass);


----------------------------------------------------------------------------------------------------------------------------

-- Table: technical.task_location

-- DROP TABLE IF EXISTS technical.task_location;

CREATE TABLE IF NOT EXISTS technical.task_location
(
    id_task_location integer NOT NULL,
    location_id integer,
    task_id integer,
    created_by text COLLATE pg_catalog."default",
    updated_by text COLLATE pg_catalog."default",
    created_at timestamp without time zone DEFAULT now(),
    updated_at timestamp without time zone DEFAULT now(),
    CONSTRAINT task_location_pkey PRIMARY KEY (id_task_location),
    CONSTRAINT location_id_fkey FOREIGN KEY (location_id)
        REFERENCES technical.clients_location (id_location) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT task_id_fkey FOREIGN KEY (task_id)
        REFERENCES technical.task_technical (id_task) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS technical.task_location
    OWNER to nextgen;
-- Index: fki_location_id_fkey

-- DROP INDEX IF EXISTS technical.fki_location_id_fkey;

CREATE INDEX IF NOT EXISTS fki_location_id_fkey
    ON technical.task_location USING btree
    (location_id ASC NULLS LAST)
    WITH (fillfactor=100, deduplicate_items=True)
    TABLESPACE pg_default;
-- Index: fki_task_id_fkey

-- DROP INDEX IF EXISTS technical.fki_task_id_fkey;

CREATE INDEX IF NOT EXISTS fki_task_id_fkey
    ON technical.task_location USING btree
    (task_id ASC NULLS LAST)
    WITH (fillfactor=100, deduplicate_items=True)
    TABLESPACE pg_default;


CREATE SEQUENCE technical.task_location_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE technical.task_location_id_seq
    OWNED BY technical.task_location.id_task_location;

ALTER SEQUENCE technical.task_location_id_seq
    OWNER TO nextgen;

ALTER TABLE IF EXISTS technical.task_location
    ALTER COLUMN id_task_location SET DEFAULT nextval('technical.task_location_id_seq'::regclass);

-------------------------------------------------------------------------------------------------------------------------

CREATE TABLE technical.auditing_sections
(
    id_section integer NOT NULL,
    name text,
	order_number integer,
    created_at timestamp without time zone DEFAULT now(),
	created_by text,
    PRIMARY KEY (id_section)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS technical.auditing_sections
    OWNER to nextgen;


CREATE SEQUENCE technical.auditing_sections_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE technical.auditing_sections_id_seq
    OWNED BY technical.auditing_sections.id_section;

ALTER SEQUENCE technical.auditing_sections_id_seq
    OWNER TO nextgen;

ALTER TABLE IF EXISTS technical.auditing_sections
    ALTER COLUMN id_section SET DEFAULT nextval('technical.auditing_sections_id_seq'::regclass);


---------------------------------------------------------------------------------------------------------------


CREATE TABLE technical.auditing_item
(
    id_item integer NOT NULL,
    section_id integer,
    name text,
    order_number integer,
    created_at timestamp without time zone DEFAULT now(),
    created_by text,
    updated_at timestamp without time zone DEFAULT now(),
    updated_by text,
    CONSTRAINT auditing_item_pkey PRIMARY KEY (id_item),
    CONSTRAINT section_id_fkey FOREIGN KEY (section_id)
        REFERENCES technical.auditing_sections (id_section) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS technical.auditing_item
    OWNER to nextgen;


CREATE SEQUENCE technical.auditing_item_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE technical.auditing_item_id_seq
    OWNED BY technical.auditing_item.id_item;

ALTER SEQUENCE technical.auditing_item_id_seq
    OWNER TO nextgen;

ALTER TABLE IF EXISTS technical.auditing_item
    ALTER COLUMN id_item SET DEFAULT nextval('technical.auditing_item_id_seq'::regclass);


-------------------------------------------------------------------------------------------------------------

CREATE TABLE technical.auditing
(
    id_auditing integer NOT NULL,
    task_id integer,
    location_id integer,
    responsible text,
    percentage_compliance text,
    status text,
    created_by text,
    created_at timestamp without time zone DEFAULT now(),
    updated_at timestamp without time zone DEFAULT now(),
    updated_by text,
    CONSTRAINT auditing_pkey PRIMARY KEY (id_auditing),
    CONSTRAINT auditing_location_fkey FOREIGN KEY (location_id)
        REFERENCES technical.clients_location (id_location) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT auditing_task_id FOREIGN KEY (task_id)
        REFERENCES technical.task_technical (id_task) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS technical.auditing
    OWNER to nextgen;



CREATE SEQUENCE technical.auditing_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE technical.auditing_id_seq
    OWNED BY technical.auditing.id_auditing;

ALTER SEQUENCE technical.auditing_id_seq
    OWNER TO nextgen;

ALTER TABLE IF EXISTS technical.auditing
    ALTER COLUMN id_auditing SET DEFAULT nextval('technical.auditing_id_seq'::regclass);


------------------------------------------------------------------------------------------------------------------------

CREATE TABLE technical.auditing_response
(
    id_response integer NOT NULL,
    auditing_id integer,
    item_id integer,
    response text,
    observation text,
    created_by text,
    created_at timestamp without time zone DEFAULT now(),
    updated_at timestamp without time zone DEFAULT now(),
    updated_by text,
    CONSTRAINT auditing_response_pkey PRIMARY KEY (id_response),
    CONSTRAINT item_id_fkey FOREIGN KEY (item_id)
        REFERENCES technical.auditing_item (id_item) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT auditing_id_fkey FOREIGN KEY (auditing_id)
        REFERENCES technical.auditing (id_auditing) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS technical.auditing_response
    OWNER to nextgen;


CREATE SEQUENCE technical.auditing_response_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE technical.auditing_response_id_seq
    OWNED BY technical.auditing_response.id_response;

ALTER SEQUENCE technical.auditing_response_id_seq
    OWNER TO nextgen;

ALTER TABLE IF EXISTS technical.auditing_response
    ALTER COLUMN id_response SET DEFAULT nextval('technical.auditing_response_id_seq'::regclass);


----------------------------------------------------------------------------------------------------------------------------

CREATE TABLE technical.auditing_signatures_img
(
    id_signature integer NOT NULL,
    auditing_id integer,
    auditor_path text,
    responsible_path text,
    client_path text,
    created_at timestamp without time zone DEFAULT now(),
    CONSTRAINT signature_pkey PRIMARY KEY (id_signature),
    CONSTRAINT signature_auditing_fkey FOREIGN KEY (auditing_id)
        REFERENCES technical.auditing (id_auditing) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS technical.auditing_signatures_img
    OWNER to nextgen;


CREATE SEQUENCE technical.auditing_signatures_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE technical.auditing_signatures_id_seq
    OWNED BY technical.auditing_signatures_img.id_signature;

ALTER SEQUENCE technical.auditing_signatures_id_seq
    OWNER TO nextgen;

ALTER TABLE IF EXISTS technical.auditing_signatures_img
    ALTER COLUMN id_signature SET DEFAULT nextval('technical.auditing_signatures_id_seq'::regclass);


-----------------------------------------------------------------------------------------------------------------

-- Table: technical.technical_record

-- DROP TABLE IF EXISTS technical.technical_record;

CREATE TABLE IF NOT EXISTS technical.technical_record
(
    id_record integer NOT NULL DEFAULT nextval('technical.technical_record_id_seq'::regclass),
    task_id integer,
    resume text COLLATE pg_catalog."default",
    created_by text COLLATE pg_catalog."default",
    updated_by text COLLATE pg_catalog."default",
    created_at timestamp without time zone DEFAULT now(),
    updated_at timestamp without time zone DEFAULT now(),
    client_id integer,
    location_id integer,
    CONSTRAINT technical_record_pkey PRIMARY KEY (id_record),
    CONSTRAINT technical_client_fkey FOREIGN KEY (client_id)
        REFERENCES technical.clients (id_client) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT technical_location_fkey FOREIGN KEY (location_id)
        REFERENCES technical.clients_location (id_location) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION,
    CONSTRAINT technical_task_fkey FOREIGN KEY (task_id)
        REFERENCES technical.task_technical (id_task) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS technical.technical_record
    OWNER to nextgen;
-- Index: fki_technical_client_fkey

-- DROP INDEX IF EXISTS technical.fki_technical_client_fkey;

CREATE INDEX IF NOT EXISTS fki_technical_client_fkey
    ON technical.technical_record USING btree
    (client_id ASC NULLS LAST)
    WITH (fillfactor=100, deduplicate_items=True)
    TABLESPACE pg_default;
-- Index: fki_technical_location_fkey

-- DROP INDEX IF EXISTS technical.fki_technical_location_fkey;

CREATE INDEX IF NOT EXISTS fki_technical_location_fkey
    ON technical.technical_record USING btree
    (location_id ASC NULLS LAST)
    WITH (fillfactor=100, deduplicate_items=True)
    TABLESPACE pg_default;
-- Index: fki_technical_task_fkey

-- DROP INDEX IF EXISTS technical.fki_technical_task_fkey;

CREATE INDEX IF NOT EXISTS fki_technical_task_fkey
    ON technical.technical_record USING btree
    (task_id ASC NULLS LAST)
    WITH (fillfactor=100, deduplicate_items=True)
    TABLESPACE pg_default;


CREATE SEQUENCE technical.technical_record_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE technical.technical_record_id_seq
    OWNED BY technical.technical_record.id_record;

ALTER SEQUENCE technical.technical_record_id_seq
    OWNER TO nextgen;

ALTER TABLE IF EXISTS technical.technical_record
    ALTER COLUMN id_record SET DEFAULT nextval('technical.technical_record_id_seq'::regclass);

-----------------------------------------------------------------------------------------------------------------------------------------

-- Table: technical.material_technical_record

-- DROP TABLE IF EXISTS technical.material_technical_record;

CREATE TABLE IF NOT EXISTS technical.material_technical_record
(
    id_material_record integer NOT NULL DEFAULT nextval('technical.material_technical_record_id_seq'::regclass),
    record_id integer,
    material text COLLATE pg_catalog."default",
    quantity integer,
    created_at timestamp without time zone DEFAULT now(),
    updated_at timestamp without time zone DEFAULT now(),
    CONSTRAINT material_record_pkey PRIMARY KEY (id_material_record),
    CONSTRAINT material_record_fkey FOREIGN KEY (record_id)
        REFERENCES technical.technical_record (id_record) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS technical.material_technical_record
    OWNER to nextgen;
-- Index: fki_material_record_fkey

-- DROP INDEX IF EXISTS technical.fki_material_record_fkey;

CREATE INDEX IF NOT EXISTS fki_material_record_fkey
    ON technical.material_technical_record USING btree
    (record_id ASC NULLS LAST)
    WITH (fillfactor=100, deduplicate_items=True)
    TABLESPACE pg_default;


CREATE SEQUENCE technical.material_technical_record_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE technical.material_technical_record_id_seq
    OWNED BY technical.material_technical_record.id_material_record;

ALTER SEQUENCE technical.material_technical_record_id_seq
    OWNER TO nextgen;

ALTER TABLE IF EXISTS technical.material_technical_record
    ALTER COLUMN id_material_record SET DEFAULT nextval('technical.material_technical_record_id_seq'::regclass);



--------------------------------------------------------------------------------------------------------------

CREATE TABLE technical.tech_record_image
(
    id_image integer NOT NULL,
    record_id integer,
    image_path text,
    created_at timestamp without time zone DEFAULT now(),
    CONSTRAINT record_image_pkey PRIMARY KEY (id_image),
    CONSTRAINT image_record_id_fkey FOREIGN KEY (record_id)
        REFERENCES technical.technical_record (id_record) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS technical.tech_record_image
    OWNER to nextgen;

CREATE SEQUENCE technical.tech_record_image_id_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 2147483647
    CACHE 1;

ALTER SEQUENCE technical.tech_record_image_id_seq
    OWNED BY technical.tech_record_image.id_image;

ALTER SEQUENCE technical.tech_record_image_id_seq
    OWNER TO nextgen;

ALTER TABLE IF EXISTS technical.tech_record_image
    ALTER COLUMN id_image SET DEFAULT nextval('technical.tech_record_image_id_seq'::regclass);
