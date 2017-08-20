CREATE TABLE crimedata (
	id DECIMAL NOT NULL, 
	record_id DECIMAL NOT NULL, 
	report_date DATE NOT NULL, 
	report_time DATETIME NOT NULL, 
	major_offense_type VARCHAR(23) NOT NULL, 
	address VARCHAR(70) NOT NULL, 
	neighborhood VARCHAR(25), 
	police_precinct VARCHAR(25), 
	police_district VARCHAR(3), 
	xcoordinate DECIMAL, 
	ycoordinate DECIMAL
);
