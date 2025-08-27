import os
import re
from os import path
import pandas as pd

from db import get_mysql_engine_from_env

DEFAULT_OUT_DIR = "C:/uff/out"

from sqlalchemy import Column, Integer, Date, String, Numeric
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class CommonColumns:
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    uploadDate = Column(Date, default=datetime.utcnow)


class Clients(Base, CommonColumns):
    __tablename__ = 'Clients'
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


class Acclts(Base, CommonColumns):
    __tablename__ = 'CabFileAPAcclts'
    txtClientId = Column(String(20))
    txtAcctNo = Column(String(7))


class Accts(Base, CommonColumns):
    __tablename__ = 'CabFileAPAccts'
    txtAcctNo = Column(String(7))
    txtAcctType = Column(String(3))
    txtAcctCur = Column(String(3))
    txtAcctRR = Column(String(4))
    txtAcctSName = Column(String(16))
    txtPlanningCode = Column(String(2))
    txtAccountServiceCode = Column(String(12))
    txtEmployerGroupCode = Column(String(4))
    dteCloseDate = Column(Integer)


class Actpln(Base, CommonColumns):
    __tablename__ = 'CabFileAPActpln'
    txtAcctNo = Column(String(7))
    txtPensionOrigin = Column(String(2))


class Externid(Base, CommonColumns):
    __tablename__ = 'CabFileAPExternid'
    txtAcctNo = Column(String(7))
    txtExtrnSys = Column(String(8))
    txtExtrnSubSys = Column(String(8))
    txtExtrnId = Column(String(26))


class Payments(Base, CommonColumns):
    __tablename__ = 'CabFileAPIPayments'
    txtAcctNo = Column(String(7))
    txtInstitution = Column(Integer)
    txtBankBranch = Column(Integer)
    txtBankAcctNo = Column(Integer)
    txtPaymentId = Column(String(2))


class Posdt(Base, CommonColumns):
    __tablename__ = 'CabFileTPosdt'
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
    intQuantity = Column(Numeric(15,0))
    dblNetAmt = Column(Numeric(17,2))
    dblPrice = Column(Numeric(17,8))
    txtCur = Column(String(2))
    txtBVtoMV = Column(String(1))


class Posli(Base, CommonColumns):
    __tablename__ = 'CabFileTPosli'
    intSeqNo = Column(Integer)
    dteProcessDate = Column(Integer)
    txtLIType = Column(String(2))
    txtLICur = Column(String(2))
    dblLIAmt = Column(Numeric(17,2))


class Postd(Base, CommonColumns):
    __tablename__ = 'CabFileTPostd'
    intSeqNo = Column(Integer)
    dteProcessDate = Column(Integer)
    txtMarket = Column(String(2))
    dblFXRate = Column(Numeric(9,5))
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


class Multfill(Base, CommonColumns):
    __tablename__ = 'CabFileTMultifill'
    intSeqNo = Column(Integer)
    dteProcessDate = Column(Integer)
    txtTradeNumber = Column(String(6))
    intFillQty = Column(Numeric(17,0))
    dblFillPrice = Column(Numeric(17,8))
    txtFillFunds = Column(String(2))


class Postl(Base, CommonColumns):
    __tablename__ = 'CabFileTPostl'
    intSeqNo = Column(Integer)
    dteProcessDate = Column(Integer)
    txtTrailer = Column(String(25))


class Dlyeval(Base, CommonColumns):
    __tablename__ = 'CabFileCSRDlyeval'
    dteProcessDate = Column(Integer)
    txtAcctNo = Column(String(7))
    dblTDMarketVal = Column(Numeric(15,2))
    dblTDLoanVal = Column(Numeric(15,2))
    dblTDReqMgn = Column(Numeric(15,2))
    dblTDReqSec = Column(Numeric(15,2))
    dblVDMarketVal = Column(Numeric(15,2))
    dblVDLoanVal = Column(Numeric(15,2))
    dblVDReqMgn = Column(Numeric(15,2))
    dblVDReqSec = Column(Numeric(15,2))
    dblVDBal = Column(Numeric(15,2))


class Recon(Base, CommonColumns):
    __tablename__ = 'CabFileCSRRecon'
    dteProcessDate = Column(Integer)
    txtAcctNo = Column(String(7))
    txtSecId = Column(String(6))
    booQtyValid = Column(Integer)
    booAmtValid = Column(Integer)
    dblQuantity = Column(Numeric(15,0))
    dblAmount = Column(Numeric(17,2))
    txtBVtoMV = Column(String(1))


class Actsummbookval(Base, CommonColumns):
    __tablename__ = 'CabFileBVActsummbookval'
    account_number = Column('Account Number', String(7))
    plan_id = Column('Plan ID', String(2))
    acct_book_value_amt = Column('Acct Book Value Amt', Numeric(14,2))
    acct_cash_amt = Column('Acct Cash Amt', Numeric(14,2))
    acct_pct_foreign = Column('Acct Pct Foreign', Numeric(5,2))
    rr_code = Column('RR Code', String(4))


class Secbookval(Base, CommonColumns):
    __tablename__ = 'CabFileBVSecbookval'
    account_number = Column('Account Number', String(7))
    instrument_id = Column('Instrument ID', String(12))
    rrsp_eligible = Column('RRSP eligible Y/N?', String(1))
    foreign_content = Column('Foreign content Y/N?', String(1))
    position_cost_qty = Column('Position cost QTY', Numeric(14,0))
    position_book_value = Column('Position book value', Numeric(14,2))
    date_last_updated = Column('Date last updated', String(10))
    position_suspect_ind = Column('Position Suspect Ind', String(3))


class Sec(Base, CommonColumns):
    __tablename__ = 'CabfileSMSec'
    txtSecId = Column(String(6))
    txtSecType = Column(String(3))
    txtSecClass = Column(String(4))
    txtSecDescE = Column(String(25))
    txtSecDescF = Column(String(25))
    txtCurrency = Column(String(2))
    lngPayFreq = Column(Integer)
    sglPayRate = Column(Numeric(9,5))
    lngFraction = Column(Integer)
    dteMaturity = Column(Integer)
    txtCusip = Column(String(12))
    txtSymbol = Column(String(26))
    txtCountry = Column(String(2))
    sglAnnualDiv = Column(Numeric(9,5))
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
    dblStrikePrice = Column(Numeric(15,0))
    dteCallDate = Column(Integer)
    dteConversionDate = Column(Integer)
    txtWithholdingTaxPct = Column(String(2))
    txtSpecialInfo = Column(String(5))
    txtISIN = Column(String(17))
    txtUnderlyingSecId = Column(String(6))
    dblUnderlyingSecCADPrice = Column(Numeric(17,6))
    dblUnderlyingSecUSDPrice = Column(Numeric(17,6))
    txtLongEnglishDesc = Column(String(50))
    txtLongFrenchDesc = Column(String(50))
    dtePickupDate = Column(Integer)
    dteLastUpdate = Column(Integer)


class Secpr(Base, CommonColumns):
    __tablename__ = 'CabFileSMSecpr'
    txtSecId = Column(String(6))
    dteCADPriceDate = Column(Integer)
    dblCADLowPrice = Column(Numeric(17,6))
    dblCADHighPrice = Column(Numeric(17,6))
    dblCADClosePrice = Column(Numeric(17,6))
    txtCADPriceSource = Column(String(7))
    dteUSDPriceDate = Column(Integer)
    dblUSDLowPrice = Column(Numeric(17,6))
    dblUSDHighPrice = Column(Numeric(17,6))
    dblUSDClosePrice = Column(Numeric(17,6))
    txtUSDPriceSource = Column(String(7))
    dblCADCloseBidAskPrice = Column(Numeric(17,6))
    dblUSDCloseBidAskPrice = Column(Numeric(17,6))


class Symbols(Base, CommonColumns):
    __tablename__ = 'CabFileSMSymbols'
    txtSecId = Column(String(6))
    txtSymbolType = Column(String(1))
    txtSymbol = Column(String(26))
    txtCountry = Column(String(2))
    TxtMarket1 = Column(String(2))
    BooMajorMkt1 = Column(String(1))
    TxtCountry2 = Column(String(2))
    BooMajorMkt2 = Column(String(1))
    TxtCountry3 = Column(String(2))
    BooMajorMkt3 = Column(String(1))
    TxtCountry4 = Column(String(2))
    BooMajorMkt4 = Column(String(1))
    TxtCountry5 = Column(String(2))
    BooMajorMkt5 = Column(String(1))
    TxtCountry6 = Column(String(2))
    BooMajorMkt6 = Column(String(1))


class Bonds(Base, CommonColumns):
    __tablename__ = 'CabFileSMBonds'
    txtSecId = Column(String(6))
    dteDatedDate = Column(Integer)
    dteFirstCpn = Column(Integer)
    dteNextCpn = Column(Integer)
    txtBondType = Column(String(1))
    txtCompoundBondInd = Column(String(1))
    dblInterestRate = Column(Numeric(8,5))
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


class Units(Base, CommonColumns):
    __tablename__ = 'Units'
    txtSecId = Column(String(6))
    dteEffective = Column(Integer)
    dteEndDate = Column(Integer)
    dblUnitofMeas = Column(Numeric(13,5))
    dblPFactRem = Column(Numeric(13,9))
    txtMultDivInd = Column(String(1))
    dblDatedIntRate = Column(Numeric(9,0))


class Div(Base, CommonColumns):
    __tablename__ = 'CabFileSMDiv'
    txtSecId = Column(String(6))
    dteRecordDate = Column(Integer)
    sglDivRate = Column(Numeric(11,6))
    lngPayFreq = Column(Integer)
    dtePayDate = Column(Integer)
    txtDivCur = Column(String(2))
    dteExDivDate = Column(String(8))
    txtDistributionActivity = Column(String(2))
    dblSharesPerShareBase = Column(Numeric(11,0))
    dblShareBase = Column(Numeric(5,0))
    txtOptPayMethod = Column(String(1))
    txtFracShareCreate = Column(String(1))
    dblFractionValue = Column(Numeric(15,0))
    txtIBMSecId = Column(String(6))
    txtSequenceCode = Column(String(1))
    txtDistributionSrc = Column(String(1))
    dteOmittedDivDate = Column(String(8))
    txtWithholdingTaxInfo = Column(String(2))
    txtPaymentTypeCode = Column(String(2))
    dblAnticipPayFreq = Column(Numeric(3,0))
    txtDistributionDesc = Column(String(32))
    booRemoveSecPos = Column(String(1))
    dblDeemedValue = Column(Numeric(15,8))
    dblPrincipalFactor = Column(Numeric(13,10))
    dblInterestFactor = Column(Numeric(13,10))
    txtIBMSecId2 = Column(String(6))


class Dsndp(Base, CommonColumns):
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

table_index = {
    "acclts.txt": Acclts,
    "accts.txt": Accts,
    "actpln.txt": Actpln,
    "ActSummBookVal.txt": Actsummbookval,
    "bonds.txt": Bonds,
    "clients.txt": Clients,
    "div.txt": Div,
    "dlyeval.txt": Dlyeval,
    "dsndp.txt": Dsndp,
    "externid.txt": Externid,
    "multfill.txt": Multfill,
    "payments.txt": Payments,
    "posdt.txt": Posdt,
    "posli.txt": Posli,
    "postd.txt": Postd,
    "postl.txt": Postl,
    # "prupdt.txt": Prupdt,
    "recon.txt": Recon,
    "sec.txt": Sec,
    "SecBookVal.txt": Secbookval,
    "secpr.txt": Secpr,
    "symbols.txt": Symbols,
    "units.txt": Units,
}


def upload_all_csvs(out_dir=DEFAULT_OUT_DIR, engine=None, if_exists='replace', read_csv_kwargs=None):
    """
    Upload every CSV (or TXT) from out_dir to MySQL using SQLAlchemy engine.
    Table name is derived from the filename.

    Args:
      out_dir (str): directory containing CSV files
      engine: SQLAlchemy engine. If None, created from env vars via get_mysql_engine_from_env()
      if_exists: passed to pandas.DataFrame.to_sql ('replace'|'append'|'fail')
      read_csv_kwargs: optional dict passed to pandas.read_csv

    Returns:
      (successes, failures) lists. failures contain tuples (filename, error).
    """
    if engine is None:
        engine = get_mysql_engine_from_env()

    if read_csv_kwargs is None:
        read_csv_kwargs = {}

    if not path.exists(out_dir):
        raise FileNotFoundError(f"Output directory not found: {out_dir}")

    successes = []
    failures = []

    for fname in os.listdir(out_dir):
        fpath = path.join(out_dir, fname)
        if not path.isfile(fpath):
            continue

        if not fname.lower().endswith('.csv')):
            # skip non-csv files
            continue

        table_name = fname.lower().strip('.csv')
        try:
            df = pd.read_csv(fpath, **read_csv_kwargs)
            df.to_sql(table_name, con=engine, if_exists=if_exists, index=False)
            successes.append((fname, table_name))
            print(f"Uploaded {fname} -> {table_name}")
        except Exception as exc:
            failures.append((fname, str(exc)))
            print(f"Failed to upload {fname}: {exc}")

    return successes, failures

if __name__ == "__main__":
    engine = None
    try:
        engine = get_mysql_engine_from_env()
    except Exception as e:
        print(f"DB engine creation failed: {e}")
        raise

    out_dir = DEFAULT_OUT_DIR
    s, f = upload_all_csvs(out_dir=out_dir, engine=engine)
    print("Successes:", s)
    print("Failures:", f)