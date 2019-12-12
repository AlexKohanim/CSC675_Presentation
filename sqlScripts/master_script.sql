CREATE Database delership;
USE delership;

CREATE TABLE `Cars` (
  `Inventory` int NOT NULL,
  `Cid` int NOT NULL AUTO_INCREMENT,
  `Model` varchar(45) NOT NULL,
  `MSRP` int NOT NULL,
  `Year` int NOT NULL,
  PRIMARY KEY (`Cid`),
  UNIQUE KEY `Model_UNIQUE` (`Model`)
);


CREATE TABLE `Customers` (
  `Pid` int NOT NULL AUTO_INCREMENT,
  `Phone` varchar(45) NOT NULL,
  `Email` varchar(128) NOT NULL,
  `Name` varchar(45) NOT NULL,
  PRIMARY KEY (`Pid`)
); 


CREATE TABLE `Employees` (
  `Eid` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) NOT NULL,
  `NumSales` int NOT NULL,
  `Salary` int DEFAULT NULL,
  PRIMARY KEY (`Eid`)
); 


CREATE TABLE `Sales` (
  `Sid` int NOT NULL AUTO_INCREMENT,
  `Cid` int NOT NULL,
  `Pid` int NOT NULL,
  `SalePrice` int NOT NULL,
  `Eid` int NOT NULL,
  PRIMARY KEY (`Sid`),
  KEY `Pid_idx` (`Pid`),
  KEY `Cid_idx` (`Cid`),
  KEY `Eid_idx` (`Eid`),
  CONSTRAINT `Cid` FOREIGN KEY (`Cid`) REFERENCES `Cars` (`Cid`) ON DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `Eid` FOREIGN KEY (`Eid`) REFERENCES `Employees` (`Eid`) ON
DELETE NO ACTION ON UPDATE CASCADE,
  CONSTRAINT `Pid` FOREIGN KEY (`Pid`) REFERENCES `Customers` (`Pid`) ON
DELETE CASCADE ON UPDATE CASCADE
) ;
CREATE INDEX `idx_Eid` ON `Employees` (Eid);
CREATE INDEX `idx_Sid` ON `Sales` (Sid);