SELECT p.pt_name, p.pt_no, p.gend_cd, p.age, IFNULL(p.tlno,"NONE")
FROM patient as p
WHERE p.age <= 12 and p.gend_cd = "W"
ORDER BY p.age DESC, p.pt_name ASC