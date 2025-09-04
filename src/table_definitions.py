from sqlalchemy import Column, Integer, DateTime, String, Numeric, Date, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Clients(Base):
    __tablename__ = 'CabFileAPClients'
    id = Column(Integer, primary_key=True)
    uploadDate = Column(Date, nullable=False, server_default=func.curdate(), index=True)

    txtActionCode = Column(String(1))
    txtClientId = Column(String(20))
    txtHPhone = Column(String(13))
    txtLangCode = Column(String(1))
    txtClientSName = Column(String(16))
    txtResCode = Column(String(2))
    txtBPhone = Column(String(13))
    txtOccupation = Column(String(10))
    txtRRCode = Column(String(4))
    txtNetWorth = Column(String(5))
    txtInvObjCode1 = Column(String(4))
    txtInvObjCode2 = Column(String(4))
    txtInvObjCode3 = Column(String(4))
    txtInvObjCode4 = Column(String(4))
    txtInvObjCode5 = Column(String(4))
    txtInvObjCode6 = Column(String(4))
    lngSIN = Column(Integer)
    dteBirthDate = Column(Integer)
    txtGenderCode = Column(String(1))
    txtIncome = Column(String(5))
    txtNALine1 = Column(String(32))
    txtNALine2 = Column(String(32))
    txtNALine3 = Column(String(32))
    txtNALine4 = Column(String(32))
    txtNALine5 = Column(String(32))
    txtNALine6 = Column(String(32))
    txtNALine7 = Column(String(32))
    txtNALine8 = Column(String(32))
    txtPostalCode = Column(String(9))
    txtRiskTolerance = Column(String(20))


class Acclts(Base):
    __tablename__ = 'CabFileAPAcclts'
    id = Column(Integer, primary_key=True)
    uploadDate = Column(Date, nullable=False, server_default=func.curdate(), index=True)

    txtClientId = Column(String(20))
    txtAcctNo = Column(String(7))


class Accts(Base):
    __tablename__ = 'CabFileAPAccts'
    id = Column(Integer, primary_key=True)
    uploadDate = Column(Date, nullable=False, server_default=func.curdate(), index=True)
    txtAcctNo = Column(String(7))
    txtAcctType = Column(String(3))
    txtAcctCur = Column(String(3))
    txtAcctRR = Column(String(4))
    txtAcctSName = Column(String(16))
    txtPlanningCode = Column(String(2))
    txtAccountServiceCode = Column(String(12))
    txtEmployerGroupCode = Column(String(4))
    dteCloseDate = Column(Integer)


class Actpln(Base):
    __tablename__ = 'CabFileAPActpln'
    id = Column(Integer, primary_key=True)
    uploadDate = Column(Date, nullable=False, server_default=func.curdate(), index=True)
    txtAcctNo = Column(String(7))
    txtPensionOrigin = Column(String(2))


class Externid(Base):
    __tablename__ = 'CabFileAPExternid'
    id = Column(Integer, primary_key=True)
    uploadDate = Column(Date, nullable=False, server_default=func.curdate(), index=True)
    txtAcctNo = Column(String(7))
    txtExtrnSys = Column(String(8))
    txtExtrnSubSys = Column(String(8))
    txtExtrnId = Column(String(26))


class Payments(Base):
    __tablename__ = 'CabFileAPIPayments'
    id = Column(Integer, primary_key=True)
    uploadDate = Column(Date, nullable=False, server_default=func.curdate(), index=True)
    txtAcctNo = Column(String(7))
    txtInstitution = Column(Integer)
    txtBankBranch = Column(Integer)
    txtBankAcctNo = Column(Integer)
    txtPaymentId = Column(String(2))


class Posdt(Base):
    __tablename__ = 'CabFileTPosdt'
    id = Column(Integer, primary_key=True)
    uploadDate = Column(Date, nullable=False, server_default=func.curdate(), index=True)
    intSeqNo = Column(Integer)
    txtAcctNo = Column(String(7))
    txtSecId = Column(String(6))
    dteValueDate = Column(Integer)
    dteProcessDate = Column(Integer)
    dteTradeDate = Column(Integer)
    booQtyValid = Column(Integer)
    booAmtValid = Column(Integer)
    booTradeItem = Column(Integer)
    booExchItem = Column(Integer)
    booRevItem = Column(Integer)
    txtEntryType = Column(String(9))
    txtEntryDesc = Column(String(25))
    intQuantity = Column(Numeric(15, 0))
    dblNetAmt = Column(Numeric(17, 2))
    dblPrice = Column(Numeric(17, 8))
    txtCur = Column(String(2))
    txtBVtoMV = Column(String(1))


class Posli(Base):
    __tablename__ = 'CabFileTPosli'
    id = Column(Integer, primary_key=True)
    uploadDate = Column(Date, nullable=False, server_default=func.curdate(), index=True)
    intSeqNo = Column(Integer)
    dteProcessDate = Column(Integer)
    txtLIType = Column(String(2))
    txtLICur = Column(String(2))
    dblLIAmt = Column(Numeric(17, 2))


class Postd(Base):
    __tablename__ = 'CabFileTPostd'
    id = Column(Integer, primary_key=True)
    uploadDate = Column(Date, nullable=False, server_default=func.curdate(), index=True)
    intSeqNo = Column(Integer)
    dteProcessDate = Column(Integer)
    txtMarket = Column(String(2))
    dblFXRate = Column(Numeric(9, 5))
    booCxlTrade = Column(Integer)
    booBuySell = Column(Integer)
    booMultiFill = Column(Integer)
    booEmpDiscount = Column(Integer)
    booQSSPCoverage = Column(Integer)
    txtRRCode = Column(String(4))
    txtTradeBasis = Column(String(1))
    txtTradeNumber = Column(String(6))
    txtSpecialTaxCode = Column(String(1))
    txtBCFeeCode = Column(String(1))
    txtSubmittingLoc = Column(String(1))
    txtInventoryCode = Column(String(1))
    txtAccountNumber = Column(String(7))
    txtFundsOfPrice = Column(String(1))
    txtTradeCode = Column(String(1))
    txtOrigTradeAcct = Column(String(10))


class Multfill(Base):
    __tablename__ = 'CabFileTMultifill'
    id = Column(Integer, primary_key=True)
    uploadDate = Column(Date, nullable=False, server_default=func.curdate(), index=True)
    intSeqNo = Column(Integer)
    dteProcessDate = Column(Integer)
    txtTradeNumber = Column(String(6))
    intFillQty = Column(Numeric(17, 0))
    dblFillPrice = Column(Numeric(17, 8))
    txtFillFunds = Column(String(2))


class Postl(Base):
    __tablename__ = 'CabFileTPostl'
    id = Column(Integer, primary_key=True)
    uploadDate = Column(Date, nullable=False, server_default=func.curdate(), index=True)
    intSeqNo = Column(Integer)
    dteProcessDate = Column(Integer)
    txtTrailer = Column(String(25))


class Prupdt(Base):
    __tablename__ = 'CabFilePrupdt'
    id = Column(Integer, primary_key=True)
    uploadDate = Column(Date, nullable=False, server_default=func.curdate(), index=True)

    txtSecId = Column(String(20), primary_key=True)  # e.g. A03AN1
    dteCADPriceDate = Column(Date, nullable=True)
    dblCADLowPrice = Column(Numeric(10, 3), nullable=True)
    dblCADHighPrice = Column(Numeric(10, 3), nullable=True)
    dblCADClosePrice = Column(Numeric(10, 3), nullable=True)
    txtCADPriceSource = Column(String(20), nullable=True)

    dteUSDPriceDate = Column(Date, nullable=True)
    dblUSDLowPrice = Column(Numeric(10, 3), nullable=True)
    dblUSDHighPrice = Column(Numeric(10, 3), nullable=True)
    dblUSDClosePrice = Column(Numeric(10, 3), nullable=True)
    txtUSDPriceSource = Column(String(20), nullable=True)


class Dlyeval(Base):
    id = Column(Integer, primary_key=True)
    uploadDate = Column(Date, nullable=False, server_default=func.curdate(), index=True)

    __tablename__ = 'CabFileCSRDlyeval'
    dteProcessDate = Column(Integer)
    txtAcctNo = Column(String(7))
    dblTDMarketVal = Column(Numeric(15, 2))
    dblTDLoanVal = Column(Numeric(15, 2))
    dblTDReqMgn = Column(Numeric(15, 2))
    dblTDReqSec = Column(Numeric(15, 2))
    dblVDMarketVal = Column(Numeric(15, 2))
    dblVDLoanVal = Column(Numeric(15, 2))
    dblVDReqMgn = Column(Numeric(15, 2))
    dblVDReqSec = Column(Numeric(15, 2))
    dblVDBal = Column(Numeric(15, 2))


class Recon(Base):
    __tablename__ = 'CabFileCSRRecon'
    id = Column(Integer, primary_key=True)
    uploadDate = Column(Date, nullable=False, server_default=func.curdate(), index=True)

    dteProcessDate = Column(Integer)
    txtAcctNo = Column(String(7))
    txtSecId = Column(String(6))
    booQtyValid = Column(Integer)
    booAmtValid = Column(Integer)
    dblQuantity = Column(Numeric(15, 0))
    dblAmount = Column(Numeric(17, 2))
    txtBVtoMV = Column(String(1))


class Actsummbookval(Base):
    id = Column(Integer, primary_key=True)
    uploadDate = Column(Date, nullable=False, server_default=func.curdate(), index=True)

    __tablename__ = 'CabFileBVActsummbookval'
    account_number = Column('Account Number', String(7))
    plan_id = Column('Plan ID', String(2))
    acct_book_value_amt = Column('Acct Book Value Amt', Numeric(14, 2))
    acct_cash_amt = Column('Acct Cash Amt', Numeric(14, 2))
    acct_pct_foreign = Column('Acct Pct Foreign', Numeric(5, 2))
    rr_code = Column('RR Code', String(4))


class Secbookval(Base):
    id = Column(Integer, primary_key=True)
    uploadDate = Column(Date, nullable=False, server_default=func.curdate(), index=True)

    __tablename__ = 'CabFileBVSecbookval'
    account_number = Column('Account Number', String(7))
    instrument_id = Column('Instrument ID', String(12))
    rrsp_eligible = Column('RRSP eligible Y/N?', String(1))
    foreign_content = Column('Foreign content Y/N?', String(1))
    position_cost_qty = Column('Position cost QTY', Numeric(14, 0))
    position_book_value = Column('Position book value', Numeric(14, 2))
    date_last_updated = Column('Date last updated', String(10))
    position_suspect_ind = Column('Position Suspect Ind', String(3))


class Sec(Base):
    id = Column(Integer, primary_key=True)
    uploadDate = Column(Date, nullable=False, server_default=func.curdate(), index=True)

    __tablename__ = 'CabfileSMSec'
    lngSpecialMgnRate = Column(String(6))
    txtSecId = Column(String(6))
    txtSecType = Column(String(3))
    txtSecClass = Column(String(4))
    txtSecDescE = Column(String(25))
    txtSecDescF = Column(String(25))
    txtCurrency = Column(String(2))
    lngPayFreq = Column(Integer)
    sglPayRate = Column(Numeric(9, 5))
    lngFraction = Column(Integer)
    dteMaturity = Column(Integer)
    txtCusip = Column(String(12))
    txtSymbol = Column(String(26))
    txtCountry = Column(String(2))
    sglAnnualDiv = Column(Numeric(9, 5))
    booBBSEligInd = Column(Integer)
    booDTCEligInd = Column(Integer)
    booEuroclearEligInd = Column(Integer)
    booWCCCEligInd = Column(Integer)
    booDCSEligInd = Column(Integer)
    booRSPEligInd = Column(Integer)
    booRRSPKnownInd = Column(Integer)
    booFgnContentEligInd = Column(String(1))
    dteFgnContentEffDate = Column(Integer)
    booCCPCInd = Column(Integer)
    dblStrikePrice = Column(Numeric(15, 0))
    dteCallDate = Column(Integer)
    dteConversionDate = Column(Integer)
    txtWithholdingTaxPct = Column(String(2))
    txtSpecialInfo = Column(String(5))
    txtISIN = Column(String(17))
    txtUnderlyingSecId = Column(String(6))
    dblUnderlyingSecCADPrice = Column(Numeric(17, 6))
    dblUnderlyingSecUSDPrice = Column(Numeric(17, 6))
    txtLongEnglishDesc = Column(String(50))
    txtLongFrenchDesc = Column(String(50))
    dtePickupDate = Column(Integer)
    dteLastUpdate = Column(Integer)


class Secpr(Base):
    id = Column(Integer, primary_key=True)
    uploadDate = Column(Date, nullable=False, server_default=func.curdate(), index=True)

    __tablename__ = 'CabFileSMSecpr'
    txtSecId = Column(String(6))
    dteCADPriceDate = Column(Integer)
    dblCADLowPrice = Column(Numeric(17, 6))
    dblCADHighPrice = Column(Numeric(17, 6))
    dblCADClosePrice = Column(Numeric(17, 6))
    txtCADPriceSource = Column(String(7))
    dteUSDPriceDate = Column(Integer)
    dblUSDLowPrice = Column(Numeric(17, 6))
    dblUSDHighPrice = Column(Numeric(17, 6))
    dblUSDClosePrice = Column(Numeric(17, 6))
    txtUSDPriceSource = Column(String(7))
    dblCADCloseBidAskPrice = Column(Numeric(17, 6))
    dblUSDCloseBidAskPrice = Column(Numeric(17, 6))


class Symbols(Base):
    __tablename__ = 'CabFileSMSymbols'
    id = Column(Integer, primary_key=True)
    uploadDate = Column(Date, nullable=False, server_default=func.curdate(), index=True)

    BooMajorMkt1 = Column(String(1))
    BooMajorMkt2 = Column(String(1))
    BooMajorMkt3 = Column(String(1))
    BooMajorMkt4 = Column(String(1))
    BooMajorMkt5 = Column(String(1))
    BooMajorMkt6 = Column(String(1))
    txtCountry = Column(String(2))
    TxtCountry2 = Column(String(2))
    TxtCountry3 = Column(String(2))
    TxtCountry4 = Column(String(2))
    TxtCountry5 = Column(String(2))
    TxtCountry6 = Column(String(2))
    TxtMarket1 = Column(String(2))
    txtMarket2 = Column(String(2))
    txtMarket3 = Column(String(2))
    txtMarket4 = Column(String(2))
    txtMarket5 = Column(String(2))
    txtMarket6 = Column(String(2))
    txtSecId = Column(String(6))
    txtSymbol = Column(String(26))
    txtSymbolType = Column(String(1))


class Bonds(Base):
    id = Column(Integer, primary_key=True)
    uploadDate = Column(Date, nullable=False, server_default=func.curdate(), index=True)

    __tablename__ = 'CabFileSMBonds'
    txtSecId = Column(String(6))
    dteDatedDate = Column(Integer)
    dteFirstCpn = Column(Integer)
    dteNextCpn = Column(Integer)
    txtBondType = Column(String(1))
    txtCompoundBondInd = Column(String(1))
    dblInterestRate = Column(Numeric(8, 5))
    booFloatingRateInd = Column(String(1))
    booUseDatedRatesInd = Column(String(1))
    txtBondRating1 = Column(String(5))
    txtRatingSrc1 = Column(String(5))
    txtBondRating2 = Column(String(5))
    txtRatingSrc2 = Column(String(5))
    txtCouponDate2 = Column(Integer)
    txtCouponDate3 = Column(Integer)
    txtCouponDate4 = Column(Integer)
    txtRegistrationStatus = Column(String(1))


class Units(Base):
    id = Column(Integer, primary_key=True)
    uploadDate = Column(Date, nullable=False, server_default=func.curdate(), index=True)

    __tablename__ = 'CabFileSMUnits'
    txtSecId = Column(String(6))
    dteEffective = Column(Integer)
    dteEndDate = Column(Integer)
    dblUnitofMeas = Column(Numeric(13, 5))
    dblPFactRem = Column(Numeric(13, 9))
    txtMultDivInd = Column(String(1))
    dblDatedIntRate = Column(Numeric(9, 0))


class Div(Base):
    id = Column(Integer, primary_key=True)
    uploadDate = Column(Date, nullable=False, server_default=func.curdate(), index=True)

    __tablename__ = 'CabFileSMDiv'
    txtSecId = Column(String(6))
    dteRecordDate = Column(Integer)
    sglDivRate = Column(Numeric(11, 6))
    lngPayFreq = Column(Integer)
    dtePayDate = Column(Integer)
    txtDivCur = Column(String(2))
    dteExDivDate = Column(String(8))
    txtDistributionActivity = Column(String(2))
    dblSharesPerShareBase = Column(Numeric(11, 0))
    dblShareBase = Column(Numeric(5, 0))
    txtOptPayMethod = Column(String(1))
    txtFracShareCreate = Column(String(1))
    dblFractionValue = Column(Numeric(15, 0))
    txtIBMSecId = Column(String(6))
    txtSequenceCode = Column(String(1))
    txtDistributionSrc = Column(String(1))
    dteOmittedDivDate = Column(String(8))
    txtWithholdingTaxInfo = Column(String(2))
    txtPaymentTypeCode = Column(String(2))
    dblAnticipPayFreq = Column(Numeric(3, 0))
    txtDistributionDesc = Column(String(32))
    booRemoveSecPos = Column(String(1))
    dblDeemedValue = Column(Numeric(15, 8))
    dblPrincipalFactor = Column(Numeric(13, 10))
    dblInterestFactor = Column(Numeric(13, 10))
    txtIBMSecId2 = Column(String(6))


class Dsndp(Base):
    id = Column(Integer, primary_key=True)
    uploadDate = Column(Date, nullable=False, server_default=func.curdate(), index=True)

    __tablename__ = 'CabFileSMDsndp'
    txtSecId = Column(String(6))
    dteProcess = Column(String(10))
    txtBroker = Column(String(3))
    dteEffective = Column(String(10))
    dteExpiry = Column(String(10))
    txtBrokerID = Column(String(3))
    txtIndicator = Column(String(1))
    txtOverride = Column(String(1))
    txtAudit = Column(String(8))


# Mapping from file base names (without extension) to ORM models
# Accept both lowercase names like "accts" and title-cased special names
table_index = {
    "acclts": Acclts,
    "accts": Accts,
    "actpln": Actpln,
    "actsummbookval": Actsummbookval,
    "bonds": Bonds,
    "clients": Clients,
    "div": Div,
    "dlyeval": Dlyeval,
    "dsndp": Dsndp,
    "externid": Externid,
    "multfill": Multfill,
    "payments": Payments,
    "posdt": Posdt,
    "posli": Posli,
    "postd": Postd,
    "postl": Postl,
    "prupdt": Prupdt,
    "recon": Recon,
    "sec": Sec,
    "secbookval": Secbookval,
    "secpr": Secpr,
    "symbols": Symbols,
    "units": Units,
}

if __name__ == "__main__":
    from db import get_mysql_engine_from_env, get_qc_engine

    engine = get_mysql_engine_from_env(echo=True)
    qc_engine = get_qc_engine(echo=True)

    # print(qc_engine)

    Base.metadata.create_all(qc_engine)
    # Base.metadata.create_all(engine)

    print("Tables created successfully.")