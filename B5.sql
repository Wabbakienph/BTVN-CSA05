CREATE TABLE Product (
    ID INT,
    Name VARCHAR(500),
    Type VARCHAR(500),
    Price FLOAT,
    DateOfManufacture DATE,
    DateOfExpiry DATE
);

CREATE TABLE Manufacturer (
    ID INT,
    Name VARCHAR(500),
    Country VARCHAR(500)
);

CREATE TABLE Store (
    ID INT,
    Name VARCHAR(500),
    Address VARCHAR(500)
);

INSERT INTO Product (ID, Name, Type, Price, DateOfManufacture, DateOfExpiry)
VALUES
(1, 'Toilet1', 'Toilet', 1.1, '2022-01-01', '2032-01-01'),
(2, 'Toilet2', 'Toilet', 1.1, '2022-02-02', '2032-02-02'),
(3, 'Toilet3', 'Toilet', 1.1, '2022-03-03', '2032-03-03'),
(4, 'Toilet1', 'Toilet', 1.1, '2022-04-04', '2032-04-04'),
(5, 'Toilet1', 'Toilet', 1.1, '2022-05-05', '2032-05-05'),
(6, 'Toilet1', 'Toilet', 1.1, '2022-06-06', '2032-06-06'),
(7, 'Toilet1', 'Toilet', 1.1, '2022-07-07', '2032-07-07'),
(8, 'Toilet1', 'Toilet', 1.1, '2022-08-08', '2032-08-08'),
(9, 'Toilet1', 'Toilet', 1.1, '2022-09-09', '2032-09-09'),
(10,'Toilet1', 'Toilet', 1.1, '2022-10-10', '2032-10-10');

INSERT INTO Manufacturer (ID, Name, Country)
VALUES 
(1, 'Toilet1', 'Japan'),
(2, 'Toilet2', 'Japan'),
(3, 'Toilet3', 'Japan'),
(4, 'Toilet4', 'Japan'),
(5, 'Toilet5', 'Japan'),
(6, 'Toilet6', 'Japan'),
(7, 'Toilet7', 'Japan'),
(8, 'Toilet8', 'Japan'),
(9, 'Toilet9', 'Japan'),
(10, 'Toilet10', 'Japan');

INSERT INTO Store (ID, Name, Address)
VALUES
(1, 'Toilet1', 'Tokyo'),
(2, 'Toilet2', 'Tokyo'),
(3, 'Toilet3', 'Tokyo'),
(4, 'Toilet4', 'Tokyo'),
(5, 'Toilet5', 'Tokyo'),
(6, 'Toilet6', 'Tokyo'),
(7, 'Toilet7', 'Tokyo'),
(8, 'Toilet8', 'Tokyo'),
(9, 'Toilet9', 'Tokyo'),
(10, 'Toilet10', 'Tokyo');