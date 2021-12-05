\set dataBase fpa_db
;
\set userName postgres
;
\connect :dataBase :userName
;

-------------
-- Export tab
-------------

\set filePath 'fpa_dataset.tab'
\o :filePath

COPY
(
	SELECT
		age,
		tearRate AS tear_rate,
		isMyope,
		isAstigmatic,
		isHypermetrope,
		prescribedLenses AS lenses
	FROM fpa_3RowHeader
)
TO STDOUT
WITH ( FORMAT CSV, HEADER TRUE, DELIMITER E'\t' )
;

-------------
-- Export csv
-------------

\set filePath 'fpa_dataset.csv'
\o :filePath

COPY
(
	SELECT
		age,
		tearRate AS tear_rate,
		CAST(isMyope AS VARCHAR),
		CAST(isAstigmatic AS VARCHAR),
		CAST(isHypermetrope AS VARCHAR),
		prescribedLenses AS lenses
	FROM fpa_view
)
TO STDOUT
WITH ( FORMAT CSV )
;

--\o :STDOUT