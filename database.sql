CREATE DATABASE AILostFound;
select database AILostFound;
USE AILostFound;

CREATE TABLE Items (
  ItemID INT PRIMARY KEY AUTO_INCREMENT,
  Name VARCHAR(100),
  Category VARCHAR(50),
  Description TEXT,
  DateFound DATE,
  Status VARCHAR(20)
);

CREATE TABLE Owners (
  OwnerID INT PRIMARY KEY AUTO_INCREMENT,
  Name VARCHAR(100),
  Contact VARCHAR(50),
  Email VARCHAR(100)
);

CREATE TABLE AISuggestions (
  SuggestionID INT PRIMARY KEY AUTO_INCREMENT,
  ItemID INT,
  SuggestedOwner VARCHAR(100),
  ConfidenceScore DECIMAL(5,2),
  FOREIGN KEY (ItemID) REFERENCES Items(ItemID)
);
CREATE TABLE LostItems (
  LostID INT PRIMARY KEY AUTO_INCREMENT,
  Name VARCHAR(100),
  Category VARCHAR(50),
  Description TEXT,
  ReportedBy VARCHAR(100)
);
ALTER TABLE LostItems 
ADD COLUMN OwnerName VARCHAR(100),
ADD COLUMN Contact VARCHAR(100);

