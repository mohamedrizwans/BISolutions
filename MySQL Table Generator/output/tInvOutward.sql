CREATE TABLE tInvOutward(
                EntryDate DATE NULL
                , FromSite VARCHAR (100) NOT NULL
                , FromSiteDC VARCHAR (100) NULL
                , TOSite VARCHAR (100) NULL
                , TOSiteDC VARCHAR (100) NULL
                , Category VARCHAR (100) NULL
                , ItemCode VARCHAR (100) NOT NULL
                , Item VARCHAR (300) NULL
                , BatchNo VARCHAR (100) NOT NULL
                , ProdGrade VARCHAR (100) NULL
                , ProdName VARCHAR (100) NULL
                , Qty INT NULL
                , Type VARCHAR (100) NULL
                , ConverttoFG VARCHAR (100) NULL
                , FGCode VARCHAR (100) NULL
    );