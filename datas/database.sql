PGDMP                         z           epic_db    14.3    14.3 �    �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16394    epic_db    DATABASE     c   CREATE DATABASE epic_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'French_France.1252';
    DROP DATABASE epic_db;
                postgres    false            �            1259    16617    app_contract    TABLE     �  CREATE TABLE public.app_contract (
    id bigint NOT NULL,
    title character varying(100) NOT NULL,
    price integer NOT NULL,
    payed boolean NOT NULL,
    amount_payed integer NOT NULL,
    contract_infos text NOT NULL,
    customer_signature boolean NOT NULL,
    creation_date date NOT NULL,
    modified_date date NOT NULL,
    customer_id_id bigint NOT NULL,
    sales_contact_id bigint NOT NULL,
    employee_signature boolean NOT NULL,
    signed boolean NOT NULL
);
     DROP TABLE public.app_contract;
       public         heap    postgres    false            �            1259    16616    app_contract_id_seq    SEQUENCE     |   CREATE SEQUENCE public.app_contract_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.app_contract_id_seq;
       public          postgres    false    230            �           0    0    app_contract_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.app_contract_id_seq OWNED BY public.app_contract.id;
          public          postgres    false    229            �            1259    16626 	   app_event    TABLE     C  CREATE TABLE public.app_event (
    id bigint NOT NULL,
    name character varying(100) NOT NULL,
    description text,
    program text,
    due_date date,
    creation_date date NOT NULL,
    modified_date date NOT NULL,
    contract_id_id bigint NOT NULL,
    customer_id_id bigint NOT NULL,
    support_id_id bigint
);
    DROP TABLE public.app_event;
       public         heap    postgres    false            �            1259    16625    app_event_id_seq    SEQUENCE     y   CREATE SEQUENCE public.app_event_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.app_event_id_seq;
       public          postgres    false    232            �           0    0    app_event_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.app_event_id_seq OWNED BY public.app_event.id;
          public          postgres    false    231            �            1259    16664    app_event_providers    TABLE     �   CREATE TABLE public.app_event_providers (
    id bigint NOT NULL,
    event_id bigint NOT NULL,
    provider_id bigint NOT NULL
);
 '   DROP TABLE public.app_event_providers;
       public         heap    postgres    false            �            1259    16663    app_event_providers_id_seq    SEQUENCE     �   CREATE SEQUENCE public.app_event_providers_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.app_event_providers_id_seq;
       public          postgres    false    238            �           0    0    app_event_providers_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.app_event_providers_id_seq OWNED BY public.app_event_providers.id;
          public          postgres    false    237            �            1259    16635    app_prospect    TABLE     �  CREATE TABLE public.app_prospect (
    id bigint NOT NULL,
    company_name character varying(100) NOT NULL,
    email character varying(100) NOT NULL,
    phone_number character varying(20) NOT NULL,
    creation_date date NOT NULL,
    modified_date date NOT NULL,
    last_contact date,
    sales_contact_id bigint,
    converted boolean NOT NULL,
    first_name character varying(100) NOT NULL,
    last_name character varying(100) NOT NULL
);
     DROP TABLE public.app_prospect;
       public         heap    postgres    false            �            1259    16634    app_prospect_id_seq    SEQUENCE     |   CREATE SEQUENCE public.app_prospect_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.app_prospect_id_seq;
       public          postgres    false    234            �           0    0    app_prospect_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.app_prospect_id_seq OWNED BY public.app_prospect.id;
          public          postgres    false    233            �            1259    16642    app_provider    TABLE     �   CREATE TABLE public.app_provider (
    id bigint NOT NULL,
    company_name character varying(100) NOT NULL,
    email character varying(100) NOT NULL,
    phone_number character varying(20) NOT NULL,
    type character varying(10) NOT NULL
);
     DROP TABLE public.app_provider;
       public         heap    postgres    false            �            1259    16641    app_provider_id_seq    SEQUENCE     |   CREATE SEQUENCE public.app_provider_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.app_provider_id_seq;
       public          postgres    false    236            �           0    0    app_provider_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.app_provider_id_seq OWNED BY public.app_provider.id;
          public          postgres    false    235            �            1259    16421 
   auth_group    TABLE     f   CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);
    DROP TABLE public.auth_group;
       public         heap    postgres    false            �            1259    16420    auth_group_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.auth_group_id_seq;
       public          postgres    false    216            �           0    0    auth_group_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;
          public          postgres    false    215            �            1259    16430    auth_group_permissions    TABLE     �   CREATE TABLE public.auth_group_permissions (
    id bigint NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);
 *   DROP TABLE public.auth_group_permissions;
       public         heap    postgres    false            �            1259    16429    auth_group_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.auth_group_permissions_id_seq;
       public          postgres    false    218            �           0    0    auth_group_permissions_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;
          public          postgres    false    217            �            1259    16414    auth_permission    TABLE     �   CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);
 #   DROP TABLE public.auth_permission;
       public         heap    postgres    false            �            1259    16413    auth_permission_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.auth_permission_id_seq;
       public          postgres    false    214            �           0    0    auth_permission_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;
          public          postgres    false    213            �            1259    16801    authtoken_token    TABLE     �   CREATE TABLE public.authtoken_token (
    key character varying(40) NOT NULL,
    created timestamp with time zone NOT NULL,
    user_id bigint NOT NULL
);
 #   DROP TABLE public.authtoken_token;
       public         heap    postgres    false            �            1259    16518    django_admin_log    TABLE     �  CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id bigint NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);
 $   DROP TABLE public.django_admin_log;
       public         heap    postgres    false            �            1259    16517    django_admin_log_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.django_admin_log_id_seq;
       public          postgres    false    226            �           0    0    django_admin_log_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;
          public          postgres    false    225            �            1259    16405    django_content_type    TABLE     �   CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);
 '   DROP TABLE public.django_content_type;
       public         heap    postgres    false            �            1259    16404    django_content_type_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.django_content_type_id_seq;
       public          postgres    false    212            �           0    0    django_content_type_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;
          public          postgres    false    211            �            1259    16396    django_migrations    TABLE     �   CREATE TABLE public.django_migrations (
    id bigint NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);
 %   DROP TABLE public.django_migrations;
       public         heap    postgres    false            �            1259    16395    django_migrations_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_migrations_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.django_migrations_id_seq;
       public          postgres    false    210            �           0    0    django_migrations_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;
          public          postgres    false    209            �            1259    16822    django_session    TABLE     �   CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);
 "   DROP TABLE public.django_session;
       public         heap    postgres    false            �            1259    16552    login_customer    TABLE     �   CREATE TABLE public.login_customer (
    user_ptr_id bigint NOT NULL,
    company_name character varying(100) NOT NULL,
    last_contact date,
    sales_contact_id bigint
);
 "   DROP TABLE public.login_customer;
       public         heap    postgres    false            �            1259    16547    login_employee    TABLE     �   CREATE TABLE public.login_employee (
    user_ptr_id bigint NOT NULL,
    company_name character varying(100) NOT NULL,
    manager_id bigint
);
 "   DROP TABLE public.login_employee;
       public         heap    postgres    false            �            1259    16463 
   login_user    TABLE     h  CREATE TABLE public.login_user (
    id bigint NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    username character varying(32) NOT NULL,
    email character varying(64) NOT NULL,
    first_name character varying(32) NOT NULL,
    last_name character varying(32) NOT NULL,
    password character varying(128) NOT NULL,
    creation_date date,
    modified_date date,
    phone_number character varying(20) NOT NULL,
    status character varying(100) NOT NULL
);
    DROP TABLE public.login_user;
       public         heap    postgres    false            �            1259    16474    login_user_groups    TABLE     ~   CREATE TABLE public.login_user_groups (
    id bigint NOT NULL,
    user_id bigint NOT NULL,
    group_id integer NOT NULL
);
 %   DROP TABLE public.login_user_groups;
       public         heap    postgres    false            �            1259    16473    login_user_groups_id_seq    SEQUENCE     �   CREATE SEQUENCE public.login_user_groups_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.login_user_groups_id_seq;
       public          postgres    false    222            �           0    0    login_user_groups_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.login_user_groups_id_seq OWNED BY public.login_user_groups.id;
          public          postgres    false    221            �            1259    16462    login_user_id_seq    SEQUENCE     z   CREATE SEQUENCE public.login_user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.login_user_id_seq;
       public          postgres    false    220            �           0    0    login_user_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.login_user_id_seq OWNED BY public.login_user.id;
          public          postgres    false    219            �            1259    16481    login_user_user_permissions    TABLE     �   CREATE TABLE public.login_user_user_permissions (
    id bigint NOT NULL,
    user_id bigint NOT NULL,
    permission_id integer NOT NULL
);
 /   DROP TABLE public.login_user_user_permissions;
       public         heap    postgres    false            �            1259    16480 "   login_user_user_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.login_user_user_permissions_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 9   DROP SEQUENCE public.login_user_user_permissions_id_seq;
       public          postgres    false    224            �           0    0 "   login_user_user_permissions_id_seq    SEQUENCE OWNED BY     i   ALTER SEQUENCE public.login_user_user_permissions_id_seq OWNED BY public.login_user_user_permissions.id;
          public          postgres    false    223            �           2604    16620    app_contract id    DEFAULT     r   ALTER TABLE ONLY public.app_contract ALTER COLUMN id SET DEFAULT nextval('public.app_contract_id_seq'::regclass);
 >   ALTER TABLE public.app_contract ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    230    229    230            �           2604    16629    app_event id    DEFAULT     l   ALTER TABLE ONLY public.app_event ALTER COLUMN id SET DEFAULT nextval('public.app_event_id_seq'::regclass);
 ;   ALTER TABLE public.app_event ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    231    232    232            �           2604    16667    app_event_providers id    DEFAULT     �   ALTER TABLE ONLY public.app_event_providers ALTER COLUMN id SET DEFAULT nextval('public.app_event_providers_id_seq'::regclass);
 E   ALTER TABLE public.app_event_providers ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    238    237    238            �           2604    16638    app_prospect id    DEFAULT     r   ALTER TABLE ONLY public.app_prospect ALTER COLUMN id SET DEFAULT nextval('public.app_prospect_id_seq'::regclass);
 >   ALTER TABLE public.app_prospect ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    234    233    234            �           2604    16645    app_provider id    DEFAULT     r   ALTER TABLE ONLY public.app_provider ALTER COLUMN id SET DEFAULT nextval('public.app_provider_id_seq'::regclass);
 >   ALTER TABLE public.app_provider ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    235    236    236            �           2604    16424    auth_group id    DEFAULT     n   ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);
 <   ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    216    215    216            �           2604    16433    auth_group_permissions id    DEFAULT     �   ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);
 H   ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    217    218    218            �           2604    16417    auth_permission id    DEFAULT     x   ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);
 A   ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    214    213    214            �           2604    16521    django_admin_log id    DEFAULT     z   ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);
 B   ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    226    225    226            �           2604    16408    django_content_type id    DEFAULT     �   ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);
 E   ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    212    211    212            �           2604    16399    django_migrations id    DEFAULT     |   ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);
 C   ALTER TABLE public.django_migrations ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    209    210    210            �           2604    16466    login_user id    DEFAULT     n   ALTER TABLE ONLY public.login_user ALTER COLUMN id SET DEFAULT nextval('public.login_user_id_seq'::regclass);
 <   ALTER TABLE public.login_user ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    219    220    220            �           2604    16477    login_user_groups id    DEFAULT     |   ALTER TABLE ONLY public.login_user_groups ALTER COLUMN id SET DEFAULT nextval('public.login_user_groups_id_seq'::regclass);
 C   ALTER TABLE public.login_user_groups ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    222    221    222            �           2604    16484    login_user_user_permissions id    DEFAULT     �   ALTER TABLE ONLY public.login_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.login_user_user_permissions_id_seq'::regclass);
 M   ALTER TABLE public.login_user_user_permissions ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    224    223    224            �          0    16617    app_contract 
   TABLE DATA           �   COPY public.app_contract (id, title, price, payed, amount_payed, contract_infos, customer_signature, creation_date, modified_date, customer_id_id, sales_contact_id, employee_signature, signed) FROM stdin;
    public          postgres    false    230   ��       �          0    16626 	   app_event 
   TABLE DATA           �   COPY public.app_event (id, name, description, program, due_date, creation_date, modified_date, contract_id_id, customer_id_id, support_id_id) FROM stdin;
    public          postgres    false    232   m�       �          0    16664    app_event_providers 
   TABLE DATA           H   COPY public.app_event_providers (id, event_id, provider_id) FROM stdin;
    public          postgres    false    238   ��       �          0    16635    app_prospect 
   TABLE DATA           �   COPY public.app_prospect (id, company_name, email, phone_number, creation_date, modified_date, last_contact, sales_contact_id, converted, first_name, last_name) FROM stdin;
    public          postgres    false    234   ��       �          0    16642    app_provider 
   TABLE DATA           S   COPY public.app_provider (id, company_name, email, phone_number, type) FROM stdin;
    public          postgres    false    236   ��       �          0    16421 
   auth_group 
   TABLE DATA           .   COPY public.auth_group (id, name) FROM stdin;
    public          postgres    false    216   �       �          0    16430    auth_group_permissions 
   TABLE DATA           M   COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
    public          postgres    false    218   �       �          0    16414    auth_permission 
   TABLE DATA           N   COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
    public          postgres    false    214   <�       �          0    16801    authtoken_token 
   TABLE DATA           @   COPY public.authtoken_token (key, created, user_id) FROM stdin;
    public          postgres    false    239   y�       �          0    16518    django_admin_log 
   TABLE DATA           �   COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
    public          postgres    false    226   ��       �          0    16405    django_content_type 
   TABLE DATA           C   COPY public.django_content_type (id, app_label, model) FROM stdin;
    public          postgres    false    212   ��       �          0    16396    django_migrations 
   TABLE DATA           C   COPY public.django_migrations (id, app, name, applied) FROM stdin;
    public          postgres    false    210   H�       �          0    16822    django_session 
   TABLE DATA           P   COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
    public          postgres    false    240   ��       �          0    16552    login_customer 
   TABLE DATA           c   COPY public.login_customer (user_ptr_id, company_name, last_contact, sales_contact_id) FROM stdin;
    public          postgres    false    228   ��       �          0    16547    login_employee 
   TABLE DATA           O   COPY public.login_employee (user_ptr_id, company_name, manager_id) FROM stdin;
    public          postgres    false    227   ��       �          0    16463 
   login_user 
   TABLE DATA           �   COPY public.login_user (id, last_login, is_superuser, is_staff, is_active, date_joined, username, email, first_name, last_name, password, creation_date, modified_date, phone_number, status) FROM stdin;
    public          postgres    false    220   �       �          0    16474    login_user_groups 
   TABLE DATA           B   COPY public.login_user_groups (id, user_id, group_id) FROM stdin;
    public          postgres    false    222   �      �          0    16481    login_user_user_permissions 
   TABLE DATA           Q   COPY public.login_user_user_permissions (id, user_id, permission_id) FROM stdin;
    public          postgres    false    224   �      �           0    0    app_contract_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.app_contract_id_seq', 7, true);
          public          postgres    false    229            �           0    0    app_event_id_seq    SEQUENCE SET     >   SELECT pg_catalog.setval('public.app_event_id_seq', 2, true);
          public          postgres    false    231            �           0    0    app_event_providers_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.app_event_providers_id_seq', 7, true);
          public          postgres    false    237            �           0    0    app_prospect_id_seq    SEQUENCE SET     A   SELECT pg_catalog.setval('public.app_prospect_id_seq', 5, true);
          public          postgres    false    233            �           0    0    app_provider_id_seq    SEQUENCE SET     B   SELECT pg_catalog.setval('public.app_provider_id_seq', 12, true);
          public          postgres    false    235            �           0    0    auth_group_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.auth_group_id_seq', 1, false);
          public          postgres    false    215            �           0    0    auth_group_permissions_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);
          public          postgres    false    217            �           0    0    auth_permission_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.auth_permission_id_seq', 168, true);
          public          postgres    false    213            �           0    0    django_admin_log_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.django_admin_log_id_seq', 24, true);
          public          postgres    false    225            �           0    0    django_content_type_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.django_content_type_id_seq', 42, true);
          public          postgres    false    211            �           0    0    django_migrations_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.django_migrations_id_seq', 65, true);
          public          postgres    false    209            �           0    0    login_user_groups_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.login_user_groups_id_seq', 1, false);
          public          postgres    false    221            �           0    0    login_user_id_seq    SEQUENCE SET     @   SELECT pg_catalog.setval('public.login_user_id_seq', 11, true);
          public          postgres    false    219            �           0    0 "   login_user_user_permissions_id_seq    SEQUENCE SET     Q   SELECT pg_catalog.setval('public.login_user_user_permissions_id_seq', 1, false);
          public          postgres    false    223            �           2606    16624    app_contract app_contract_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.app_contract
    ADD CONSTRAINT app_contract_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.app_contract DROP CONSTRAINT app_contract_pkey;
       public            postgres    false    230            �           2606    16795 0   app_event app_event_contract_id_id_fcd9151c_uniq 
   CONSTRAINT     u   ALTER TABLE ONLY public.app_event
    ADD CONSTRAINT app_event_contract_id_id_fcd9151c_uniq UNIQUE (contract_id_id);
 Z   ALTER TABLE ONLY public.app_event DROP CONSTRAINT app_event_contract_id_id_fcd9151c_uniq;
       public            postgres    false    232            �           2606    16633    app_event app_event_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.app_event
    ADD CONSTRAINT app_event_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.app_event DROP CONSTRAINT app_event_pkey;
       public            postgres    false    232                       2606    16689 J   app_event_providers app_event_providers_event_id_provider_id_1e1a79fa_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.app_event_providers
    ADD CONSTRAINT app_event_providers_event_id_provider_id_1e1a79fa_uniq UNIQUE (event_id, provider_id);
 t   ALTER TABLE ONLY public.app_event_providers DROP CONSTRAINT app_event_providers_event_id_provider_id_1e1a79fa_uniq;
       public            postgres    false    238    238                       2606    16669 ,   app_event_providers app_event_providers_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.app_event_providers
    ADD CONSTRAINT app_event_providers_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.app_event_providers DROP CONSTRAINT app_event_providers_pkey;
       public            postgres    false    238            �           2606    16779 -   app_prospect app_prospect_email_ecf92de9_uniq 
   CONSTRAINT     i   ALTER TABLE ONLY public.app_prospect
    ADD CONSTRAINT app_prospect_email_ecf92de9_uniq UNIQUE (email);
 W   ALTER TABLE ONLY public.app_prospect DROP CONSTRAINT app_prospect_email_ecf92de9_uniq;
       public            postgres    false    234            �           2606    16640    app_prospect app_prospect_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.app_prospect
    ADD CONSTRAINT app_prospect_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.app_prospect DROP CONSTRAINT app_prospect_pkey;
       public            postgres    false    234                       2606    16647    app_provider app_provider_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.app_provider
    ADD CONSTRAINT app_provider_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.app_provider DROP CONSTRAINT app_provider_pkey;
       public            postgres    false    236            �           2606    16460    auth_group auth_group_name_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);
 H   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
       public            postgres    false    216            �           2606    16446 R   auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);
 |   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq;
       public            postgres    false    218    218            �           2606    16435 2   auth_group_permissions auth_group_permissions_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
       public            postgres    false    218            �           2606    16426    auth_group auth_group_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
       public            postgres    false    216            �           2606    16437 F   auth_permission auth_permission_content_type_id_codename_01ab375a_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);
 p   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq;
       public            postgres    false    214    214            �           2606    16419 $   auth_permission auth_permission_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
       public            postgres    false    214            
           2606    16805 $   authtoken_token authtoken_token_pkey 
   CONSTRAINT     c   ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_pkey PRIMARY KEY (key);
 N   ALTER TABLE ONLY public.authtoken_token DROP CONSTRAINT authtoken_token_pkey;
       public            postgres    false    239                       2606    16807 +   authtoken_token authtoken_token_user_id_key 
   CONSTRAINT     i   ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_key UNIQUE (user_id);
 U   ALTER TABLE ONLY public.authtoken_token DROP CONSTRAINT authtoken_token_user_id_key;
       public            postgres    false    239            �           2606    16526 &   django_admin_log django_admin_log_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
       public            postgres    false    226            �           2606    16412 E   django_content_type django_content_type_app_label_model_76bd3d3b_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);
 o   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq;
       public            postgres    false    212    212            �           2606    16410 ,   django_content_type django_content_type_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
       public            postgres    false    212            �           2606    16403 (   django_migrations django_migrations_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.django_migrations DROP CONSTRAINT django_migrations_pkey;
       public            postgres    false    210                       2606    16828 "   django_session django_session_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);
 L   ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
       public            postgres    false    240            �           2606    16556 "   login_customer login_customer_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.login_customer
    ADD CONSTRAINT login_customer_pkey PRIMARY KEY (user_ptr_id);
 L   ALTER TABLE ONLY public.login_customer DROP CONSTRAINT login_customer_pkey;
       public            postgres    false    228            �           2606    16551 "   login_employee login_employee_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.login_employee
    ADD CONSTRAINT login_employee_pkey PRIMARY KEY (user_ptr_id);
 L   ALTER TABLE ONLY public.login_employee DROP CONSTRAINT login_employee_pkey;
       public            postgres    false    227            �           2606    16472    login_user login_user_email_key 
   CONSTRAINT     [   ALTER TABLE ONLY public.login_user
    ADD CONSTRAINT login_user_email_key UNIQUE (email);
 I   ALTER TABLE ONLY public.login_user DROP CONSTRAINT login_user_email_key;
       public            postgres    false    220            �           2606    16479 (   login_user_groups login_user_groups_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.login_user_groups
    ADD CONSTRAINT login_user_groups_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.login_user_groups DROP CONSTRAINT login_user_groups_pkey;
       public            postgres    false    222            �           2606    16490 B   login_user_groups login_user_groups_user_id_group_id_e039d177_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.login_user_groups
    ADD CONSTRAINT login_user_groups_user_id_group_id_e039d177_uniq UNIQUE (user_id, group_id);
 l   ALTER TABLE ONLY public.login_user_groups DROP CONSTRAINT login_user_groups_user_id_group_id_e039d177_uniq;
       public            postgres    false    222    222            �           2606    16468    login_user login_user_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.login_user
    ADD CONSTRAINT login_user_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.login_user DROP CONSTRAINT login_user_pkey;
       public            postgres    false    220            �           2606    16486 <   login_user_user_permissions login_user_user_permissions_pkey 
   CONSTRAINT     z   ALTER TABLE ONLY public.login_user_user_permissions
    ADD CONSTRAINT login_user_user_permissions_pkey PRIMARY KEY (id);
 f   ALTER TABLE ONLY public.login_user_user_permissions DROP CONSTRAINT login_user_user_permissions_pkey;
       public            postgres    false    224            �           2606    16504 [   login_user_user_permissions login_user_user_permissions_user_id_permission_id_a985464b_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.login_user_user_permissions
    ADD CONSTRAINT login_user_user_permissions_user_id_permission_id_a985464b_uniq UNIQUE (user_id, permission_id);
 �   ALTER TABLE ONLY public.login_user_user_permissions DROP CONSTRAINT login_user_user_permissions_user_id_permission_id_a985464b_uniq;
       public            postgres    false    224    224            �           2606    16470 "   login_user login_user_username_key 
   CONSTRAINT     a   ALTER TABLE ONLY public.login_user
    ADD CONSTRAINT login_user_username_key UNIQUE (username);
 L   ALTER TABLE ONLY public.login_user DROP CONSTRAINT login_user_username_key;
       public            postgres    false    220            �           1259    16703 $   app_contract_customer_id_id_bcc42707    INDEX     g   CREATE INDEX app_contract_customer_id_id_bcc42707 ON public.app_contract USING btree (customer_id_id);
 8   DROP INDEX public.app_contract_customer_id_id_bcc42707;
       public            postgres    false    230            �           1259    16704 &   app_contract_sales_contact_id_acaa720d    INDEX     k   CREATE INDEX app_contract_sales_contact_id_acaa720d ON public.app_contract USING btree (sales_contact_id);
 :   DROP INDEX public.app_contract_sales_contact_id_acaa720d;
       public            postgres    false    230            �           1259    16687 !   app_event_customer_id_id_11a8f188    INDEX     a   CREATE INDEX app_event_customer_id_id_11a8f188 ON public.app_event USING btree (customer_id_id);
 5   DROP INDEX public.app_event_customer_id_id_11a8f188;
       public            postgres    false    232                       1259    16700 %   app_event_providers_event_id_035a130a    INDEX     i   CREATE INDEX app_event_providers_event_id_035a130a ON public.app_event_providers USING btree (event_id);
 9   DROP INDEX public.app_event_providers_event_id_035a130a;
       public            postgres    false    238                       1259    16701 (   app_event_providers_provider_id_2f82d6fd    INDEX     o   CREATE INDEX app_event_providers_provider_id_2f82d6fd ON public.app_event_providers USING btree (provider_id);
 <   DROP INDEX public.app_event_providers_provider_id_2f82d6fd;
       public            postgres    false    238            �           1259    16702     app_event_support_id_id_7fec16a6    INDEX     _   CREATE INDEX app_event_support_id_id_7fec16a6 ON public.app_event USING btree (support_id_id);
 4   DROP INDEX public.app_event_support_id_id_7fec16a6;
       public            postgres    false    232            �           1259    16780     app_prospect_email_ecf92de9_like    INDEX     n   CREATE INDEX app_prospect_email_ecf92de9_like ON public.app_prospect USING btree (email varchar_pattern_ops);
 4   DROP INDEX public.app_prospect_email_ecf92de9_like;
       public            postgres    false    234            �           1259    16685 &   app_prospect_sales_contact_id_a17c4f35    INDEX     k   CREATE INDEX app_prospect_sales_contact_id_a17c4f35 ON public.app_prospect USING btree (sales_contact_id);
 :   DROP INDEX public.app_prospect_sales_contact_id_a17c4f35;
       public            postgres    false    234            �           1259    16461    auth_group_name_a6ea08ec_like    INDEX     h   CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);
 1   DROP INDEX public.auth_group_name_a6ea08ec_like;
       public            postgres    false    216            �           1259    16457 (   auth_group_permissions_group_id_b120cbf9    INDEX     o   CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);
 <   DROP INDEX public.auth_group_permissions_group_id_b120cbf9;
       public            postgres    false    218            �           1259    16458 -   auth_group_permissions_permission_id_84c5c92e    INDEX     y   CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);
 A   DROP INDEX public.auth_group_permissions_permission_id_84c5c92e;
       public            postgres    false    218            �           1259    16443 (   auth_permission_content_type_id_2f476e4b    INDEX     o   CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);
 <   DROP INDEX public.auth_permission_content_type_id_2f476e4b;
       public            postgres    false    214                       1259    16813 !   authtoken_token_key_10f0b77e_like    INDEX     p   CREATE INDEX authtoken_token_key_10f0b77e_like ON public.authtoken_token USING btree (key varchar_pattern_ops);
 5   DROP INDEX public.authtoken_token_key_10f0b77e_like;
       public            postgres    false    239            �           1259    16537 )   django_admin_log_content_type_id_c4bce8eb    INDEX     q   CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);
 =   DROP INDEX public.django_admin_log_content_type_id_c4bce8eb;
       public            postgres    false    226            �           1259    16538 !   django_admin_log_user_id_c564eba6    INDEX     a   CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);
 5   DROP INDEX public.django_admin_log_user_id_c564eba6;
       public            postgres    false    226                       1259    16830 #   django_session_expire_date_a5c62663    INDEX     e   CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);
 7   DROP INDEX public.django_session_expire_date_a5c62663;
       public            postgres    false    240                       1259    16829 (   django_session_session_key_c0390e0f_like    INDEX     ~   CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);
 <   DROP INDEX public.django_session_session_key_c0390e0f_like;
       public            postgres    false    240            �           1259    16572 (   login_customer_sales_contact_id_ce094e4c    INDEX     o   CREATE INDEX login_customer_sales_contact_id_ce094e4c ON public.login_customer USING btree (sales_contact_id);
 <   DROP INDEX public.login_customer_sales_contact_id_ce094e4c;
       public            postgres    false    228            �           1259    16598 "   login_employee_manager_id_c37ca2d8    INDEX     c   CREATE INDEX login_employee_manager_id_c37ca2d8 ON public.login_employee USING btree (manager_id);
 6   DROP INDEX public.login_employee_manager_id_c37ca2d8;
       public            postgres    false    227            �           1259    16488    login_user_email_a5f3da64_like    INDEX     j   CREATE INDEX login_user_email_a5f3da64_like ON public.login_user USING btree (email varchar_pattern_ops);
 2   DROP INDEX public.login_user_email_a5f3da64_like;
       public            postgres    false    220            �           1259    16502 #   login_user_groups_group_id_a8810f0d    INDEX     e   CREATE INDEX login_user_groups_group_id_a8810f0d ON public.login_user_groups USING btree (group_id);
 7   DROP INDEX public.login_user_groups_group_id_a8810f0d;
       public            postgres    false    222            �           1259    16501 "   login_user_groups_user_id_f6fabf84    INDEX     c   CREATE INDEX login_user_groups_user_id_f6fabf84 ON public.login_user_groups USING btree (user_id);
 6   DROP INDEX public.login_user_groups_user_id_f6fabf84;
       public            postgres    false    222            �           1259    16516 2   login_user_user_permissions_permission_id_08d04f9c    INDEX     �   CREATE INDEX login_user_user_permissions_permission_id_08d04f9c ON public.login_user_user_permissions USING btree (permission_id);
 F   DROP INDEX public.login_user_user_permissions_permission_id_08d04f9c;
       public            postgres    false    224            �           1259    16515 ,   login_user_user_permissions_user_id_2a4ce843    INDEX     w   CREATE INDEX login_user_user_permissions_user_id_2a4ce843 ON public.login_user_user_permissions USING btree (user_id);
 @   DROP INDEX public.login_user_user_permissions_user_id_2a4ce843;
       public            postgres    false    224            �           1259    16487 !   login_user_username_387fa286_like    INDEX     p   CREATE INDEX login_user_username_387fa286_like ON public.login_user USING btree (username varchar_pattern_ops);
 5   DROP INDEX public.login_user_username_387fa286_like;
       public            postgres    false    220                       2606    16757 >   app_contract app_contract_customer_id_id_bcc42707_fk_login_cus    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_contract
    ADD CONSTRAINT app_contract_customer_id_id_bcc42707_fk_login_cus FOREIGN KEY (customer_id_id) REFERENCES public.login_customer(user_ptr_id) DEFERRABLE INITIALLY DEFERRED;
 h   ALTER TABLE ONLY public.app_contract DROP CONSTRAINT app_contract_customer_id_id_bcc42707_fk_login_cus;
       public          postgres    false    3310    228    230                       2606    16762 @   app_contract app_contract_sales_contact_id_acaa720d_fk_login_emp    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_contract
    ADD CONSTRAINT app_contract_sales_contact_id_acaa720d_fk_login_emp FOREIGN KEY (sales_contact_id) REFERENCES public.login_employee(user_ptr_id) DEFERRABLE INITIALLY DEFERRED;
 j   ALTER TABLE ONLY public.app_contract DROP CONSTRAINT app_contract_sales_contact_id_acaa720d_fk_login_emp;
       public          postgres    false    230    3308    227            "           2606    16796 >   app_event app_event_contract_id_id_fcd9151c_fk_app_contract_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_event
    ADD CONSTRAINT app_event_contract_id_id_fcd9151c_fk_app_contract_id FOREIGN KEY (contract_id_id) REFERENCES public.app_contract(id) DEFERRABLE INITIALLY DEFERRED;
 h   ALTER TABLE ONLY public.app_event DROP CONSTRAINT app_event_contract_id_id_fcd9151c_fk_app_contract_id;
       public          postgres    false    3314    230    232                        2606    16767 I   app_event app_event_customer_id_id_11a8f188_fk_login_customer_user_ptr_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_event
    ADD CONSTRAINT app_event_customer_id_id_11a8f188_fk_login_customer_user_ptr_id FOREIGN KEY (customer_id_id) REFERENCES public.login_customer(user_ptr_id) DEFERRABLE INITIALLY DEFERRED;
 s   ALTER TABLE ONLY public.app_event DROP CONSTRAINT app_event_customer_id_id_11a8f188_fk_login_customer_user_ptr_id;
       public          postgres    false    232    3310    228            $           2606    16690 I   app_event_providers app_event_providers_event_id_035a130a_fk_app_event_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_event_providers
    ADD CONSTRAINT app_event_providers_event_id_035a130a_fk_app_event_id FOREIGN KEY (event_id) REFERENCES public.app_event(id) DEFERRABLE INITIALLY DEFERRED;
 s   ALTER TABLE ONLY public.app_event_providers DROP CONSTRAINT app_event_providers_event_id_035a130a_fk_app_event_id;
       public          postgres    false    232    238    3320            %           2606    16695 O   app_event_providers app_event_providers_provider_id_2f82d6fd_fk_app_provider_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_event_providers
    ADD CONSTRAINT app_event_providers_provider_id_2f82d6fd_fk_app_provider_id FOREIGN KEY (provider_id) REFERENCES public.app_provider(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.app_event_providers DROP CONSTRAINT app_event_providers_provider_id_2f82d6fd_fk_app_provider_id;
       public          postgres    false    238    3329    236            !           2606    16772 H   app_event app_event_support_id_id_7fec16a6_fk_login_employee_user_ptr_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_event
    ADD CONSTRAINT app_event_support_id_id_7fec16a6_fk_login_employee_user_ptr_id FOREIGN KEY (support_id_id) REFERENCES public.login_employee(user_ptr_id) DEFERRABLE INITIALLY DEFERRED;
 r   ALTER TABLE ONLY public.app_event DROP CONSTRAINT app_event_support_id_id_7fec16a6_fk_login_employee_user_ptr_id;
       public          postgres    false    232    3308    227            #           2606    16712 @   app_prospect app_prospect_sales_contact_id_a17c4f35_fk_login_emp    FK CONSTRAINT     �   ALTER TABLE ONLY public.app_prospect
    ADD CONSTRAINT app_prospect_sales_contact_id_a17c4f35_fk_login_emp FOREIGN KEY (sales_contact_id) REFERENCES public.login_employee(user_ptr_id) DEFERRABLE INITIALLY DEFERRED;
 j   ALTER TABLE ONLY public.app_prospect DROP CONSTRAINT app_prospect_sales_contact_id_a17c4f35_fk_login_emp;
       public          postgres    false    234    227    3308                       2606    16452 O   auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm;
       public          postgres    false    3270    214    218                       2606    16447 P   auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id;
       public          postgres    false    216    3275    218                       2606    16438 E   auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co;
       public          postgres    false    214    212    3265            &           2606    16808 A   authtoken_token authtoken_token_user_id_35299eff_fk_login_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.authtoken_token
    ADD CONSTRAINT authtoken_token_user_id_35299eff_fk_login_user_id FOREIGN KEY (user_id) REFERENCES public.login_user(id) DEFERRABLE INITIALLY DEFERRED;
 k   ALTER TABLE ONLY public.authtoken_token DROP CONSTRAINT authtoken_token_user_id_35299eff_fk_login_user_id;
       public          postgres    false    220    239    3286                       2606    16527 G   django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co;
       public          postgres    false    226    212    3265                       2606    16532 C   django_admin_log django_admin_log_user_id_c564eba6_fk_login_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_login_user_id FOREIGN KEY (user_id) REFERENCES public.login_user(id) DEFERRABLE INITIALLY DEFERRED;
 m   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_user_id_c564eba6_fk_login_user_id;
       public          postgres    false    226    220    3286                       2606    16599 D   login_customer login_customer_sales_contact_id_ce094e4c_fk_login_emp    FK CONSTRAINT     �   ALTER TABLE ONLY public.login_customer
    ADD CONSTRAINT login_customer_sales_contact_id_ce094e4c_fk_login_emp FOREIGN KEY (sales_contact_id) REFERENCES public.login_employee(user_ptr_id) DEFERRABLE INITIALLY DEFERRED;
 n   ALTER TABLE ONLY public.login_customer DROP CONSTRAINT login_customer_sales_contact_id_ce094e4c_fk_login_emp;
       public          postgres    false    227    228    3308                       2606    16562 C   login_customer login_customer_user_ptr_id_2a1f83ca_fk_login_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.login_customer
    ADD CONSTRAINT login_customer_user_ptr_id_2a1f83ca_fk_login_user_id FOREIGN KEY (user_ptr_id) REFERENCES public.login_user(id) DEFERRABLE INITIALLY DEFERRED;
 m   ALTER TABLE ONLY public.login_customer DROP CONSTRAINT login_customer_user_ptr_id_2a1f83ca_fk_login_user_id;
       public          postgres    false    228    3286    220                       2606    16585 >   login_employee login_employee_manager_id_c37ca2d8_fk_login_emp    FK CONSTRAINT     �   ALTER TABLE ONLY public.login_employee
    ADD CONSTRAINT login_employee_manager_id_c37ca2d8_fk_login_emp FOREIGN KEY (manager_id) REFERENCES public.login_employee(user_ptr_id) DEFERRABLE INITIALLY DEFERRED;
 h   ALTER TABLE ONLY public.login_employee DROP CONSTRAINT login_employee_manager_id_c37ca2d8_fk_login_emp;
       public          postgres    false    3308    227    227                       2606    16557 C   login_employee login_employee_user_ptr_id_0c527a54_fk_login_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.login_employee
    ADD CONSTRAINT login_employee_user_ptr_id_0c527a54_fk_login_user_id FOREIGN KEY (user_ptr_id) REFERENCES public.login_user(id) DEFERRABLE INITIALLY DEFERRED;
 m   ALTER TABLE ONLY public.login_employee DROP CONSTRAINT login_employee_user_ptr_id_0c527a54_fk_login_user_id;
       public          postgres    false    227    3286    220                       2606    16496 F   login_user_groups login_user_groups_group_id_a8810f0d_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.login_user_groups
    ADD CONSTRAINT login_user_groups_group_id_a8810f0d_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 p   ALTER TABLE ONLY public.login_user_groups DROP CONSTRAINT login_user_groups_group_id_a8810f0d_fk_auth_group_id;
       public          postgres    false    216    3275    222                       2606    16491 E   login_user_groups login_user_groups_user_id_f6fabf84_fk_login_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.login_user_groups
    ADD CONSTRAINT login_user_groups_user_id_f6fabf84_fk_login_user_id FOREIGN KEY (user_id) REFERENCES public.login_user(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.login_user_groups DROP CONSTRAINT login_user_groups_user_id_f6fabf84_fk_login_user_id;
       public          postgres    false    220    3286    222                       2606    16510 T   login_user_user_permissions login_user_user_perm_permission_id_08d04f9c_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.login_user_user_permissions
    ADD CONSTRAINT login_user_user_perm_permission_id_08d04f9c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 ~   ALTER TABLE ONLY public.login_user_user_permissions DROP CONSTRAINT login_user_user_perm_permission_id_08d04f9c_fk_auth_perm;
       public          postgres    false    224    214    3270                       2606    16505 Y   login_user_user_permissions login_user_user_permissions_user_id_2a4ce843_fk_login_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.login_user_user_permissions
    ADD CONSTRAINT login_user_user_permissions_user_id_2a4ce843_fk_login_user_id FOREIGN KEY (user_id) REFERENCES public.login_user(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.login_user_user_permissions DROP CONSTRAINT login_user_user_permissions_user_id_2a4ce843_fk_login_user_id;
       public          postgres    false    224    3286    220            �   �   x�3���T0200�45 �i`��/�$#3/�5202�50�50Bfr�%ӸL8�\�C<������5[r����r��:��)�F�s��� j�g������7�T�!Q��9��38�(5/1%U���ʲ���"N�}a��� ��%��P�Y�e������W��ܔH��P�1z\\\ �7aK      �   B   x�3��R0202������t�t��������\F���
^�ye��E��qZ���qqq |�      �   .   x�ƹ 0����<Ÿ�:|�JnnK�$es-�%=h�9�|�'�      �   �   x�3�t*�L�/J�M�L�@L���\Nmcc3KsKsKN###]3]#df��q:^������RZ��W�e��T����ϙ�%&�8$��`S��MAf�X��6�h�GjQ�ᕜ>��y���\1z\\\ �_/X      �   b  x�e��n�@���Sp롉\nh���J�����t��W��5|� 
5������gfL��#��E"D2+yT��Td}I�D2����c��:�	�m���p�Y�P���:��'�=��e�
å6��S��vY����z�s��'��A��W��)�"�����;͆W��P��w5h�����6��`�Q�F��+[�C-a޸�q=Ӏ�p��������[�e���3Ɖ�Y�Hj���B(�HGޜ�����cҀ�iz�ֺI��'��$A�oFv�4����\�ʢ	\p�U)`���V�쌶�z��o���׊b�%&U�pj��؊��4C�.��ϊ\��b`1���`�-�c�i����f      �      x������ � �      �      x������ � �      �   -  x�]�ݮ�@��c�
��P�wz=l��XSh��w1�~��ٞ�1y���*_�~w�^w�ᶋ�2}��T��/�H벪��.���-z��ж�^�#.���vɾ�����V�qz���>�EاL�!x�Po����zα���z�z���6��U�Mz\c�
N�N�	j�II��j�e������P� �[��v���\�?q���'8��h�[���>i���R8/�*�1��� g�-X�3d��c�I4�kY�؍�
n�fE��!Q�Z�t,�yk%�4��	
n0�a�H7*��e���D�$��8�uָ�oz��@�s7B8�	̀����m�?����t��"�;���;�H�
(v�����׼��;�|�Zw���`u'�L�Q8��(��Η�'�A�5�f{}����i��7�����@�,���7�E�҂�P!/��;���f���W�_(;�4����׿�	���N~���	@*�QFa��'c-��Wz�M-�iM����B��M�R+zt�
�0���ʲ���ת      �   J   x���� �O�>�lcfI�����A�������19��_�,Y��4�������D��?      �   �  x����n�@���SX�p��vf�پ�@AU�F���x��J��PP��Ux��c����Z��-�7�o�or��3�1�!�@�ӗ#�l�)��\D]�M+�.�f����p뼦��t�*��}����xzRTu{�q�ՙ��ⲱM[O���#�#�`Ђ�L�u�CG뭫�s~��K�vu�(}c���@|�1S����o��m�b�fuG8X��z��O�7D�!]d\1�A���ID�x[�����j���q���dt[���n�۲j���p%h�Zup�:�]���^	��j�A$���� }����h��2�Ϛm�ϖ��D�IұE�r���Le���b)H�GХ�$0C��bu^�$�i��Lh���Ov�0�Ġ��R��bt\����0{Rg��� �
^��]9�E !YjRaĠщ����(!(��B2x��V��ŷv\�0,�d 	d���i�n��	V�2�4Cp��z�E'���1F�xb(d�zH�Qo׶��*��h��(.4�L2@&�I�~=����@�?��&GQ�PB3E�V��"ǟъ~�ۺ���ގmE?�Q����n?I��������:~���ntt����F�כ�l�����R�rzY�3(�C���w����nʍ��Xz�V�1�iW$��2}�8��1q������_V��:_�d2���i      �   �   x�]�K�0��a*��w�nX4*��8�r�����(���Lsw�|t�sZ+����R�#`���ĳ 6��m:�B���JI�`[ڙ_]9���$~�ߗ��lf�x݉�L�����I?k�͘�HqH]���
�bF��l�
m������8�wXU�      �   �  x���ݎ�8���O����\�?�gY	�ēF�1�5y�1�e�H"�Ԋ"��\�:ذ;������ڙ~���:WCU�;d�?����P����������XXӴߦ?�/Źl�"
�L�(�+/����A!����-:c������X4埢6���E�D������һӔU��"C7T��9e����Я �&r���~(��T��]��(䌏�,B�{�/����?�bl�
C(���G��|�uu,���Ey<�������dV��2��,���<�F�~m ��?t�5��{H(`u���{�q��c�s�K�Zd�ζ�3;��'���s zp����}uY9P���;��(�@�r�q�=6/i�C�T�N���e�4�n9��e�f��'�h��0����.O�᫭+.C-��V������C�t��:�p�bM���A��cѴv9�8B6M�D��/k7I�X�B���ɽ�ZP�˛����O����3b�����m㾸�}.���۫1ty��K7u��Yŀ't?�å��.���)a��R*��(�-t�4��ŋ����]��޽K��<n6�}/�] 	Mu��W�����:"bм�Pq9YB�{��#�p�f̦\�T>�x� ����x��'f�M
�H�4 _��!��΅Vޯ<M�����O�]�w�VN��3^!H��
.9�i+$IA�v3.
湰LQ�r�T��k��Y��Eu���!ʩpM �����Ngs��1��H��X�'m�	�\%܄_VPwrR���\!��,En*I���nfT� ��DxhHu|�	�ҿZ
��iR�w�3���45�zZ)y7FFl�JlL >�YمF�����V����ߕr��(�M��T,�1PH��Sa	�4r�pE�"�Ѡ�>v��Z��l�f\��[�W��]�xI��-�v� ��#�ؐ�G��j 3#�!M��������܈���'{#��O3@k&�,��~�Z�bڸJ26��9ۚ�i��̍�-@�@fFy��-u��OnEu�v����Ʈ�A��ɮ�7sf�Eۏ;�M'Y5�����<��T,���V��y�l:�*@�(XD����^���d�"�9^���16��^�;���&��.9w{�P��~�o�?�2�K��#��������#A      �   �  x���I��H @�u�)z߲D�m<`lc��,0�<�ɧ���^�Ju������ȋ� �SL�8~�9�[4eSQ&����5S}Jŋ>$�l�GI��ݷ�5����[@?8���r����n܁������@~�7c��ӝ�n����5��}�}�+�R�E�QU��,2g�IRu�������;���V�e»�q�MrQ-�ց΋��ʄ�R�t/s��z�}��Sz��l�ݩ���� fzظ? �p���_  ZcY���]z��q�a(2�~=� em�mT�/���	E�^��ֲ�9�O�%�ΜK�ދ���8Uu"w�a�ª���^��[S,N��A���	�����l�x�.7�(�*o�tit�'4M���!�x�jh�ij�Cs*�tM���=y�dG1y*w~5��*����P�C�W&rZ��2F�V�[,�iZ��0�������F�2�k!��Q����U�^]�ǽ��4,b2q]6��%Q�������p�Afo辢�V쨯w�5���l�߈8���F��%�4���u��a��w8}Z/���B�^��KeYp���e�=�yׂ�Qd���qzR�rri�Ma�5&�����	���Ea��Ir�&<�� �}T5�K�S@	�\||�=���      �   =   x���t�)H-6200����4�24�tLI�LI,�4202�50�50�rzz�:B��qqq ��o      �   3   x�3�t-�Lv-K�+)���2G�q��r-�T�!�-��QU�������� �!f      �   �  x���Y��H���_1ޙ��b7��h��6��L�M@6Y\���v�[��C��^�z�_� �{@���)zH�������U}�@r�VBA��DJ����w?zy�x/�ʁ�%ؼ���zn�\�SRt�����t\T\jvٓ�t��djZĨ7V��T3�rK���*�[�:��}�P�=>	��_V��O�1���<RFqu������N0�é.�5 �K�I��g�f���0~�v��H�g
��CZ�廭�ͥ#%k�II���������n��M�0�s��(С)�TYK�˷ �,����r�4n@����h��/Q�X2�����l������u���v��r�o�fO�R��7�y�\�����.�Lq��c��'B�/��`"���~�[�ɲ �F���Q7��!N���s��p��:ϳ�j�AV�_�Hދ-6���bMB4��6<^�� ̌^�:H;��p|i,'�j��_�N�ڣ���z�ς�� 9L3Tu����o�#/�"��^����"-�AT|��E��Qq�=�&�AVTe��z�B�����.j�Y9����a��O+g�$O�[ qB��y͐���Q�{0�p�`n]�K�γ��E�	��u*�l�3$�4�����D�o{��tE�VR:���
xE���~���&�hz`�21sǙ��L7��!IwL����8ƃ��g�i7�I��ob!$�3�&U�4�v��s�����a���))o'��S*Չj�1�L��k�����$�7��W��,H?�l�v�V��]�:�J���f�$2����Ͱ�L�J���F�`$	��z&A~*�f��2܏�F���݂"�!NH��ŴnwH��Ӽ�ǜ��T�(ν�[���I>�	Ϝ�6���������z�����=xh�Y���e�FQ1}�!76���*9S������ưK�oh�B�7p�n����RFE�vr�G�m�����*l46�õ����H�Ʉҵ���%:i"f��7��O�K���'�#��+J}P\;��wN�B��$j?V����۲UJ��,۵�c���k_J��h'v��7R>�>���X�
����L_�ω�i5V����T�&غ�	(ޡ�UބKQf�A#/�!$M}���������      �      x������ � �      �      x������ � �     