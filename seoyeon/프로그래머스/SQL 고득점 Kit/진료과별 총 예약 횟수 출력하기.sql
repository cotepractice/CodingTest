SELECT MCDP_CD as "진료과코드", count(*) as "5월예약건수"
FROM appointment as a
WHERE date_format(a.APNT_YMD,"%Y-%m")="2022-05"
GROUP BY MCDP_CD
ORDER BY count(*) ASC, MCDP_CD ASC