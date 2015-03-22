/*
  VerseBot for reddit
  By Matthieu Grieger
  update_old_translation_table.sql
  Copyright (c) 2015 Matthieu Grieger (MIT License)
*/

ALTER TABLE translation_stats ALTER COLUMN name TYPE TEXT;
ALTER TABLE translation_stats ALTER COLUMN trans TYPE TEXT;
ALTER TABLE translation_stats ALTER COLUMN lang TYPE TEXT;

ALTER TABLE translation_stats ADD COLUMN has_ot BOOLEAN DEFAULT TRUE;
ALTER TABLE translation_stats ADD COLUMN has_nt BOOLEAN DEFAULT TRUE;
ALTER TABLE translation_stats ADD COLUMN has_deut BOOLEAN DEFAULT FALSE;

ALTER TABLE translation_stats DISABLE TRIGGER update_translation_stats_timestamp;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = AMU;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = ERV-BG;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = CCO;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = APSD-CEB;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = CHR;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = CKW;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = SNC;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = HOF;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = NGU-DE;
UPDATE translation_stats SET has_deut = TRUE WHERE trans = CEB;
UPDATE translation_stats SET has_deut = TRUE WHERE trans = DRA;
UPDATE translation_stats SET has_deut = TRUE WHERE trans = GNT;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = PHILLIPS;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = MOUNCE;
UPDATE translation_stats SET has_deut = TRUE WHERE trans = NRSV;
UPDATE translation_stats SET has_deut = TRUE WHERE trans = NRSVA;
UPDATE translation_stats SET has_deut = TRUE WHERE trans = RSV;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = WE;
UPDATE translation_stats SET has_deut = TRUE WHERE trans = DHH;
UPDATE translation_stats SET has_deut = TRUE WHERE trans = TLA;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = TR1550;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = WHNU;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = TR1894;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = SBLGNT;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = HHH;
UPDATE translation_stats SET has_nt = FALSE WHERE trans = WLC;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = CRO;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = HWP;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = BDG;
UPDATE translation_stats SET has_deut = TRUE WHERE trans = CEI;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = JAC;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = KEK;
UPDATE translation_stats SET has_deut = TRUE WHERE trans = VULGATE;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = MNT;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = MVC;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = MVJ;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = REIMER;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = NGU;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = LB;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = NP;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = SZ-PL;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = NBTN;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = VFL;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = MTDS;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = QUT;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = ERV-RU;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = NPK;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = ERV-SR;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = SNT;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = ERV-TH;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = SND;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = NA-TWI;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = ERV-UK;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = USP;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = ERV-ZH;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = CSBS;
UPDATE translation_stats SET has_ot = FALSE WHERE trans = CSBT;
ALTER TABLE translation_stats ENABLE TRIGGER update_translation_stats_timestamp;
