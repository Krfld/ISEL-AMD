\set dataBase fpa_db
;
\set userName postgres
;
\connect :dataBase :userName
;

DROP TABLE IF EXISTS TREATS;
DROP TABLE IF EXISTS DOCTOR;
DROP TABLE IF EXISTS PATIENT;
DROP TABLE IF EXISTS DISEASE;
DROP TABLE IF EXISTS DIAGNOSTIC;

---------
-- DOCTOR
---------

CREATE TABLE DOCTOR
(
	cc			VARCHAR( 8 )	NOT NULL	PRIMARY KEY,
	name		VARCHAR( 50 )	NOT NULL,
	birthDate	DATE			NOT NULL
);

----------
-- PATIENT
----------

CREATE TABLE PATIENT
(
	cc			VARCHAR( 8 )	NOT NULL	PRIMARY KEY,
	name		VARCHAR( 50 )	NOT NULL,
	birthDate	DATE			NOT NULL
);

----------
-- DISEASE
----------

CREATE TABLE DISEASE
(
	id				INT			NOT NULL	PRIMARY KEY,
	isMyope			BOOLEAN		NOT NULL,
	isAstigmatic	BOOLEAN		NOT NULL,
	isHypermetrope	BOOLEAN		NOT NULL
);

-------------
-- DIAGNOSTIC
-------------

CREATE TABLE DIAGNOSTIC
(
	id			INT				NOT NULL	PRIMARY KEY,
	age			VARCHAR( 20 )	NOT NULL,
	tearRate	VARCHAR( 20 )	NOT NULL
);

---------
-- TREATS
---------

CREATE TABLE TREATS
(
	prescriptionDate	DATE			NOT NULL,
	prescribedLenses	VARCHAR( 20 )	NOT NULL,
	diseaseId			INT				NOT NULL,
	diagnosticId		INT				NOT NULL,
	ccDoctor			VARCHAR( 8 )	NOT NULL,
	ccPatient			VARCHAR( 8 )	NOT NULL,
	
	PRIMARY KEY( prescriptionDate, diseaseId, diagnosticId, ccDoctor, ccPatient ),
	
	CONSTRAINT constraintDiseaseId		FOREIGN KEY( diseaseId )		REFERENCES DISEASE( id ),
	CONSTRAINT constraintDiagnosticId	FOREIGN KEY( diagnosticId )		REFERENCES DIAGNOSTIC( id ),
	CONSTRAINT constraintCcDoctor		FOREIGN KEY( ccDoctor )			REFERENCES DOCTOR( cc ),
	CONSTRAINT constraintCcPatient		FOREIGN KEY( ccPatient )		REFERENCES PATIENT( cc )
);
