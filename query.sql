-- Helper SQL for language detection

-- Query 1: Most Common Animal Types
SELECT animal_type, COUNT(*) AS total
FROM pets
GROUP BY animal_type
ORDER BY total DESC;

-- Query 2: Average Age of Pets by Animal Type
SELECT animal_type, ROUND(AVG(age), 2) AS average_age
FROM pets
GROUP BY animal_type
ORDER BY average_age DESC;

-- Query 3: Number of Pets per Owneer
SELECT o.name AS owner_name, COUNT(p.pet_id) AS total_pets
FROM owners o
LEFT JOIN pets p ON o.id = p.owners_id
GROUP BY o.name
ORDER BY total_pets DESC;

-- Query 4: License Status Distribution of Pet Owners
SELECT license_status, COUNT(*) AS total
FROM owners
GROUP BY license_status;

-- Query 5: Finding All Pets Belonging to a Specific Owner (e.g. Willand)
SELECT pet_id, 
       pet_name,
       animal_type
FROM pets
WHERE owners_id = 'X002';