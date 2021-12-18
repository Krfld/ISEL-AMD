----------
-- DB name
----------

\set dataBase fpa_db
;

------------
-- Remode DB
------------

\echo "Remove Data Base" :dataBase
;

DROP DATABASE IF EXISTS :dataBase
;

------------
-- Create DB
------------

\echo "Create Data Base" :dataBase
;

CREATE DATABASE :dataBase
;
