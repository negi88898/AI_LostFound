USE AILostFound;

CREATE TABLE IF NOT EXISTS Items (
  ItemID INT PRIMARY KEY AUTO_INCREMENT,
  Name VARCHAR(100),
  Category VARCHAR(50),
  Description TEXT,
  DateFound DATE,
  Status VARCHAR(20)
);
-- Table for Lost Items
CREATE TABLE IF NOT EXISTS LostItems (
  LostID INT PRIMARY KEY AUTO_INCREMENT,
  OwnerName VARCHAR(100),
  Contact VARCHAR(50),
  ItemName VARCHAR(100),
  Category VARCHAR(50),
  Description TEXT
);

-- Table for AI Suggestions
CREATE TABLE IF NOT EXISTS AISuggestions (
  SuggestionID INT PRIMARY KEY AUTO_INCREMENT,
  ItemID INT,
  SuggestedOwner VARCHAR(100),
  ConfidenceScore DECIMAL(5,2),
  FOREIGN KEY (ItemID) REFERENCES Items(ItemID)
);
USE AILostFound;

DROP TABLE IF EXISTS LostItems;

CREATE TABLE LostItems (
  LostID INT PRIMARY KEY AUTO_INCREMENT,
  OwnerName VARCHAR(100),
  Contact VARCHAR(50),
  ItemName VARCHAR(100),
  Category VARCHAR(50),
  Description TEXT
);


