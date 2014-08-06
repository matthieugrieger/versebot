CREATE TABLE translation_stats (id SERIAL PRIMARY KEY, trans VARCHAR(20), count INTEGER DEFAULT 0, last_used TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT NOW());

INSERT INTO translation_stats (trans) VALUES ('AMU'), ('ERV-AR'), ('ALAB'), ('ERV-AWA'), ('BG1940'),
	('BULG'), ('ERV-BG'), ('BPB'), ('CCO'), ('APSD-CEB'), ('CHR'), ('CKW'), ('B21'), ('SNC'), ('BPH'),
	('DN1933'), ('HOF'), ('LUTH1545'), ('NGU-DE'), ('SCH1951'), ('SCH2000'), ('KJ21'), ('ASV'), ('AMP'),
	('CEB'), ('CJB'), ('CEV'), ('DARBY'), ('DRA'), ('ERV'), ('ESV'), ('ESVUK'), ('EXB'), ('GNV'), ('GW'),
	('GNT'), ('HCSB'), ('PHILLIPS'), ('JUB'), ('KJV'), ('AKJV'), ('LEB'), ('TLB'), ('MSG'), ('MOUNCE'),
	('NOG'), ('NASB'), ('NCV'), ('NET Bible'), ('NIRV'), ('NIV'), ('NIVUK'), ('NKJV'), ('NLV'), ('NLT'),
	('NRSV'), ('NRSVA'), ('NRSVACE'), ('NRSVCE'), ('OJB'), ('RSV'), ('RSVCE'), ('VOICE'), ('WEB'), ('WE'),
	('WYC'), ('YLT'), ('LBLA'), ('DHH'), ('JBS'), ('NBLH'), ('NTV'), ('CST'), ('NVI'), ('PDT'), ('BLP'),
	('BLPH'), ('RVC'), ('RVR1960'), ('RVR1977'), ('RVR1995'), ('RVA'), ('TLA'), ('R1933'), ('BDS'), ('LSG'),
	('NEG1979'), ('SG21'), ('TR1550'), ('WHNU'), ('TR1894'), ('SBLGNT'), ('HHH'), ('WLC'), ('ERV-HI'), ('HLGN'),
	('CRO'), ('HCV'), ('KAR'), ('ERV-HU'), ('NT-HU'), ('HWP'), ('ICELAND'), ('BDG'), ('CEI'), ('LND'), ('NR1994'),
	('NR2006'), ('JAC'), ('KEK'), ('VULGATE'), ('MAORI'), ('MNT'), ('ERV-MR'), ('MVC'), ('MVJ'), ('REIMER'), ('ERV-NE'),
	('NGU'), ('HTB'), ('DNB1930'), ('LB'), ('ERV-OR'), ('ERV-PA'), ('NP'), ('SZ-PL'), ('NBTN'), ('AA'), ('NVI-PT'),
	('OL'), ('VFL'), ('MTDS'), ('QUT'), ('RMNN'), ('NTLR'), ('ERV-RU'), ('RUSV'), ('SZ'), ('NPK'), ('SOM'), ('ALB'),
	('ERV-SR'), ('SVL'), ('SV1917'), ('SFB'), ('SNT'), ('ERV-TA'), ('TNCV'), ('ERV-TH'), ('SND'), ('NA-TWI'), ('UKR'),
	('ERV-UK'), ('ERV-UR'), ('USP'), ('VIET'), ('BD2011'), ('BPT'), ('CCB'), ('ERV-ZH'), ('CNVT'), ('CSBS'), ('CSBT'),
	('CUVS'), ('CUV'), ('CUVMPS'), ('CUVMPT'), ('NJPS');
	
CREATE TRIGGER update_translation_stats_timestamp BEFORE UPDATE
    ON translation_stats FOR EACH ROW EXECUTE PROCEDURE 
    update_timestamp_column();
