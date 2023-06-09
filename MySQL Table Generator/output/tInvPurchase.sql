CREATE TABLE tInvPurchase(
                PurchaseDate DATE NULL
                , SupplierCode VARCHAR (100) NULL
                , SupplierName VARCHAR (300) NULL
                , InvoiceDate DATE NULL
                , Invno VARCHAR (100) NULL
                , DCNo VARCHAR (100) NULL
                , Type VARCHAR (100) NULL
                , Category VARCHAR (100) NULL
                , ItemCode VARCHAR (100) NULL
                , Item VARCHAR (300) NULL
                , LotNo VARCHAR (100) NULL
                , ReceiveSite VARCHAR (50) NULL
                , StorageLocation VARCHAR (50) NULL
                , InvoiceQty INT NULL
                , NoofBags INT NULL
                , Weightslipweight INT NULL
                , ManualWeight INT NULL
                , Rateperkg FLOAT NULL
                , GST18 FLOAT NULL
                , TotalValue FLOAT NULL
                , MFI VARCHAR (100) NULL
                , Filler VARCHAR (100) NULL
                , Impact VARCHAR (100) NULL
    );